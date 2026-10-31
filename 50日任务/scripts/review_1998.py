from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
notes=['原填空是强事件量级，不是寒潮、台风的普遍中心气压；1060—1080 hPa尤其不能理解为常态。高海拔地区海平面订正气压与实际站压须区分。', '原记录两套单位不等价。静力条件下$\\omega=\\frac{\\partial p}{\\partial t}+\\mathbf V_h\\cdot\\nabla_zp-\\rho gw$；仅当前两项可忽略时用$\\omega\\simeq-\\rho gw$。取密度1 kg/m³，1—10 cm/s约对应3.5—35 hPa/h，1—10 m/s约对应353—3530 hPa/h；上升对应负值。不能把几十hPa/h与1—10 m/s直接等同。', '待核教材口径：原填空给出的三处位置不能据此认定为冬季阻塞频率的严格前三名；鄂霍次克海阻高有明显季节性。原解主要讲阻塞机制，未提供冬季分布统计依据，保留此疑点。', '涡度、水平散度及垂直积分公式符号正确，水平导数须在同一等压面取值。补充地面边界$\\omega_s=\\frac{\\partial p_s}{\\partial t}+u_s\\frac{\\partial p_s}{\\partial x}+v_s\\frac{\\partial p_s}{\\partial y}$，一般不等于零。质量薄层为$(p_{底}-p_{顶})/g>0$；原文$-dp/g$仅适用于向上积分时dp为负的取向。', 'Hadley是热带平均南北向垂直环流，Walker是热带东西向垂直环流；太平洋西升东沉是典型背景态，会随ENSO变化。费雷尔与极地环流不是本题必答项。', '应直接列假定：远离赤道、摩擦可忽略、局地及平流加速度均远小于科氏项，水平气压梯度力与科氏力平衡。$Ro=\\frac{U}{|f|L}\\ll1$及$\\frac{1}{|f|T}\\ll1$分别约束两类加速度；不能仅说“无摩擦”便推出地转风。', '西南涡与高原涡须区分。西南涡主要位于高原东侧及四川盆地附近低层，常用700 hPa识别，是中尺度低压涡旋；原解“小尺度”应理解为相对天气尺度较小，不宜误当微尺度。作答补充地形、低层切变/辐合与湿过程共同影响，发展东移时可带来下游暴雨。', '活动应同时答季节北跳南撤、短期西伸东退以及强度和持续时间变化；雨带多在副高边缘水汽输送与冷空气交汇处，内部持续控制易高温少雨。日期和纬度范围仅为经验，不是逐年的固定对应表。', '压力坐标局地温度方程各项符号正确；需区分局地变化$\\frac{\\partial T}{\\partial t}$与随气块变化$\\frac{DT}{Dt}$。自由大气仍有辐射、凝结等非绝热加热，Q的量纲为单位质量单位时间加热率。', '待核教材分型体系：按中高纬槽脊数目、位置、振幅和优势流向，可概括纬向型、经向型及混合型；若试卷要求某一特定半球总体分型，须依指定教材名称与判据。原解大气活动中心定义与本题无直接关系，不能充当分型依据。', '按理想锋面气旋答初生、发展、成熟/锢囚、衰亡。冷锋追近暖锋时地面暖区逐渐收窄，不能背成发展期暖区必扩大。区域需区分生成与移动：蒙古及东北、江淮、东部近海为常见生成或发展区，蒙古并非我国境内全部地区；冷反气旋入侵路线不是本题所问。', '原解暖海焓供给、湿度、弱垂直切变、初始涡旋与适宜旋转环境覆盖主要有利条件。它们不是各自独立的充分条件；26.5℃为经验参考。CISK和能量来源可作解释，不必把整段生命周期知识替代条件清单。']
source=root.parent/'动力气象课后习题/试题解答/往年试题解析/1998.md'
ids=re.findall(r'^## 题目 (.+)$',source.read_text(encoding='utf-8'),re.M)
assert len(ids)==len(notes)
review=dict(zip(ids,notes))
(root/'scripts/review_1998.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 for q,note in review.items():
  pattern=r'^(### '+re.escape(q)+r'[^\n]*)\n(?:\n\*\*本次复核提示（2026-10-31）：\*\* [^\n]*\n)?'
  s=re.sub(pattern,lambda m:m[1]+'\n\n**本次复核提示（2026-10-31）：** '+note+'\n',s,flags=re.M)
 p.write_text(s,encoding='utf-8')
p=root/'逐题复核记录.md';s=p.read_text(encoding='utf-8').replace('1996、1997年共95题','1996、1997、1998年共107题').replace('其中1996年3题仍有教材口径待核','其中1996年3题及1998年2题仍有教材口径待核').replace('其余441题','其余429题')
lines=[]
for line in s.splitlines():
 m=re.match(r'\| \[([^\]]+)\]',line)
 if m and m[1] in review:
  line=line.replace('结构核对完成；学科内容待复核','内容复核；教材口径待核' if m[1] in ['1998-一-3','1998-三-3'] else '内容复核（2026-10-31）').replace('仅核对题号、题干/解答段落，未据此宣称答案正确。',review[m[1]].replace('|',r'\|'))
 lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Reviewed',len(review),'questions')
