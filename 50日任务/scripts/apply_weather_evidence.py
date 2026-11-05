"""Apply weather evidence to the specific question blocks, not original transcripts."""
from pathlib import Path
from urllib.parse import quote
import json,re

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'scripts/review_weather_evidence.json').read_text(encoding='utf-8'))
evidence=root/'复核依据/天气课件复核.md'
text=(root/'scripts/weather_evidence.md').read_text(encoding='utf-8')
text=text.replace('# 2026-11-03 天气学疑点核对依据','# 2026-11-04 天气学疑点核对依据')
text=re.sub(r'^## (W\d+) (.+)$',r'## \1\n\n**\2**',text,flags=re.M)
evidence.parent.mkdir(exist_ok=True)
evidence.write_text(text,encoding='utf-8')
url='https://github.com/0183ty2512/lao-san-yang/blob/main/'+quote('50日任务/复核依据/天气课件复核.md')
for q,e in data.items():
    link=url+'#'+e['evidence']['section'].lower()
    e['note']=re.sub(r'\[课件页码与核对依据\]\([^)]+\)',f'[课件页码与核对依据]({link})',e['note'])
    e['status']=e['status'].replace('2026-11-03','2026-11-04')
    e['evidence']['url']=link

answers={
'2020-二-3':'''此处按本地教材“锋前暖区暴雨”的触发机制回答三类：

1. **边界层浅薄冷空气侵入。** 浅冷空气前沿形成低层辐合和抬升，使暖湿气块达到可释放不稳定能量的高度。
2. **地形作用。** 山坡强迫抬升及地形辐合（如喇叭口地形）可集中上升运动，触发对流。
3. **海陆分布作用。** 海陆摩擦差异造成的低层辐合可触发上升；具体过程还可能受海陆风及日变化影响。

适用前提是暖区已有潮湿、不稳定的背景，且水汽供应和系统持续性有利。这里不能将“三类”换成锋面、低涡/切变线、暖区三个并列天气系统。''',
'2005-四-整题':'''**双阻配置。** 500 hPa中高纬西阻高位于乌拉尔山附近，东阻高位于雅库茨克附近，两者之间为宽广低槽；其南侧约35°—40°N常有较平直强西风带，冷空气可经巴尔喀什湖、贝加尔湖一带南下。这是典型概念配置，不是每场过程必须满足的精确经纬度。

**中低纬与低层配合。** 西太副高呈带状伸向华南，教材典型图在120°E附近的脊线约22°N；其北侧西南暖湿气流与北来的气流在江淮附近交汇。850—700 hPa的江淮切变线南侧有西南低空急流，持续输送水汽。

**高层与地面。** 江淮上空南亚高压及有利高层辐散与低层辐合配合；地面梅雨锋较长时间停滞。切变线上低涡或锋面波动反复东移，可造成多轮暴雨。双阻维持冷空气活动背景，不能仅列一般梅雨定义代替双阻的位置与高低空配置。''',
'2002-五-整题':'''影响我国的主要寒潮路径包括：

1. **西北路（中路）：** 从关键区经蒙古高原到河套，再向长江中下游和江南推进，常影响中东部大范围地区。
2. **西路：** 经新疆、青海及青藏高原东侧一带南下，偏重西北及西南等地区的影响。
3. **东路：** 经蒙古高原、华北北部后主力东移，部分冷空气在低层回流南下，东部地区影响突出。
4. 另外可出现东、西路冷空气汇合的过程。

**本题“影响最严重”的教材作答：通常为西北路（中路）。** 本地课件指出河套至较低纬地区路径短、地势北高南低，有利冷空气迅速南下，往往造成最强寒潮。这是常见强度倾向，某次具体灾害损失仍随冷空气强度、水汽、影响范围及暴露条件而变化。''',
'1999-一-1':'''按本地教学资料与题干较宽的东部洪涝口径，保留填空：**长江流域（长江中下游）；1954；1991**。

课件将1954、1991、1998等列作长江流域暴雨洪水例子，同时另举1991年江淮暴雨。因此1991并非无依据的年份，但各次灾区和全流域同步程度不同，不能把1991江淮突出灾情与1954、1998的大洪水范围完全等同。此处确认教学举例的依据，不声称已取得原卷官方评分表。''',
'2021-三-3':'''寒潮是强冷空气大范围南侵，造成显著降温、大风及可能雨雪、冻害的天气过程。共同主线是冷空气酝酿蓄积、槽脊调整、冷高压及冷锋南下；不同过程的冷空气组织方式、南下路径、持续时间和水汽配置不同，雨雪并非每次都同样显著。

**“关键系统有哪几类”仍须原课程上下文确定。** 本地课件存在三个不同层次：

| 讨论对象 | 应关注的系统或类型 |
|---|---|
| 倒Ω型中期过程预报 | 北大西洋、北太平洋的异常暖脊及随后亚洲槽脊调整 |
| 乌拉尔山高压脊的发展 | 补充型、叠加型、结合型 |
| 短中期斜压扰动过程 | 横槽型、小槽发展型、低槽东移型 |

以上分类对象不同，不能合并成同一套编号答案。业务监测还需同时看极涡/冷槽、地面冷高压及冷锋；这只是物理预报框架，不能冒充已确认的原题专指分类。''',
'1996-四-3':'''**“第二类”尚不能唯一对应。** 本地课件存在实质性的编号差别：一套短中期分类的第二项为小槽发展型，另一套为低槽东移型；中期过程分类的第二项又是极涡偏心型。需要原课程的分类表才能确定本题所指。

复习时可以分开理解：小槽发展型关注冷槽中短波扰动发展及槽后冷空气南下；低槽东移型关注较深冷槽东移、槽后偏北气流引导冷空气；极涡偏心型关注极涡偏离极地、冷空气中心及其南下通道的调整。它们不能因编号相同就视为同一种过程。

未找回对应分类表前，保留此题待核，不能把一般寒潮的“蓄积—爆发—南下”过程当作已完成专指答案。''',
'1998-三-3':'''**若采用本地西风波状流型课件的分类，**主要按高空气流相对纬圈的走向及槽脊经向振幅，分为两种基本型：

- **纬向型：** 西风较平直，槽脊经向振幅小，南北交换较弱。
- **经向型：** 南北向气流明显，槽脊振幅大，可伴大型闭合暖高压和冷低压，南北交换较强。

不同区域可同时出现两类状态，并随时间互相转换。“混合/过渡”可以描述这种状态，但该课件未将它列为第三个同等基本类型。原题若另指某一北半球总体分型体系，其名称与判据仍待原表确认。''',
'1996-四-4':'''**若采用本地西风波状流型课件的分类，**按高空气流相对纬圈的走向及槽脊经向振幅，分纬向型与经向型：纬向型西风较平直、槽脊振幅小、南北交换较弱；经向型南北气流明显、槽脊振幅大，并可伴大型闭合暖高压和冷低压。

两型可在不同区域并存，也会随时间互相转换；“混合/过渡”可描述这种状态，但该来源没有将其列为第三个基本型。原题“北半球总体分型”可能指其他指定体系，目前缺少对应名称和原分类表，保留待核。一般“大气活动中心”的定义不能代替本题的分类原则。''',
'2026-二-1':'''**固定“五个共同特征”表仍待核，以下只是雹增长机制的复习归纳。** 已查本地课件支持：冰雹来自旺盛积雨云；较强上升气流帮助雹胚在云中停留；过冷水为凇附增长提供水源；液水含量与温度影响干、湿增长；粒子轨迹和停留时间共同影响最终雹粒大小。

不能把上述五个解释点直接宣布为原教材的固定五条。强雷电、阵风等可伴随强对流，但不是每个雹云都必须满足的定义条件；垂直风切变有助于组织和维持，也不能替代浮力、水汽及粒子增长条件。'''
}
blocking='''**指定三个冬季高频地区的填空仍待核。** 原资料记录为乌拉尔山地区、鄂霍次克海地区和北大西洋东部（欧洲西海岸），目前尚缺与其冬季、纬带、阻塞判据及样本期匹配的频率图，不能标为已经证实的唯一列表。

可确定的一般物理概念是：阻塞高压为中高纬持续、少动并使西风绕行的强脊或闭合高压；形成和维持与暖输送、波破碎及涡旋反馈等有关。一般机制不能验证某个空间统计排序，也不能仅据夏季阻高常见便反推该地区冬季从不高发。'''
for q in ['2000-一-2','1998-一-3','1992-一-1']:answers[q]=blocking
assert set(answers)==set(data)

