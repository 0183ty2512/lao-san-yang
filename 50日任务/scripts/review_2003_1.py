from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
notes=['正压与斜压的密度—压力定义正确；湿空气应以虚温代替干空气温度讨论密度。地转风无垂直切变结论依赖静力、地转与相同水平位置，不能推广到任意实际风。', '地转风分量、热成风积分方向正确；上层减下层的约定必须保留。有限层厚热成风对应对数气压平均温度梯度，北半球冷侧在左，不能把层平均与单层温度混用。', '正压无辐散β平面、常数U下的频散关系及两个群速分量经对k、l求导核对一致。$c_x=\\omega/k$要求$k\\ne0$；一维波长公式仅适用于l=0。相对基本流向西是相速结论，不能自动用于群速方向；频散不是耗散。', '有效位能定义、静力柱内能加重力位能的积分和四库转换符号一致。积分等式还要求底面高度零、顶端边界项消失；加热是否产生有效位能依其空间分布，不是任何加热都增加有效位能。', '位温定义、压力比与积分符号正确；R和cp按干空气一致取值，参考压力固定，温度用K。绝热守恒指随气块导数，不代表固定地点位温恒定。', 'CISK是对流潜热加热与大尺度低层辐合相互促进的理想化机制；先给定义与反馈，再列台风初始扰动，不能与单气块条件不稳定或海气通量反馈混称。', '开尔文波高斯衰减和东传选择经代回经向平衡核对正确；使用静止基本态、线性赤道β平面浅水模型。混合波所列为正频率分支，其共轭支用于构造实场；负k时西向相速、东向群速不矛盾。此处H为等效深度，不能直接取真实对流层几何厚度。', 'Ertel位涡推导中膨胀项、速度梯度两项相消及斜压三重积为零均成立；最后一步要求定组成状态关系使位温为p、ρ的函数。名词解释应先写$q=\\frac{\\boldsymbol\\omega_a\\cdot\\nabla\\theta}{\\rho}$与绝热无摩擦守恒，不能只展示证明而漏定义；湿过程或组分变化需另处理。', '已按“地面对空气的应力”核对符号：$\\mathbf M=-\\frac{\\mathbf k\\times\\boldsymbol\\tau_s}{\\rho f}$，$w_E=-\\frac{\\operatorname{curl}_z\\boldsymbol\\tau_s}{\\rho f}$。需常数ρ、f、层顶应力消失及底部w=0；采用反向应力定义时符号反转。原解Ri和Re介绍与抽吸定义关系弱，可略。', '计算核对：柱厚由10 km变5 km，绝对涡度变为初始一半，$\\zeta_{a2}=6.3152\\times10^{-5}\\ \\mathrm{s^{-1}}$；减去30°N的f后$\\zeta_2=-9.7695\\times10^{-6}\\ \\mathrm{s^{-1}}$。相对涡度为反气旋性，绝对涡度仍正；该结果依赖均匀浅水气柱与固定顶界。', '周期通量抵消证明正确，但必须要求速度及压力势通量在成对边界周期一致；只说速度周期不够。均匀密度、恒定厚度时面积动能乘常数即总动能。原题所称方程组未完整展示，此解明确采用给定的无辐散水平动量模型，不声称覆盖未知模型。', '浅水模式应止于两条水平动量方程及层厚连续方程，并说明静力、均匀密度、柱状水平速度、固定表面压力和底部无穿透。原第五步常f动量式与保留β涡度式混用，且不属于本题要求，已从本题学习副本删除，避免当成同一模型的严格推导。', '位涡证明的旋度交叉项、行星涡度随流变化及商法则相消正确；要求h大于零、无摩擦与质量源汇。证明不需要线性化。原第五步基本流线性化混用常f和β近似，已从本题学习副本删除。']
source=root.parent/'动力气象课后习题/试题解答/往年试题解析/2003_1.md'
ids=re.findall(r'^## 题目 (.+)$',source.read_text(encoding='utf-8'),re.M)
assert len(ids)==len(notes)
review=dict(zip(ids,notes))
(root/'scripts/review_2003_1.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 for q,note in review.items():
  pattern=r'^(### '+re.escape(q)+r'[^\n]*)\n(?:\n\*\*本次复核提示（2026-11-01）：\*\* [^\n]*\n)?'
  s=re.sub(pattern,lambda m:m[1]+'\n\n**本次复核提示（2026-11-01）：** '+note+'\n',s,flags=re.M)
 p.write_text(s,encoding='utf-8')
p=root/'逐题复核记录.md';s=p.read_text(encoding='utf-8').replace('2002、2003年共165条记录','2002、2003及2003_1年共178条记录').replace('其余371题','其余358题')
lines=[]
for line in s.splitlines():
 m=re.match(r'\| \[([^\]]+)\]',line)
 if m and m[1] in review:
  line=line.replace('结构核对完成；学科内容待复核','内容复核（2026-11-01）').replace('仅核对题号、题干/解答段落，未据此宣称答案正确。',review[m[1]].replace('|',r'\|'))
 lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Reviewed',len(review),'questions')
