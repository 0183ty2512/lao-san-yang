"""Add addressable reading targets without rewriting the lesson's rendered math."""

import html
import re
from itertools import count


QUESTION_ID = r"\d{4}(?:_\d+)?-[一二三四五六七八九十]+-(?:\d+|整题)"
QUESTION_BLOCK = re.compile(
    rf"^### (?P<qid>{QUESTION_ID}) · [^\n]*\n(?P<body>[\s\S]*?)(?=^#{{1,3}} |\Z)",
    re.MULTILINE,
)
MATH = re.compile(r"\$\$[\s\S]*?\$\$|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|(?<!\\)\$[^$]+?(?<!\\)\$")
# All three block shapes are emitted by Python-Markdown, after math protection.
BLOCK = re.compile(
    r"^<(?P<heading>h[1-3])(?: [^>]*)?>(?P<title>.*?)</(?P=heading)>"
    r"|^<p(?: [^>]*)?><strong>(?P<number>\d+)[.．、] (?P<answer>[^<\n]+)</strong></p>"
    r"|^<ol(?: [^>]*)?>(?P<items>[\s\S]*?)</ol>",
    re.MULTILINE,
)
EXISTING_ID = re.compile(r"""\bid=(["'])(.*?)\1""")
ITEM = re.compile(r"<li(?: [^>]*)?>([\s\S]*?)</li>")
MOCK_TITLE = re.compile(r"模拟试题([一二三四五六七八九十]+)(?:\s*·\s*(参考答案))?")
MOCK_SECTION = re.compile(r"([一二三四])、([^（(]+)")


def plain(text):
    """Only clean the navigation label; the original text stays in the document."""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"(?:SVGFORMULA\d+END|MATHPLACEHOLDER\d+TOKEN)", "公式", text)
    return " ".join(html.unescape(text).split())


def question_topics(source):
    topics = {}
    for match in QUESTION_BLOCK.finditer(source):
        qid = match["qid"]
        if qid in topics:
            continue
        before_links = match["body"].partition("[解析来源")[0]
        for paragraph in re.split(r"\n\s*\n", before_links):
            paragraph = paragraph.strip()
            if not paragraph or paragraph.startswith(("**本次复核提示", "<a ", "[", ">")):
                continue
            paragraph = re.sub(r"^\*\*原资料填空记载（待核）：\*\*\s*", "", paragraph)
            topic = plain(MATH.sub("公式", paragraph).replace("**", "").replace("\x60", ""))
            if topic:
                topics[qid] = shorten(topic.rstrip("：:"), 60)
                break
    return topics


def shorten(text, limit):
    return text if len(text) <= limit else text[:limit - 1].rstrip() + "…"


def slug(label):
    return re.sub(r"[^\w-]+", "-", label.lower()).strip("-") or "section"


def prepare_outline(content, source):
    """Return HTML with focusable anchors plus ordered, plain-text drawer entries."""
    topics = question_topics(source)
    occupied = {html.unescape(m[2]) for m in EXISTING_ID.finditer(content)}
    occupied.add("lesson-start")
    entries = [{"id": "lesson-start", "level": 1, "label": "本页开头", "meta": ""}]
    mock_name = mock_mode = section = section_name = ""

    def attach(block, wanted_id, level, label, meta=""):
        opening, tail = block.split(">", 1)
        existing = EXISTING_ID.search(opening)
        if existing:
            target = html.unescape(existing[2])
        else:
            target = wanted_id
            serial = 2
            while target in occupied:
                target = f"{wanted_id}-{serial}"
                serial += 1
            occupied.add(target)
            opening += f' id="{html.escape(target, quote=True)}"'
        if " tabindex=" not in opening:
            opening += ' tabindex="-1"'
        entries.append({"id": target, "level": level, "label": label, "meta": meta})
        return opening + ">" + tail

    def index_block(match):
        nonlocal mock_name, mock_mode, section, section_name
        if match["heading"]:
            level = int(match["heading"][1])
            title = plain(match["title"])
            if not title:
                return match[0]
            if level == 1:
                mock = MOCK_TITLE.fullmatch(title)
                section = section_name = ""
                mock_name = mock[1] if mock else ""
                mock_mode = ("答案" if mock[2] else "试题") if mock else ""
            elif level == 2:
                part = MOCK_SECTION.fullmatch(title.split("（")[0]) if mock_name else None
                section = part[1] if part else ""
                section_name = part[2] if part else ""
                if not part:
                    mock_name = mock_mode = ""

            question = re.match(rf"^({QUESTION_ID}) · (.+)$", title)
            if question:
                qid, suffix = question.groups()
                solution = "完整解答" in suffix
                target = ("solution-" if solution else "q-") + qid
                label = qid + (" · 完整解答" if solution else "")
                return attach(match[0], target, 3, label, topics.get(qid, ""))

            if mock_name and section:
                context = f"模拟{mock_name} · {mock_mode}"
                target = f"mock-{mock_name}-{mock_mode}-{section}"
                return attach(match[0], target, level, title, context)
            return attach(match[0], "section-" + slug(title), level, title)

        if not (mock_name and section):
            return match[0]
        prefix = f"mock-{mock_name}-{mock_mode}-{section}"
        meta = f"模拟{mock_name} · {mock_mode} · {section_name}"
        if match["number"] and mock_mode == "答案":
            number = match["number"]
            return attach(match[0], f"{prefix}-{number}", 3,
                          f"{number}. {plain(match['answer'])}", meta)
        if match["items"] and mock_mode == "试题":
            start = re.match(r'<ol start="(\d+)">', match[0])
            numbers = count(int(start[1]) if start else 1)

            def index_item(item):
                number = next(numbers)
                label = f"{number}. {shorten(plain(item[1]), 64)}"
                return attach(item[0], f"{prefix}-{number}", 3, label, meta)

            return ITEM.sub(index_item, match[0])
        return match[0]

    return BLOCK.sub(index_block, content), entries
