from pathlib import Path
import json,re,html,markdown,shutil
root=Path(__file__).resolve().parents[1]; out=root.parent/'docs'; out.mkdir(exist_ok=True)
manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
css='''[hidden]{display:none!important}*{box-sizing:border-box}body{margin:0;background:#f3f5f8;color:#253248;font:17px/1.85 system-ui,"Microsoft YaHei",sans-serif}header,main,footer{max-width:1040px;margin:auto;padding:24px}header{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}a{color:#245dac;text-decoration:none}a:hover{text-decoration:underline}article{background:white;padding:clamp(20px,5vw,64px);border-radius:16px;box-shadow:0 8px 35px #20305009}h1{font-size:clamp(26px,4vw,38px);line-height:1.45}h2{margin-top:48px;border-bottom:1px solid #dce3eb;padding-bottom:12px}h3{margin-top:32px}blockquote{border-left:3px solid #6c90b9;margin:20px 0;padding:10px 20px;background:#f1f6fb}table{display:block;overflow:auto;border-collapse:collapse}td,th{border:1px solid #d9e1eb;padding:9px}mjx-container[display="true"]{overflow-x:auto;overflow-y:hidden;padding:10px 0}nav{display:flex;gap:20px;flex-wrap:wrap}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px}.card{display:block;padding:22px;background:white;border-radius:12px;border:1px solid #dce3eb}.card small{display:block;color:#64748b}input{padding:12px;font:inherit;width:100%;margin-bottom:25px;border:1px solid #cbd5e1;border-radius:8px}@media print{header,footer{display:none}body{background:white}article{box-shadow:none;padding:0}}'''
(out/'style.css').write_text(css,encoding='utf-8')
math=r'''<script>window.MathJax={tex:{inlineMath:[['$','$'],['\\(','\\)']],displayMath:[['$$','$$'],['\\[','\\]']],processEscapes:true},svg:{fontCache:'local'}};</script><script defer src="mathjax/tex-svg.js"></script>'''
def page(title,body,nav=''):
 return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><link rel="stylesheet" href="style.css">'+math+'</head><body><header><a href="index.html">大气科学 · 50日复习</a><nav>'+nav+'</nav></header><main>'+body+'</main><footer>学习整理版 · 非官方评分标准 · 来源见各题链接</footer></body></html>'
count=0
for m in manifest:
 d=m['day']; source=(root/m['file']).read_text(encoding='utf-8'); saved=[]
 def protect(match):
  saved.append(html.escape(match[0]));return 'MATHPLACEHOLDER'+str(len(saved)-1)+'TOKEN'
 source=re.sub(r'\$\$[\s\S]*?\$\$|(?<!\\)\$(?!\$)[^\n$]+?(?<!\\)\$',protect,source)
 content=markdown.markdown(source,extensions=['tables','fenced_code','sane_lists'])
 for i,v in enumerate(saved):content=content.replace('MATHPLACEHOLDER'+str(i)+'TOKEN',v)
 count+=len(saved)
 nav=(f'<a href="D{d-1:02}.html">← 上一天</a>' if d>1 else '')+f'<a href="md/D{d:02}.md" download>下载 MD</a>'+(f'<a href="D{d+1:02}.html">下一天 →</a>' if d<50 else '')
 (out/f'D{d:02}.html').write_text(page(m['title'],'<article>'+content+'</article>',nav),encoding='utf-8')
 (out/'md').mkdir(exist_ok=True);shutil.copyfile(root/m['file'],out/'md'/f'D{d:02}.md')
cards=''.join(f'<a class="card" href="D{m["day"]:02}.html"><small>D{m["day"]:02} / {m["date"]}</small>{html.escape(m["title"])}</a>' for m in manifest)
body='<h1>每天四小时，把知识写成答案。</h1><p>2026.10.29 — 12.17 · 50天学习计划<br>真题、解析、公式推导与来源，在这里逐日阅读。</p><input id="search" aria-label="搜索学习内容" placeholder="搜索天数、日期或知识点…"><div class="grid">'+cards+'</div><script>document.querySelector("#search").addEventListener("input",e=>document.querySelectorAll(".card").forEach(c=>c.hidden=!c.textContent.toLowerCase().includes(e.target.value.toLowerCase())));</script>'
(out/'index.html').write_text(page('50日大气科学复习',body),encoding='utf-8');(out/'.nojekyll').touch()
print('Built 50 pages; protected math expressions:',count)
