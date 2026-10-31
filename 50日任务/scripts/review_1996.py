from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
notes=[
'原填空“几十到几百公里”不能覆盖全部中尺度。按常用中α、中β、中γ划分，总范围约2—2000 km；200—2000 km仅是中α。',
'填空可用凝结潜热与斜压有效位能，但解释须补充热带气旋从暖海获取焓，凝结不是能量的最终来源；四能量库收支内部转换项相消。',
r'有限层厚热成风平行层平均等温线；局地垂直切变才与该等压面等温线对应。静力式写为$\frac{\partial\Phi}{\partial\ln p}=-RT$，上下层下标t、b不表示偏导。',
'日期、脊线纬度为气候经验范围；“全长江流域进入伏旱”过于绝对，应理解为长江中下游在副高控制下较易出现伏旱，不能套用每个地区和每年。',
'西北太平洋是主要活跃洋盆；5—20°应注明北纬且为常见生成纬带，不能理解为所有台风活动轨迹都限于该纬带。',
'定义重点是低层局地风速极大。原解“题中的12 m/s”不适用本题（题干未给数值）；高度和阈值仅作具体研究的例子。',
'季节突变指环流从一季型向另一季型较迅速转换，需举急流或副高跃变、季风建立等指标；并非所有要素同步突变。',
'待核教材术语：原解第一段推导的是均匀西风背景下一维无辐散罗斯贝波的下游发展，不能据此作为“上游效应”的完整答案。保留群速解释作对照，本题定义仍须与课程指定教材核实。',
'阻塞的持续性、准静止和阻挡西风带三点齐全。相关雨雪、高温及寒潮只是随位置、季节与冷空气条件变化的可能影响。',
r'补充相对涡度是相对地球旋转坐标系速度场的旋度。三维定义为$\boldsymbol\zeta=\nabla\times\mathbf V$；局地直角坐标的垂直分量为$\zeta=\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}$，单位为$\mathrm{s^{-1}}$。',
r'原解只给水平散度，补全三维散度$\nabla\cdot\mathbf V=\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}$；水平散度仅取前两项。散度描述局地体积膨胀率，不可把水平辐合直接等同整柱上升。',
'平流贡献负号及压力坐标热力方程核对一致；Q为单位质量单位时间加热，稳定层结的上升动力冷却可抵消暖平流。',
'位温推导的积分上下限和指数符号正确；采用理想干空气、定比热与可逆干绝热过程，参考压力固定，温度单位K。',
'原解季节移动内容较多，结构作答应优先写：深厚暖性反气旋、中低层内部下沉及常见下沉逆温、周边风场与北侧/西北侧雨带；暖性不意味着所有高度中心垂直重合。',
'动力绕流、地形抬升、季节热源、季风转换及高原系统东移已覆盖四种以上影响；宜逐项列出机制与对应天气，避免把近地层低压和高空高压混淆。',
'待核分类编号：“第二类”依教材分类表确定。原解可作为一般寒潮演变复习，尚不能确认其就是题目指定的第二类；不以泛化过程替代专指答案。',
'补充常见流向分类的特点：纬向型槽脊振幅小、西风较平直；经向型槽脊振幅大、南北交换强，阻塞可较活跃；混合型各区域特征不同。原解“大气活动中心”段与设问关系弱；若课程采用指定总体分型体系，其名称及判据仍待教材核实。',
'高度差换算地转风的正负号、纬距和单位一致。500 hPa、35—55°N是本解选用约定，课程另有定义时须更换，指数循环不具有固定周期。',
r'原解缺少对流参数。浮力驱动、黏性与热扩散控制的Boussinesq层可引入$Ra=\frac{g\alpha_T\Delta T H^3}{\nu\kappa_T}$，其中$\alpha_T$为热膨胀系数、$\kappa_T$为热扩散率；临界值依边界条件，不直接套用真实湿对流。层结与切变还可用$Ri=\frac{N^2}{(\frac{\partial U}{\partial z})^2}$（单向基本流）。$Fr=\frac{U}{NH}$要求稳定层结的实数N。参考：[MIT对流课程讲义](https://ocw.mit.edu/courses/12-002-physics-and-chemistry-of-the-terrestrial-planets-fall-2008/b41969cc35965fff31b067af04b2010f_MIT12_002f08_lec14.pdf)。'
]
source=root.parent/'动力气象课后习题/试题解答/往年试题解析/1996.md'
ids=re.findall(r'^## 题目 (.+)$',source.read_text(encoding='utf-8'),re.M)
assert len(ids)==len(notes)
review=dict(zip(ids,notes))
(root/'scripts/review_1996.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 for q,note in review.items():
  pattern=r'^(### '+re.escape(q)+r'[^\n]*)\n(?:\n\*\*本次复核提示（2026-10-31）：\*\* [^\n]*\n)?'
  s=re.sub(pattern,lambda m:m[1]+'\n\n**本次复核提示（2026-10-31）：** '+note+'\n',s,flags=re.M)
 p.write_text(s,encoding='utf-8')
p=root/'逐题复核记录.md';s=p.read_text(encoding='utf-8')
s=s.replace('2026-10-30。','2026-10-31。',1).replace('1989、1990、1992、1994年共62题','1989、1990、1992、1994、1996年共81题（其中1996年3题仍有教材口径待核）').replace('其余474题','其余455题')
lines=[]
for line in s.splitlines():
 m=re.match(r'\| \[([^\]]+)\]',line)
 if m and m[1] in review:
  q=m[1]; status='内容复核；教材口径待核' if q in ['1996-二-3','1996-四-3','1996-四-4'] else '内容复核（2026-10-31）'
  line=line.replace('结构核对完成；学科内容待复核',status).replace('仅核对题号、题干/解答段落，未据此宣称答案正确。',review[q].replace('|',r'\|'))
 lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Reviewed',len(review),'questions')
