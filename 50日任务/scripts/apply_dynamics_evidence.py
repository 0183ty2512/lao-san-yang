from pathlib import Path
from urllib.parse import quote
import re,json
root=Path(__file__).resolve().parents[1]
target=root/'复核依据/动力课件复核.md'
doc=(root/'scripts/dynamics_evidence.md').read_text(encoding='utf-8').replace('（2026-11-03）','（2026-11-04）')
doc=re.sub(r'^## (DYN\d+) (.+)$',r'## \1\n\n**\2**',doc,flags=re.M)
doc=doc.replace('第 64 页明确讨论 λ=0 和 N=0 两个条件。','第 64 页明确讨论 λ=0 和 N=0 两个条件。课件将 λ=0 称为“水平无辐散”的措辞不能直接由这个改写后的连续式推出；该式本身仅约束竖直速度不随高度变化，以下按方程而非简称解释。')
target.write_text(doc,encoding='utf-8')
base='https://github.com/0183ty2512/lao-san-yang/blob/main/'+quote('50日任务/复核依据/动力课件复核.md')
notes={}
def add(ids,key,note,resolved=False):
 for q in ids.split():notes[q]={'note':note+f' [课件页码与核对依据]({base}#{key.lower()})','status':'内容复核（2026-11-04；课件口径已核）' if resolved else '内容复核；原卷/教材待核'}
add('2026-三-3','DYN01','课件第63—64页已确认连续式中的λ及两条件λ=0、N=0，热力式速度应为w。λ=0直接得到∂w/∂z=0；结合非零竖直波数或固定无穿透边界才排除竖直运动。保留退化模态限制，刚盖或静力不自动滤除内波。',True)
add('2025-四-1','DYN02','稳态无摩擦伯努利积分、正压压力势和干绝热焓特例已核。课件能确认能量定义，不能恢复原卷缺录的三个起始式；当前仍是注明条件的解答。')
add('2025-四-2','DYN02','能量组合代数与局地压力项已核；干式守恒需无源汇且局地压力不变，湿式还需稀薄水汽及忽略降水能量等近似。课件整柱积分关系不能当作任意气块gz=RT。原卷三个起始式仍缺录。')
add('2025-四-3','DYN02','机械伯努利、干湿焓与静力能适用条件已核，静力本身不保证守恒。原卷起始式缺录，教材的能量名称无法确定原卷唯一要求的范围。')
add('2023-四-1','DYN03','课件尺度分析的科氏项是fU，量纲为加速度；若原题β是∂f/∂y，则βU量纲不符。将β按f解释仍属修正假设，不能用课件例题替代缺失原卷数据。')
add('2023-四-2','DYN03','已核对准地转W=εUH/L及βL/f₀=εb的零阶、一阶展开，并将压力偏导简写展开。课件有教学尺度示例，但原卷表格和数据未保存，故保留原卷待核。')
add('2018-四-整题','DYN04','课件与积分推导均确认Rayleigh–Kuo变号条件仅为必要条件。原题未给基本流剖面、波数或边界，不能求唯一临界风速；余弦流例子只是额外模型的变号门槛。')
add('2017-一-8','DYN05','课件分别定义无量纲Rossby数Ro与有量纲β参数，但原题“罗斯贝参数”未提供语境，不能确定唯一所指；保留两种定义与单位，不混称。')
add('2016-四-整题','DYN06','长波课件支持均匀基本流、正压无辐散β平面模型的色散推导；原题只称“给出公式”而未录实际原式，含变形半径或切变的模型不等价，故仍待原卷确认。')
add('2013-三-1','DYN07','若u为速度，uζ与Dζ/Dt量纲不一致；将其按阻尼率μ解释并取均匀U可核得线性阻尼式，但未找到原卷完整式。侧壁与y无关模态的可容许性也须原边界确认。')
add('2013-三-2','DYN07','在明确修正为常系数阻尼μ、均匀U的模型中，ω=kU−iμ，振幅增长率为−μ；μ≥0时无指数增长。该条件解不能代替缺失基本流和边界下的切变不稳定答案。')
add('2010-二-2','DYN08','滤波课件明确使用H(y)，支持修正所存H₀(x)的方向错误；一致β平面基本态满足g∂H/∂y=−f(y)U。原卷截断模型仍不完整，不能从精确常f动量式直接导出βv项。')
add('2010-二-3','DYN08','H(y)方向已由课件确认。所列频率式只对应注明的局地系数与散度式截断；它与另一套三方程滤波模型的高频β修正不同，不能拼作全域变系数系统的精确解，原卷模型仍待核。')
add('2006_1-二-1 2004_1-二-1','DYN08','常f的两条精确动量式与额外βv涡度式一般不相容。课件支持使用选定三方程的局地滤波模型；当前三次式代数已核，但它不是所存四式的精确一般解，原卷截断层级仍待确认。')
add('2006_1-二-2 2004_1-二-2','DYN08','在上一问声明的局地滤波近似下，区分慢罗斯贝波与快惯性重力波；快波含正负两支，慢波有位涡梯度回复。分类可核，但原卷常f与β项相容性疑点仍适用。')
assert len(notes)==17
for e in notes.values():
 for a,b in [('∂w/∂z=0',r'$\frac{\partial w}{\partial z}=0$'),('∂f/∂y',r'$\frac{\partial f}{\partial y}$'),('g∂H/∂y=−f(y)U',r'$g\frac{\partial H}{\partial y}=-f(y)U$')]:
  e['note']=e['note'].replace(a,b)

