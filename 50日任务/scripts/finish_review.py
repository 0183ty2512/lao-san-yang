"""Apply verified wording, derivative typography and static study diagrams."""
from pathlib import Path
import re,subprocess,shutil,json
root=Path(__file__).resolve().parents[1]
assets=root.parent/'docs/assets';assets.mkdir(exist_ok=True)
base='https://0183ty2512.github.io/lao-san-yang/assets/'
graphs={
'energy-cycle':('能量循环：箭头规定正方向，转换可正可负','''rankdir=TB;
GZ[label="平均非绝热产生 GZ"]; GE[label="扰动非绝热产生 GE"];
AZ[label="平均有效位能 AZ"]; AE[label="扰动有效位能 AE"];
KZ[label="平均动能 KZ"]; KE[label="扰动动能 KE"];
DZ[label="摩擦耗散 DZ"]; DE[label="摩擦耗散 DE"];
{rank=same;GZ;GE} {rank=same;AZ;AE} {rank=same;KZ;KE} {rank=same;DZ;DE}
GZ->AZ; GE->AE; AZ->AE[label="CA：扰动热输送"];
AZ->KZ[label="CZ：平均环流压力功"]; AE->KE[label="CE：扰动压力功"];
KZ->KE[style=invis,weight=100]; KE->KZ[label="CK：动量输送与切变",constraint=false]; KZ->DZ; KE->DE;'''),
'wave-life':('典型不稳定斜压波的概念过程','''rankdir=TB;
A[label="斜压基本流与小扰动"];B[label="倾斜波增长\n向极热输送"];
C[label="成熟：振幅增大与波破碎"];D[label="衰减：温差减弱\n动量反馈基本流"];
E[label="波包能量向下游传播"];F[label="下游新扰动发展"];
A->B;B->C;C->D;B->E;E->F;'''),
'monsoon-systems':('东亚冬夏季环流联系示意','''rankdir=TB;
subgraph cluster_w {label="冬季东亚";WH[label="大陆西伯利亚冷高压"];WC[label="中国东部"];
WL[label="北太平洋阿留申低压"];WJ[label="高空西风急流与东亚槽"];
WH->WC[label="偏北冷干气流"];WC->WL;WJ->WC;}
subgraph cluster_s {label="夏季东亚";SL[label="大陆热低压与季风槽"];SC[label="中国季风雨带"];
SH[label="西太平洋副热带高压"];SW[label="印度洋及南海西南气流"];SA[label="高空南亚高压"];
SL->SC[dir=none];SH->SC[label="西侧偏南暖湿气流"];SW->SC;SA->SC[label="上层环流配合"];}
''')}
for key,(title,body) in graphs.items():
    dot='digraph G {graph[bgcolor="white",pad="0.25",nodesep="0.35",ranksep="0.6",fontname="Microsoft YaHei",fontsize=17,label="'+title+'",labelloc=t];node[shape=box,style="rounded,filled",fillcolor="#edf4fc",color="#6489b3",fontname="Microsoft YaHei",fontsize=15,margin="0.15,0.12"];edge[color="#456b94",fontname="Microsoft YaHei",fontsize=12];'+body+'}'
    subprocess.run(['dot','-Tsvg','-o',str(assets/(key+'.svg'))],input=dot,encoding='utf-8',check=True)
