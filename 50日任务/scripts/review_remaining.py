"""Apply individually authored review notes, preserving source transcripts."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'scripts/review_remaining.json').read_text(encoding='utf-8'))
for p in (root/'每日内容').glob('D*.md'):
    s=p.read_text(encoding='utf-8')
    for q,entry in data.items():
        pattern=r'^(### '+re.escape(q)+r'[^\n]*)\n(?:\n\*\*本次复核提示（\d{4}-\d{2}-\d{2}）：\*\* [^\n]*\n)*'
        s=re.sub(pattern,lambda m:m[1]+'\n\n**本次复核提示（2026-11-02）：** '+entry['note']+'\n',s,flags=re.M)
    p.write_text(s,encoding='utf-8')
p=root/'逐题复核记录.md'
lines=p.read_text(encoding='utf-8').splitlines()
for i,line in enumerate(lines):
    m=re.match(r'\| \[([^\]]+)\]',line)
    if m and m[1] in data:
        e=data[m[1]]
        prefix=line.split(' | ')[0]
        lines[i]=prefix+' | '+e.get('status','内容复核（2026-11-02）')+' | '+e['note'].replace('|',r'\|')+' |'
rows=[l for l in lines if l.startswith('| [')]
pending=sum('结构核对完成；学科内容待复核' in l for l in rows)
unresolved=sum('待核' in l.split(' | ')[1] for l in rows)
omitted=sum('仅核对任务范围' in l for l in rows)
missing=sum('缺题' in l.split(' | ')[1] for l in rows)
lines[2]=f'2026-11-02。全部{len(rows)}条记录中，{len(rows)-pending-unresolved-missing-omitted}条完成内容复核；{unresolved}条保留原卷或教材口径疑点；{missing}条缺题无法审核答案；{omitted}条原卷标略仅核对任务范围。尚未检查{pending}条。待核、缺题及范围核对不计作答案核验通过，公式成功渲染也不等于学科正确。具体条件与修订见下表。'
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(lines[2])