# Canonical question and original-source links remain visible in every day's first occurrence.
canonical={}
for p in sorted((root/'每日内容').glob('D*.md')):
    text=p.read_text(encoding='utf-8')
    for q in data:
        m=re.search(r'^### '+re.escape(q)+r' ·[^\n]*\n([\s\S]*?)(?=^#{1,3} |\Z)',text,re.M)
        if m and q not in canonical:
            body=re.sub(r'^\*\*本次复核提示（[^\n]*\n','',m[1],flags=re.M).lstrip()
            body=re.sub(r'^<a id="reviewed-[^"]+"></a>\s*','',body).lstrip()
            body=body.removeprefix('**原资料填空记载（待核）：** ')
            source=re.search(r'^\[解析来源[^\n]+',body,re.M)
            if source:canonical[q]=(body.split('\n\n')[0],source[0])
assert set(canonical)==set(data)
counts={q:0 for q in data};changed=[]
for p in (root/'每日内容').glob('D*.md'):
    old=p.read_text(encoding='utf-8');text=old
    for q,e in data.items():
        pattern=r'^(### '+re.escape(q)+r' ·[^\n]*)\n([\s\S]*?)(?=^#{1,3} |\Z)'
        def update(m):
            counts[q]+=1
            first,source=canonical[q]
            # Use an explicit anchor for the repeated selected-answer block in the same day.
            if q in ['2000-一-2','1998-一-3','1992-一-1']:
                first='**原资料填空记载（待核）：** '+first
            if '完整解答' in m[1] and ('id="reviewed-'+q+'"') in text[:m.start()]:
                return m[1]+'\n\n**本次复核提示（2026-11-04）：** '+e['note']+'\n\n本题解析已合并至[本页前文复核版](#reviewed-'+q+')，原始来源仍可通过前文链接核对。\n\n'
            return m[1]+'\n\n<a id="reviewed-'+q+'"></a>\n\n**本次复核提示（2026-11-04）：** '+e['note']+'\n\n'+first+'\n\n'+source+'\n\n**复核后解析：**\n\n'+answers[q]+'\n\n'
        text=re.sub(pattern,update,text,flags=re.M)
    if text!=old:p.write_text(text,encoding='utf-8');changed.append(p.name)