shutil.copyfile(root.parent/'动力气象课后习题/试题解答/往年试题解析/图解/罗斯贝波生命史.png',assets/'rossby-wave-life.png')
math_pattern=r'\$\$[\s\S]*?\$\$|(?<!\\)\$(?!\$)[^$]+?(?<!\\)\$'
count=0
def normalize(m):
    global count
    s=m[0]
    # Explicit coordinate operators, including indexed Cartesian coordinates.
    def op(a):
        coord=a[1] or a[2]
        coords={'i':'x_i','j':'x_j','lambda':r'\lambda','varphi':r'\varphi'}
        if coord in ('pp','xx','yy','zz','tt'):
            return r'\frac{\partial^2}{\partial '+coord[0]+'^2}'
        return r'\frac{\partial}{\partial '+coords.get(coord,coord)+'}'
    s=re.sub(r'\\partial_(?:\{([^}]+)\}|(lambda|varphi|[xyztpij]))',op,s)
    # Whitelist fields with derivative subscripts. Layer/component labels stay intact.
    atom=r'(?:\\(?:bar|overline)\s*(?:\{[^{}]+\}|\\[A-Za-z]+|[A-Za-z])|\\(?:Phi|psi|chi|zeta|omega|eta|alpha|phi|pi)|(?<![A-Za-z\\])[uvwhbUTpHABW])'
    pat='('+atom+r"\x27?)_(?:\{([xyztp]{1,2})\}|([xyztp]))"
    # TeX unbraced subscripts contain ONE token: alpha_yp_x is alpha_y times p_x.
    s=s.replace(r'\frac{\partial^2 \alpha}{\partial y\partial p}_x',r'\frac{\partial\alpha}{\partial y}\frac{\partial p}{\partial x}')
    s=s.replace(r'\frac{\partial^2 \alpha}{\partial x\partial p}_y',r'\frac{\partial\alpha}{\partial x}\frac{\partial p}{\partial y}')
    def field(a):
        f=a[1];c=a[2] or a[3]
        # t labels in pressure/temperature and upper/lower-layer geostrophic winds.
        if c=='t' and ((f=='p' and 'Dp/Dt' not in s) or f=='T' or (f in ('u','v') and f+'_t-'+f+'_b' in s)):
            return a[0]
        if f in ('A','B') and c!='p':return a[0]
        if f=='W' and c!='zz':return a[0]
        if f=='H' and c!='y':return a[0]
        den=(r'\partial '+c if len(c)==1 else r'\partial '+c[0]+'^2' if c[0]==c[1] else r'\partial '+c[0]+r'\partial '+c[1])
        return r'\frac{\partial'+('^2' if len(c)==2 else '')+' '+f+'}{'+den+'}'
    s=re.sub(pat,field,s)
    # TeX products need no whitespace: Hu_x, K_mu_{zz}, fT_y, up_x.
    # Consume whole commands first so the tail of a command is never a field.
    s=re.sub(r'\\[A-Za-z]+|([uvwhbUTpHABW])_(?:\{([xyztp]{1,2})\}|([xyztp]))',lambda a:field(a) if a[1] else a[0],s)
    for product,coord in [('hu','x'),('hv','y')]:
        s=s.replace('('+product+')_'+coord,r'\frac{\partial ('+product+r')}{\partial '+coord+'}')
    s=re.sub(r'\\(bar|overline)\s*\\frac\{\\partial (u|v|U)\}\{\\partial ([xyz])\}',lambda a:r'\frac{\partial'+'\\'+a[1]+'{'+a[2]+'}}{'+r'\partial '+a[3]+'}',s)
    s=s.replace(r'\mathbf n,dS',r'\mathbf n\,dS')
    if s!=m[0]:count+=1
    return s
for p in (root/'每日内容').glob('D*.md'):
    s=p.read_text(encoding='utf-8')
    s=s.replace('锋面上升指向冷空气一侧','锋面随高度向冷空气一侧倾斜')
    s=s.replace('双向箭头表示转换可正可负，方向由收支项决定','图中箭头规定转换的正方向，转换量可正可负')
    s=s.replace('题中 70—80 m/s 是典型量级而非上限','70—80 m/s 可作为示例量级而非上限')
    s=s.replace('题中的 12 m/s 或 12—15 m/s 属常用识别量级','12 m/s 或 12—15 m/s 属部分资料的经验识别量级')
    s=s.replace('$f$平面舍弃纬向变化',' $f$平面舍弃随纬度的变化').replace('β平面保留一阶纬向变化','β平面保留一阶经向变化')
    # Give each removed duplicate a direct link to its question's full source.
    parts=re.split(r'(?=^### \d{4})',s,flags=re.M)
    sources={}
    for b in parts:
        q=re.match(r'### (\d{4}(?:_1)?-[^\n·]+)',b)
        src=re.search(r'\[解析来源（对应题目行）\]\(([^)]+)\)',b)
        if q and src:sources[q[1].strip()]=src[1]
    for i,b in enumerate(parts):
        src=re.search(r'\[解析来源（对应题目行）\]\(([^)]+)\)',b)
        q=re.match(r'### (\d{4}(?:_1)?-[^\n·]+)',b)
        url=src[1] if src else sources.get(q[1].strip()) if q else None
        if url:b=b.replace('本段与上文相同，可回看前面的解析，不再重复展开。','本段与前文重复，已合并；[查看本题完整解析]('+url+')。')
        parts[i]=b
    s=''.join(parts)
    def diagram(m):
        code=m[1]
        key='energy-cycle' if 'GZ[' in code else 'monsoon-systems' if 'subgraph WI' in code else 'wave-life'
        return '!['+graphs[key][0]+']('+base+key+'.svg)'+ ('\n\n![典型斜压波水平与垂直结构]('+base+'rossby-wave-life.png)' if key=='wave-life' else '')
    s=re.sub(r'```mermaid\n(.*?)```',diagram,s,flags=re.S)
    s=re.sub(math_pattern,normalize,s)
    p.write_text(s,encoding='utf-8')
print('Normalized math expressions:',count)
