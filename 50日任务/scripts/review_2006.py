from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
notes=['低频是相对天气尺度而言，不能把所有低频变化等同MJO。MJO是季节内热带对流与环流耦合、活跃包络通常东移，30—60天为常用时间尺度而非严格周期；QBO为另一个尺度。参考：[NOAA MJO说明](https://psl.noaa.gov/mjo/)。', '东风波为热带东风背景中的波状扰动，典型向西传播；不能单凭西移或有对流就判东风波，也不能断言每个东风波必生成热带气旋。应分别说明波动传播和气块运动。', '上对流层狭长风速极大带和强切变定义正确；极锋、副热带西风急流的季节规律不能概括所有高空急流，热带还存在东风急流。原解“题中70—80 m/s”并非本题数据。', '先答强冷空气导致的大范围显著降温、大风及可能雨雪冻害，再写蓄积—环流调整—冷锋南下—锋后天气。原源地、路径、倒Ω为扩展，未给具体分类时不应作为每次寒潮必经阶段。', '原解混写地面冷高压、热低压与500 hPa，需分开。主答冬季中高纬西风强偏南、等高线密和定常槽明显，夏季西风弱北移、副高北抬；地面大陆热低压不能替代500 hPa高度场结构。', '题目问东亚环流，不能只讲副高。还应结合夏季风建立与北进、西风急流北移、中高纬冷空气活动，说明华南—江淮—华北东北雨带推进和秋季南撤；日期纬度为经验，不是每年固定时刻表。', '弱f、湿对流加热、辐散环流、Hadley与Walker均已涵盖。弱水平温差是热带大尺度背景近似，热带气旋等局地结构可有强梯度；也不能把低纬全部视为无旋转或处处上升。', '应突出水汽、可释放不稳定、触发抬升与合适垂直切变的配合。原解普通单体三阶段不能代替强雷暴持续机制：切变可帮助上升/下沉分离、保持暖湿入流或触发新单体；强切变和大CAPE均非单独充分条件。', '建立时改变下游槽脊、积聚冷空气并延长天气滞留；崩溃时环流调整可促冷空气南下。影响我国仍取决于阻高位置、季节、路径和水汽；不是任意欧亚阻塞崩溃均形成我国寒潮。']
source=root.parent/'动力气象课后习题/试题解答/往年试题解析/2006.md'
ids=re.findall(r'^## 题目 (.+)$',source.read_text(encoding='utf-8'),re.M)
assert len(ids)==len(notes)
review=dict(zip(ids,notes))
(root/'scripts/review_2006.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 for q,note in review.items():
  pattern=r'^(### '+re.escape(q)+r'[^\n]*)\n(?:\n\*\*本次复核提示（2026-11-01）：\*\* [^\n]*\n)?'
  s=re.sub(pattern,lambda m:m[1]+'\n\n**本次复核提示（2026-11-01）：** '+note+'\n',s,flags=re.M)
 p.write_text(s,encoding='utf-8')
p=root/'逐题复核记录.md';s=p.read_text(encoding='utf-8').replace('2005及2005_1年共213条记录','2005、2005_1及2006年共222条记录').replace('其余323题','其余314题')
lines=[]
for line in s.splitlines():
 m=re.match(r'\| \[([^\]]+)\]',line)
 if m and m[1] in review:
  line=line.replace('结构核对完成；学科内容待复核','内容复核（2026-11-01）').replace('仅核对题号、题干/解答段落，未据此宣称答案正确。',review[m[1]].replace('|',r'\|'))
 lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Reviewed',len(review),'questions')
