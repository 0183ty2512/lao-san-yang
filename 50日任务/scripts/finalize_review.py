"""Merge review records and remove redundant adjacent source reminders."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
data={}
for name in ['review_optional.json','review_weather_applied.json','review_dynamics_evidence.json']:
    data.update(json.loads((root/'scripts'/name).read_text(encoding='utf-8')))
p=root/'逐题复核记录.md';lines=p.read_text(encoding='utf-8').splitlines()
statuses={}
for i,l in enumerate(lines):
    m=re.match(r'\| \[([^\]]+)\]',l)
    if not m:continue
    if m[1] in data:
        e=data[m[1]]
        lines[i]=l.split(' | ')[0]+' | '+e['status']+' | '+e['note'].replace('|',r'\|')+' |'
    statuses[m[1]]=lines[i].split(' | ')[1]
pending=sum('待核' in s for s in statuses.values())
missing=sum('缺题' in s for s in statuses.values())
omitted=sum('仅核对任务范围' in s for s in statuses.values())
reviewed=len(statuses)-pending-missing-omitted
lines[2]=f'2026-11-04。全部{len(statuses)}条年度题均已检查：{reviewed}条完成内容复核（含28条原卷标略的拓展选读），{pending}条仍缺原卷信息或指定教材口径，{missing}条缺题。待核及缺题不计作答案核验通过。模拟卷附录另见复核依据目录中的逐题记录，不与年度题混计。'
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
dedup=0;labels=0
for p in (root/'每日内容').glob('D*.md'):
    s=p.read_text(encoding='utf-8')
    def label(m):
        global labels
        q=m[1];body=m[0]
        old='**审校状态：尚未逐题学科审校。**'
        if q in statuses and old in body:
            labels+=body.count(old)
            body=body.replace(old,'**本题复核状态：'+statuses[q]+'。**')
        return body
    s=re.sub(r'^### ([\d_]+-[一二三四五六]+-[^ ·\n]+) ·[^\n]*\n[\s\S]*?(?=^#{1,3} |\Z)',label,s,flags=re.M)
    pattern=r'(^本段与前文重复，已合并；[^\n]+\n)(?:\n\1)+'
    s,n=re.subn(pattern,r'\1',s,flags=re.M);dedup+=n
    p.write_text(s,encoding='utf-8')
print(lines[2]);print('Updated stale labels:',labels,'collapsed repeated source reminders:',dedup)
for p in [root/'逐题复核记录.md',*(root/'每日内容').glob('D*.md'),*(root/'复核依据').glob('*.md')]:
    s=p.read_text(encoding='utf-8')
    s=re.sub(r'(https://github\.com/0183ty2512/lao-san-yang/blob/[^)\s]*?\.md)#(L\d+)',r'\1?plain=1#\2',s)
    p.write_text(s,encoding='utf-8')
