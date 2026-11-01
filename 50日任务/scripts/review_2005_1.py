from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
notes=['正压密度函数、斜压梯度叉积及热成风联系正确；湿空气要用虚温。必须区分热力结构是否斜压与扰动是否斜压不稳定，前者不是后者充分条件。', '先给三维定义：相对涡度$\\boldsymbol\\zeta=\\nabla\\times\\mathbf V$，散度$\\nabla\\cdot\\mathbf V$；原解分别只列涡度垂直分量和水平散度，需加限定。三维散度另有$\\frac{\\partial w}{\\partial z}$，单位均为s⁻¹，绝对涡度还含地球旋转。', '频散关系、相速及两群速分量与常数U的正压无辐散β平面模型一致。一维波长公式取l=0，二维不能仅按纬向波长判断静止条件；地面相速可东可西，内禀纬向相速向西不代表能量必向西。', '有效位能是相对绝热重排最低参考态的可用全位能，定义正确。四库内部转换相消，符号约定明确；图示箭头不能解释成每种转换始终单向或所有加热始终增加有效位能。', '赤道模态列举、Kelvin高斯束缚和混合波分支正确；均属线性浅水或竖直模态等效模型，H为等效深度。赤道Kelvin在静止背景内禀东传，不能把沿岸Kelvin的实体边界条件移到赤道。', '地转风两分量符号、静力微分及热成风积分方向一致；温度按层平均且压力比同单位。热成风是地转风差，不是独立实际气流；实际强摩擦或强加速度运动可偏离该平衡。', '浅水模式前两步推导正确，但必须补柱状水平速度、固定表面压力与底面无穿透。后续位涡证明可作延伸；与本题无关且混用常f和β的第五步线性化已从本题副本移除。', '位涡守恒证明正确：先得绝对涡度随流变化，再与层厚连续式用商法则组合。h须正、无摩擦且无质量源汇；无需做小扰动线性化。原第五步近似不一致，已从本题副本移除。', '基本态不稳定定义及能量来源分类合理。平行纬向流的惯性条件为$f(f-\\frac{\\partial U}{\\partial y})<0$；Rayleigh–Kuo变号只是规定无黏正压通道模型的必要条件，并非充分条件。对称不稳定的fq判据需静力、惯性稳定及沿锋不变等假设；云带形态本身不能唯一证明机制。']
source=root.parent/'动力气象课后习题/试题解答/往年试题解析/2005_1.md'
ids=re.findall(r'^## 题目 (.+)$',source.read_text(encoding='utf-8'),re.M)
assert len(ids)==len(notes)
review=dict(zip(ids,notes))
(root/'scripts/review_2005_1.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 for q,note in review.items():
  pattern=r'^(### '+re.escape(q)+r'[^\n]*)\n(?:\n\*\*本次复核提示（2026-11-01）：\*\* [^\n]*\n)?'
  s=re.sub(pattern,lambda m:m[1]+'\n\n**本次复核提示（2026-11-01）：** '+note+'\n',s,flags=re.M)
 p.write_text(s,encoding='utf-8')
p=root/'逐题复核记录.md';s=p.read_text(encoding='utf-8').replace('2004_1及2005年共204条记录','2004_1、2005及2005_1年共213条记录').replace('其余332题','其余323题')
lines=[]
for line in s.splitlines():
 m=re.match(r'\| \[([^\]]+)\]',line)
 if m and m[1] in review:
  line=line.replace('结构核对完成；学科内容待复核','内容复核（2026-11-01）').replace('仅核对题号、题干/解答段落，未据此宣称答案正确。',review[m[1]].replace('|',r'\|'))
 lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Reviewed',len(review),'questions')
