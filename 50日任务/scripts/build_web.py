"""Build the GitHub Pages reader from the same Markdown files used for email."""
from hashlib import sha256
from html import escape
from pathlib import Path
from urllib.parse import quote
import json
import re
import shutil
import subprocess

import markdown
from web_layout import index_body, lesson_header, page
from web_outline import prepare_outline


scripts = Path(__file__).resolve().parent
root = scripts.parent
out = root.parent / 'docs'
manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
review_url = 'https://github.com/0183ty2512/lao-san-yang/blob/main/' + quote('50日任务/逐题复核记录.md')
math_pattern = re.compile(r'\$\$[\s\S]*?\$\$|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|(?<!\\)\$(?!\$)[^$]+?(?<!\\)\$')
expressions = []


def save_math(match):
    raw = match[0]
    paired = raw.startswith(('$$', r'\(', r'\['))
    trim = 2 if paired else 1
    number = len(expressions)
    expressions.append({'tex': raw[trim:-trim], 'display': raw.startswith(('$$', r'\['))})
    return f'SVGFORMULA{number}END'


def review_note():
    rows = (root / '逐题复核记录.md').read_text(encoding='utf-8').splitlines()
    statuses = [row.split(' | ')[1] for row in rows if row.startswith('| [')]
    pending = sum('待核' in value for value in statuses)
    missing = sum('缺题' in value for value in statuses)
    scoped = sum('仅核对任务范围' in value for value in statuses)
    unchecked = sum('学科内容待复核' in value for value in statuses)
    reviewed = len(statuses) - pending - missing - scoped - unchecked
    summary = f'年度题共{len(statuses)}条，{reviewed}条完成内容复核，{pending}条待核，{missing}条缺题。'
    if scoped or unchecked:
        summary += f'{scoped}条仅核对任务范围，{unchecked}条尚待内容复核。'
    return ('<details class="review-note"><summary>资料来源与复核记录</summary><p>课程依据原50日计划和仓库学习资料整理。'
            + escape(summary) + f'模拟卷单列复核。 <a href="{review_url}">查看逐题记录与依据</a></p></details>')


def prepare_lesson(item):
    text = (root / item['file']).read_text(encoding='utf-8')
    # The shared title, date, workload and source note are presented in the reader header.
    first_section = re.search(r'^## ', text, re.M)
    if not first_section:
        raise ValueError(f"日课缺少章节：{item['file']}")
    body = text[first_section.start():].replace('**审校状态：', '**题目审校信息：')
    protected = math_pattern.sub(save_math, body)
    content = markdown.markdown(protected, extensions=['tables', 'fenced_code', 'sane_lists'])
    return prepare_outline(content, text)


def main():
    lessons = [prepare_lesson(item) for item in manifest]
    (scripts / 'formulas.json').write_text(json.dumps(expressions, ensure_ascii=False), encoding='utf-8')
    subprocess.run(['node', str(scripts / 'render_math.cjs')], check=True)
    rendered = json.loads((scripts / 'rendered.json').read_text(encoding='utf-8'))
    if len(rendered) != len(expressions):
        raise ValueError('公式数量与排版结果不一致')

    def formula(match):
        number = int(match[1])
        style = 'math-scroll block' if expressions[number]['display'] else 'math-scroll'
        return (f'<span class="{style}" tabindex="0" role="region" aria-label="数学公式，可横向滚动">'
                + rendered[number] + '</span>')

    out.mkdir(exist_ok=True)
    (out / 'md').mkdir(exist_ok=True)
    css = (scripts / 'web/reader.css').read_bytes()
    js = (scripts / 'web/reader.js').read_bytes()
    version = sha256(css + js).hexdigest()[:12]
    (out / 'style.css').write_bytes(css)
    (out / 'theme.js').write_bytes(js)
    review = review_note()
    for item, (content, sections) in zip(manifest, lessons):
        number = item['day']
        content = re.sub(r'SVGFORMULA(\d+)END', formula, content)
        body = (lesson_header(item, len(manifest)) +
                '<article class="lesson-paper"><div class="lesson-content">' + content + '</div></article>' + review)
        document = page(f"D{number:02} · {item['title']}", body, manifest, number, sections, version)
        (out / f'D{number:02}.html').write_text(document, encoding='utf-8')
        shutil.copyfile(root / item['file'], out / 'md' / f'D{number:02}.md')
    index = page('大气科学50日复习计划', index_body(manifest, review), manifest, asset_version=version)
    (out / 'index.html').write_text(index, encoding='utf-8')
    (out / '.nojekyll').touch()
    print(f'Built {len(manifest)} lessons, {sum(len(entries) for _, entries in lessons)} outline entries, {len(rendered)} formulas.')


if __name__ == '__main__':
    main()