# A second pass contracts same-day repeats after both matches have been written.
for name in changed:
    p=root/'每日内容'/name;text=p.read_text(encoding='utf-8')
    for q,e in data.items():
        pattern=r'^(### '+re.escape(q)+r' · 完整解答[^\n]*)\n([\s\S]*?)(?=^#{1,3} |\Z)'
        def compact(m):
            if 'id="reviewed-'+q+'"' not in text[:m.start()]:return m[0]
            return m[1]+'\n\n**本次复核提示（2026-11-04）：** '+e['note']+'\n\n本题解析已合并至[本页前文复核版](#reviewed-'+q+')，原始来源仍可通过前文链接核对。\n\n'
        text=re.sub(pattern,compact,text,flags=re.M)
    p.write_text(text,encoding='utf-8')

p=root/'逐题复核记录.md';lines=p.read_text(encoding='utf-8').splitlines()
ledger_count=0
for i,line in enumerate(lines):
    m=re.match(r'\| \[([^]]+)\]',line)
    if m and m[1] in data:
        e=data[m[1]]
        lines[i]=line.split(' | ')[0]+' | '+e['status']+' | '+e['note'].replace('|',r'\|')+' |'
        ledger_count+=1
assert ledger_count==12
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
for q,e in data.items():e['answer']=answers[q]
(root/'scripts/review_weather_applied.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'questions':len(data),'occurrences':counts,'files':changed,'ledger_rows':ledger_count},ensure_ascii=False))
