from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
notes=['本题问对流性天气，列雷暴、飑线及冰雹/龙卷相关天气可解释，但冰雹是降水现象、龙卷本体尺度通常小于中尺度系统；不能把所有填空都当同一尺度的系统分类。', '散度数量级可作典型估计。原解$\\frac{\\partial w}{\\partial z}=-D$仅适用于不可压缩近似；可压缩大气须考虑密度变化，静力压力坐标可用$\\frac{\\partial\\omega}{\\partial p}=-D$。不能将两式不加条件地互换。', '100、300 hPa分别是热带与极地对流层顶的代表性气压量级；标题“高度”实际用气压坐标表示，不是几何高度数值，随季节地点变化。', '原填空把江淮整个区域配到单一时段、脊线纬度，精度有限。20—25°N常用于长江中下游梅雨初期经验，雨带向江淮/淮河推进可对应更北脊线；应结合月份、雨带及西伸位置，不能机械套用。', '缺题核验：原始题干缺失，无法进行答案正确性复核。本条只保留缺题占位，不给星级、标准答案或虚构解析，须取得原卷后再补。', '叉积方向及地转风分量正确；梯度应明确在等压面上，f带半球符号，f趋零时不适用。地转平衡还要求摩擦和水平加速度可忽略。', '位温公式正确：压力比无量纲、温度用K、干空气气体常数与比热采用一致约定；位温是参照压力下的温度，不是气块当前实际温度。', '题干右侧仅为水平散度，应把左侧写成$D=\\nabla_h\\cdot\\mathbf V_h$；若V表示三维速度，完整散度还需加$\\frac{\\partial w}{\\partial z}$，不能漏掉后仍称三维散度。', '公式是局地直角坐标的垂直相对涡度分量，单位s⁻¹；三维涡度为旋度矢量，绝对垂直涡度还须加f。题干符号不要与完整三维量混称。', '题干右侧是水平温度平流，左侧V与梯度也应限定水平；三维高度坐标温度平流另含垂直平流。局地增温还含绝热压缩膨胀与非绝热加热。', '重点是Hadley南北向和Walker东西向热带垂直环流，低层辐合上升与高层外流、下沉支形成闭合；费雷尔和极地环流只作背景，不是热带主答内容。', '题目限定高空环流，应先写中高纬阻塞/槽脊与西太副高的相对配置，再写上对流层南亚高压、西风急流对上升区的配合。850—700 hPa急流可补充完整配置，但不能替代高空部分；“有急流”不自动意味着任意位置辐散。', '待核教材预期答案：西路、西北路、东路已给出，但原解未确定设问要求的“最严重”类型；部分课程还单列多路汇合型。需按教材路径分类及影响区域解释，不能在无条件下给出永远最严重的一路。']
source=root.parent/'动力气象课后习题/试题解答/往年试题解析/2002.md'
ids=re.findall(r'^## 题目 (.+)$',source.read_text(encoding='utf-8'),re.M)
assert len(ids)==len(notes)
review=dict(zip(ids,notes))
(root/'scripts/review_2002.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf-8')
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 for q,note in review.items():
  pattern=r'^(### '+re.escape(q)+r'[^\n]*)\n(?:\n\*\*本次复核提示（2026-10-31）：\*\* [^\n]*\n)?'
  s=re.sub(pattern,lambda m:m[1]+'\n\n**本次复核提示（2026-10-31）：** '+note+'\n',s,flags=re.M)
 p.write_text(s,encoding='utf-8')
p=root/'逐题复核记录.md';s=p.read_text(encoding='utf-8').replace('2000、2001年共143题','2000、2001、2002年共156条记录').replace('其中7题仍有原卷或教材口径待核','其中8题仍有原卷或教材口径待核、1条缺题无法审核答案').replace('其余393题','其余380题')
lines=[]
for line in s.splitlines():
 m=re.match(r'\| \[([^\]]+)\]',line)
 if m and m[1] in review:
  line=line.replace('结构核对完成；学科内容待复核','缺题：无法审核答案' if m[1]=='2002-一-5' else '内容复核；教材口径待核' if m[1]=='2002-五-整题' else '内容复核（2026-10-31）').replace('仅核对题号、题干/解答段落，未据此宣称答案正确。',review[m[1]].replace('|',r'\|'))
 lines.append(line)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Reviewed',len(review),'questions')
