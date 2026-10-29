from pathlib import Path
import re, json, datetime, urllib.parse
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'50日任务'; DAYS=OUT/'每日内容'; DAYS.mkdir(exist_ok=True)
BASE='https://github.com/0183ty2512/lao-san-yang/blob/main/'
files=list(ROOT.rglob('*.md'))
def url(p,line=None):
 return BASE+urllib.parse.quote(p.relative_to(ROOT).as_posix())+(f'#L{line}' if line else '')
def links(s):
 def sub(m):
  v=m[1].split('|'); target=v[0].split('#')[0]; label=v[-1]; name=target.split('/')[-1]
  matches=[p for p in files if p.stem==name]
  if not matches:return label+'（库内引用未定位）'
  p=next((p for p in matches if p.relative_to(ROOT).as_posix().removesuffix('.md').endswith(target.removeprefix('牢三样/'))),matches[0])
  return f'[{label}]({url(p)})'
 return re.sub(r'\[\[([^\]]+)\]\]',sub,s)
folder=ROOT/'动力气象课后习题/试题解答/往年试题解析'
records=[]
for p in sorted([p for p in folder.glob('*.md') if re.fullmatch(r'\d{4}(_1)?',p.stem)],reverse=True):
 s=p.read_text(encoding='utf-8'); ms=list(re.finditer(r'^## 题目 (.+)$',s,re.M))
 for i,m in enumerate(ms):
  body=s[m.end():ms[i+1].start() if i+1<len(ms) else len(s)]
  def section(title):
   match=re.search(r'### '+title+r'\s*\n(.*?)(?=\n### |\Z)',body,re.S); return match[1].strip() if match else ''
  records.append(dict(id=m[1].strip(),p=p,line=s[:m.start()].count('\n')+1,question=section('原题'),short=section('考场精简版与审校状态'),detail=section('详细解答'),body=body))
assert len(records)==536,len(records)
import fitz
text='\n'.join(p.get_text() for p in fitz.open(OUT/'50天复习逐日安排_紧凑公式版.pdf'))
plan=re.findall(r'D(\d{2})\n(\d+/\d+)\n([^\n]+)',text); assert len(plan)==50,len(plan)
manifest=[]; offset=0; covered=[]
for ds,dt,title in plan:
 day=int(ds); date=(datetime.date(2026,10,29)+datetime.timedelta(days=day-1)).isoformat()
 if 4<=day<=26:
  n=24 if day<=10 else 23; selected=records[offset:offset+n]; offset+=n; covered += [r['id'] for r in selected]
 else:
  terms=[t for t in re.split(r'[、／；：，。·\s]+',title) if len(t)>1]
  keys={'地转风':['地转','热成风'],'云微物理':['凝结','冰晶'],'波动':['波','频散'],'动力气象学':['涡度','位涡','地转','波动'],'天气学原理':['锋','气旋','季风','寒潮'],'大气物理学':['辐射','绝热','凝结'],'三科':['地转','锋','辐射']}
  for k,v in keys.items():
   if k in title:terms+=v
  if 40<=day<=46:terms=['地转','涡度','锋','梅雨','辐射','位温']
  ranked=sorted(records,key=lambda r:sum(3*(t in r['question'])+(t in r['body']) for t in terms),reverse=True)
  selected=[]
  for t in terms:
   choices=sorted(records,key=lambda r:3*(t in r['question'])+(t in r['body']),reverse=True)
   for r in choices:
    if r not in selected and (t in r['body']):
     selected.append(r); break
  for r in ranked:
   if len(selected)>=12:break
   if r not in selected:selected.append(r)
 full=sorted(selected,key=lambda r:len(r['detail']),reverse=True)[:5]
 out=[f'# D{ds} · {title}',f'日期：{date}｜建议投入：4小时｜动力40% · 天气40% · 物理20%', '> 本学习包依据原50日PDF与仓库学习资料整理。参考答案不是官方评分标准；未完成学科审校及缺题标记均保留。公式采用 GitHub 数学 Markdown，请在 GitHub 正文或 Obsidian 阅读视图打开。', '## 今日目标与记忆标准','闭卷说清概念、适用条件、符号与单位；推导必须写出起始方程、近似及关键步骤。先答题，再展开核对。', '## 四小时执行','1. 20分钟：回忆此前第1、3、7、14天的重点，尚未开始的日期跳过。\n2. 80分钟：逐题闭卷提取，核对以下简答与来源。\n3. 70分钟：精选5题完整书写。名词解释90秒、简答7分钟、论述12分钟为训练目标。\n4. 40分钟：把本日知识按“假设→方程→物理机制→天气表现”串成2—4条知识链。\n5. 30分钟：记录遗漏点、用时与次日/3日/7日/14日复习日期。','## 逐题回忆与简答']
 for r in selected:
  out += [f"### {r['id']}",r['question'],f"[解析来源（对应题目行）]({url(r['p'],r['line'])}) · [原始年度题干]({url(ROOT/'往年试题分析'/(r['p'].stem+'.md'))})",r['short'] if '针对本题' in r['short'] else r['short']+'\n\n'+r['detail']]
 out += ['## 精选完整解析与公式推导','以下保留资料中的条件、步骤和审校信息。先完成手写，再核对。']
 for r in full:out += [f"### {r['id']} · 完整解答",r['question'],r['detail'],f"[核对原文]({url(r['p'],r['line'])})"]
 if 40<=day<=46:
  num={40:'一',41:'一',42:'二',43:'二',44:'三',45:'三',46:'四'}[day]; p=ROOT/'模拟试题'/f'模拟试题{num}.md'
  out += ['## 限时模拟与复盘', '练习日先闭卷作答后看答案；复盘日按上一份答卷逐项标注漏点，原卷分值保持原样，不另称官方150分卷。',f'[模拟卷原资料]({url(p)})',p.read_text(encoding='utf-8')]
 if day==39:
  p=folder/'01_考点频次与证据总表.md'; out += ['## 高频考点完整核对',f'[频次与证据总表]({url(p)})',p.read_text(encoding='utf-8')]
 out += ['## 当日验收','- [ ] 本日每题均完成至少一次闭卷提取。\n- [ ] 精选题写清假设、符号与中间步骤；无漏负号、下标和单位。\n- [ ] 能用自己的话解释至少两条跨章节联系。\n- [ ] 错题记录包含题号、错因、修正答案及下一次复习日期。']
 name=f'D{ds}.md'; content=links('\n\n'.join(out))+'\n'; (DAYS/name).write_text(content,encoding='utf-8')
 manifest.append(dict(day=day,date=date,title=title,file='每日内容/'+name,questions=[r['id'] for r in selected]))
assert offset==536 and len(set(covered))==536
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'README.md').write_text('# 50日复习任务\n\n依据原PDF：2026-10-29至2026-12-17。每日北京时间10:30（日本时间11:30）。\n\n公式请使用 GitHub 正文或 Obsidian 阅读视图；不要使用纯文本预览。536条历年记录已按PDF顺序完整覆盖、不重复。来源链接定位到原题解析行。其余阶段提供专题选题和完整解析。\n\n'+ '\n'.join(f"- [{m['date']} D{m['day']:02} · {m['title']}]({m['file']})" for m in manifest)+'\n',encoding='utf-8')
print('Generated 50 days; verified 536 unique records.')
