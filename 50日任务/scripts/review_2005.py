from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
notes=['需分别定义：阻塞高压使中高纬西风绕行并持续停滞；切断低压是从主西风带槽中分离的闭合低压，典型为高空冷涡。两者可配对但不必同时存在，切断低压也未必对应明显地面低压中心。', '静力式应写$\\frac{\\partial p}{\\partial z}=-\\rho g$，物理意义为向上的垂直气压梯度力与重力平衡。竖直加速度可忽略，不等于竖直速度为零；位势与测高公式属于扩展内容。', '低压系统须有相对低压扰动及相应环流，中尺度范围、寿命只是典型特征。切变线并不自动等于低压，强非地转运动也不是每个中尺度低压的必备条件。', '原题括号容易误导，必须分开答：条件不稳定为$\\Gamma_m<\\Gamma<\\Gamma_d$；位势不稳定为$\\frac{\\partial\\theta_e}{\\partial z}<0$，针对整层抬升。二者并非同义，前者比较气块饱和状态，后者比较整层湿热分布。', '重点为季节推进与雨带对应：春初夏偏南、梅雨阶段北抬、盛夏进一步北跳、秋季南撤；同时解释西伸东退与持续性。纬度和日历日期为经验，不能忽略冷空气、水汽及年际差异。', '原解气旋内容明显多于反气旋，补齐形成条件：温带气旋常依斜压取能及高低空配置发展；冷高压由冷却和冷空气积聚并与高空环流配合，暖性副高由大尺度下沉及热力/行星波共同维持。天气比较为气旋常云雨、反气旋中心常少云，但冷高压前缘可大风雨雪、副高边缘可暴雨；两类都可能有强风，不能作晴雨绝对分类。', '待核教材图：题目明确只问双阻型，不能用一般梅雨配置充当完整答案。可确定框架为两处中高纬阻塞维持其间/下游冷槽，与副高北缘暖湿输送配合形成持续雨带；两阻中心、槽位置及高层配置需对照指定教材双阻型图，原资料未给足依据。', '海陆热力差异、太阳季节加热与行星环流移动、青藏高原热力和动力作用均已覆盖。答题须突出形成因子和作用链，冬夏系统只作说明；东亚夏季并非各地统一西南风。']
source=root.parent/'动力气象课后习题/试题解答/往年试题解析/2005.md'
ids=re.findall(r'^## 题目 (.+)$',source.read_text(encoding='utf-8'),re.M)
assert len(ids)==len(notes)
review=dict(zip(ids,notes))
(root/'scripts/review_2005.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 for q,note in review.items():
  pattern=r'^(### '+re.escape(q)+r'[^\n]*)\n(?:\n\*\*本次复核提示（2026-11-01）：\*\* [^\n]*\n)?'
  s=re.sub(pattern,lambda m:m[1]+'\n\n**本次复核提示（2026-11-01）：** '+note+'\n',s,flags=re.M)
 p.write_text(s,encoding='utf-8')
p=root/'逐题复核记录.md';s=p.read_text(encoding='utf-8').replace('2004及2004_1年共196条记录','2004、2004_1及2005年共204条记录').replace('其中10题','其中11题').replace('其余340题','其余332题')
lines=[]
for line in s.splitlines():
 m=re.match(r'\| \[([^\]]+)\]',line)
 if m and m[1] in review:
  line=line.replace('结构核对完成；学科内容待复核','内容复核；教材图待核' if m[1]=='2005-四-整题' else '内容复核（2026-11-01）').replace('仅核对题号、题干/解答段落，未据此宣称答案正确。',review[m[1]].replace('|',r'\|'))
 lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Reviewed',len(review),'questions')