recovered={
'2010-二-2':r'''**按课件修正后的条件推导。** 将所存 $H_0(x)$ 改为 $H(y)$，取 $u=U+u'$、$v=v'$、$h=H(y)+h'$，$U$ 为常数。精确β平面基本态须满足 $g\frac{\partial H}{\partial y}=-f(y)U$，其中 $f(y)=f_0+\beta y$。

令 $\mathcal D=\frac{\partial}{\partial t}+U\frac{\partial}{\partial x}$，舍去扰动二阶项，得到
$$\mathcal D u'-f(y)v'=-g\frac{\partial h'}{\partial x},\qquad \mathcal D v'+f(y)u'=-g\frac{\partial h'}{\partial y},$$
$$\mathcal D h'+H\left(\frac{\partial u'}{\partial x}+\frac{\partial v'}{\partial y}\right)+v'\frac{\partial H}{\partial y}=0.$$
对第二动量式取x偏导减去第一式的y偏导，定义 $\zeta'=\frac{\partial v'}{\partial x}-\frac{\partial u'}{\partial y}$、$D'=\frac{\partial u'}{\partial x}+\frac{\partial v'}{\partial y}$，得
$$\boxed{\mathcal D\zeta'+\beta v'+f(y)D'=0}.$$
此后才可说明局地近似，将伸缩项的 $f(y)$ 冻结为 $f_0$。若先将两动量式精确设为常f，则取旋度不会产生β项。''',
'2013-三-2':r'''**以下仅延续上一问的修正模型。** 将所存速度字符u解释为阻尼率 $\mu$（单位 $\mathrm{s^{-1}}$），取均匀基本流U，线性式为
$$\left(\frac{\partial}{\partial t}+U\frac{\partial}{\partial x}\right)\zeta'+\mu\zeta'=0.$$
代入 $\zeta'=\hat\zeta e^{i(kx-\omega t)}$，得 $-i\omega+ikU+\mu=0$，即 $\omega=kU-i\mu$。时间因子为 $e^{-ikUt}e^{-\mu t}$，振幅增长率 $\sigma=-\mu$。非负摩擦阻尼只使扰动衰减；形式上 $\mu<0$ 是外加负阻尼供能，不能叫作已证明的切变不稳定。若原题意在求切变不稳定，仍需原基本流、完整方程与边界。''',
'2006_1-二-2':r'''沿用上一问声明的局地近似，$c_0^2=gH$、$L_D=c_0/|f_0|$，慢根为
$$\omega_R\approx-\frac{\beta k}{k^2+L_D^{-2}},$$
其回复机制为背景位涡梯度，偏涡旋性，对 $\beta>0$ 的静止背景内禀纬向相速向西。快根零阶为
$$\omega_\pm\approx\pm\sqrt{f_0^2+c_0^2k^2},$$
由重力与旋转共同回复，质量场和辐散振荡明显。所谓两类是罗斯贝波与惯性重力波，后者有两个频率分支；均是上一问所选局地模型的结论。'''
}
recovered['2004_1-二-2']=recovered['2006_1-二-2']

