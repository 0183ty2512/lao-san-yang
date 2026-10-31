from pathlib import Path
import re,json,collections
root=Path(__file__).resolve().parents[1]
folder=root.parent/'动力气象课后习题/试题解答/往年试题解析'
freq={};topics={};years=collections.defaultdict(set)
for p in folder.glob('*.md'):
 if not re.fullmatch(r'\d{4}(_1)?',p.stem):continue
 for b in re.split(r'^## 题目 ',p.read_text(encoding='utf-8'),flags=re.M)[1:]:
  q=b.splitlines()[0].strip(); section=b.split('### 考点与考察频次')[-1].split('### 难度')[0]
  ts=re.findall(r'^\| ([^|]+?) \| \d+ 次 \|',section,re.M);topics[q]=ts
  for t in ts:years[t].add(p.stem[:4])
for q,ts in topics.items():freq[q]=max([len(years[t]) for t in ts] or [1])
def normalize(m):
 s=m[0]
 s=re.sub(r'\\partial_(?:\{([txypz])\}|([txypz])(?![A-Za-z*^]))',lambda a:r'\frac{\partial}{\partial '+(a[1] or a[2])+'}',s)
 # Only unambiguous single-coordinate subscripts; retain level labels u_t,p_t and accented fields.
 s=re.sub(r'(?<![A-Za-z\\])((?:\\(?:Phi|psi|chi|zeta|omega)|[uvTwU])\x27?)_([xy]{1,2})(?![A-Za-z*^])',lambda a:r'\frac{\partial'+('^2' if len(a[2])==2 else '')+' '+a[1]+'}{'+(r'\partial '+a[2] if len(a[2])==1 else r'\partial '+a[2][0]+'^2' if a[2][0]==a[2][1] else r'\partial '+a[2][0]+r'\partial '+a[2][1])+'}',s) if not re.search(r'\\(?:bar|overline|hat)',s) else s
 s=re.sub(r'\\partial\s*([A-Za-z]|\\[A-Za-z]+)\s*/\s*\\partial\s*([txypz])',lambda a:r'\frac{\partial '+a[1]+r'}{\partial '+a[2]+'}',s)
 return s

removed=0
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 s=re.sub(r'\n> 星级口径：[^\n]*\n','\n',s)
 s=s.replace('## 逐题回忆与简答','> 星级口径：按同考点在不同年份的出现次数，1次★、2—3次★★、4—6次★★★、7—10次★★★★、11次及以上★★★★★；多考点题取最高频考点。星级表示复习频次，不是命题概率。\n\n## 逐题回忆与简答')
 s=re.sub(r'^(### (\d{4}(?:_1)?-[^\n·]+?))(?: · [★☆]+[^\n]*)?$',lambda m:m[1]+' · '+'★'*(1 if freq.get(m[2].strip(),1)==1 else 2 if freq.get(m[2].strip(),1)<=3 else 3 if freq.get(m[2].strip(),1)<=6 else 4 if freq.get(m[2].strip(),1)<=10 else 5)+f'（同考点{freq.get(m[2].strip(),1)}年）',s,flags=re.M)
 # Exact repeated long paragraphs become pointers; question headings and source links remain.
 seen={};paras=s.split('\n\n');out=[]
 for para in paras:
  key=para.strip()
  if len(key)>100 and not key.startswith(('#','[','>','|')) and key in seen:
   out.append('本段与上文相同，可回看前面的解析，不再重复展开。');removed+=1
  else:
   out.append(para);seen[key]=True
 s='\n\n'.join(out)
 s=re.sub(r'\$\$[\s\S]*?\$\$|(?<!\\)\$(?!\$)[^$]+?(?<!\\)\$',normalize,s)
 p.write_text(s,encoding='utf-8')
(root/'考点频次星级.json').write_text(json.dumps({t:{'years':sorted(y),'count':len(y)} for t,y in years.items()},ensure_ascii=False,indent=2),encoding='utf-8')
print('Reduced paragraphs:',removed,'; rated questions:',len(freq))