counts={q:0 for q in notes}
for p in (root/'每日内容').glob('D*.md'):
 text=p.read_text(encoding='utf-8');before=text
 for q,e in notes.items():
  def update(m):
   counts[q]+=1;s=m[0]
   s=re.sub(r'\*\*本次复核提示（[^\n]*\n',lambda _: '**本次复核提示（2026-11-04）：** '+e['note']+'\n',s,count=1)
   s=re.sub(r'\*\*审校状态：[^\n]*', '**审校状态：'+('内容已复核，课件两条件已定位；边界限制见下文。**' if q=='2026-三-3' else '条件推导已复核；原卷信息仍待核。**'),s)
   if q=='2026-三-3':
    s=s.replace(r'\omega \frac{\partial \bar{\theta}}{\partial z}',r'w \frac{\partial \bar{\theta}}{\partial z}')
    s=s.replace('按原λ位于连续式、热力式ω解释为竖直速度w，','按课件λ位于连续式、热力式速度校正为w，')
    s=re.sub(r'9\. \*\*答案边界。\*\*[^\n]*','9. **课件与答案边界。** 已在第63—64页定位λ=0与N=0两个条件及竖直速度w的记号。λ=0的方程本身仅给出竖直速度不随高度变化，排除竖直运动仍需上述模态或边界条件；不照抄课件“水平无辐散”的简称，也不采用“静力或刚盖自动滤除内波”的概括。',s)
   if q in recovered and '· 完整解答' not in s.splitlines()[0]:
    status=s.index('**审校状态：');end=s.index('\n',status)
    s=s[:end]+'\n\n'+recovered[q]+'\n\n'
   return s
  text=re.sub(r'^### '+re.escape(q)+r' ·[^\n]*\n[\s\S]*?(?=^#{1,3} |\Z)',update,text,flags=re.M)
 if text!=before:p.write_text(text,encoding='utf-8')

# Targeted notation changes: scalar derivatives are distinct from force components.
substitutions={r'\partial_\lambda Q_\lambda':r'\frac{\partial Q_\lambda}{\partial\lambda}',r'\partial_\varphi(Q_\varphi\cos\varphi)':r'\frac{\partial (Q_\varphi\cos\varphi)}{\partial\varphi}',r'p_r/\rho':r'\frac{1}{\rho}\frac{\partial p}{\partial r}',r'D_t-f_0\zeta':r'\frac{\partial D}{\partial t}-f_0\zeta'}
substitutions['p_r']=r'\frac{\partial p}{\partial r}'
for xy in ['x','y']:
 substitutions[r'\pi_{'+xy+r'^*}']=r'\frac{\partial\pi}{\partial '+xy+r'^*}'
 for n in ['0','1']:substitutions[r'\pi_{'+n+xy+'}']=r'\frac{\partial\pi_'+n+r'}{\partial '+xy+'}'
old=r'$(F_x)_z=(\widetilde F_x)_p+F_p(\frac{\partial p}{\partial x})_z$，以及 $F_z=F_p\frac{\partial p}{\partial z}$'
new=r'$\left(\frac{\partial F}{\partial x}\right)_z=\left(\frac{\partial\widetilde F}{\partial x}\right)_p+\frac{\partial\widetilde F}{\partial p}\left(\frac{\partial p}{\partial x}\right)_z$，以及 $\frac{\partial F}{\partial z}=\frac{\partial\widetilde F}{\partial p}\frac{\partial p}{\partial z}$'
notation=0
for p in (root/'每日内容').glob('D*.md'):
 text=p.read_text(encoding='utf-8');before=text
 # Do not edit simulator appendices owned by other reviewers.
 split=text.find('## 限时模拟与复盘');head=text if split<0 else text[:split];tail='' if split<0 else text[split:]
 for a,b in substitutions.items():notation+=head.count(a);head=head.replace(a,b)
 notation+=head.count(old);head=head.replace(old,new)
 head=head.replace(r'原式$F_z=F_p\frac{\partial p}{\partial z}$中的两个下标p均为偏导，即',r'原式的标量F下标简写已展开为偏导，即')
 text=head+tail
 if text!=before:p.write_text(text,encoding='utf-8')
p=root/'逐题复核记录.md';lines=p.read_text(encoding='utf-8').splitlines()
for i,l in enumerate(lines):
 m=re.match(r'\| \[([^]]+)\]',l)
 if m and m[1] in notes:
  e=notes[m[1]];lines[i]=l.split(' | ')[0]+' | '+e['status']+' | '+e['note'].replace('|',r'\|')+' |'
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
(root/'scripts/review_dynamics_evidence.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert all(counts.values()),counts
print('updated question counts',counts,'notation replacements',notation)
