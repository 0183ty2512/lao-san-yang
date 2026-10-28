<!-- 题13 -->
**第一步：使用和差化积。** 当两振幅均为 $A_0$，
$$\varphi=2A_0\cos\frac{\delta kx-\delta\omega t}{2}\cos\left[(k+\delta k/2)x-(\omega+\delta\omega/2)t\right].$$
第一因子是带符号的慢包络，绝对振幅为其绝对值；第二因子是快载波。

**第二步：追踪包络。** 保持 $\delta kx-\delta\omega t$ 为常数，微分得 $\delta k\,dx-\delta\omega\,dt=0$，故包络速度 $c_{g,\delta}=\delta\omega/\delta k$。

**第三步：取窄带极限。** 同一频散分支上 $\delta\omega=\omega(k+\delta k)-\omega(k)$，所以 $\lim_{\delta k\to0}c_{g,\delta}=d\omega/dk$。严格两列有限间隔的波对应差商，只有极限才是导数；两列波本身是无限重复的拍，真正局地波包可由一簇近波数叠加形成。
<!-- 题14 -->
**第一步：把波数写成频率的函数。** 在可局部反演的频散分支上，$c(\omega)=\omega/k$，故 $k=\omega/c(\omega)$。

**第二步：对频率求导。** 使用商法则，
$$\frac{dk}{d\omega}=\frac{c-\omega\,dc/d\omega}{c^2}.$$
**第三步：取倒数。** 当该导数非零且有限时，
$$c_g=\frac{d\omega}{dk}=\left(\frac{dk}{d\omega}\right)^{-1}=\frac{c^2}{c-\omega\,dc/d\omega}.$$
若 $c=0$ 或分支不能反演，此表达式可能出现退化，宜直接用 $d\omega/dk$。无频散时 $dc/d\omega=0$，立即得到 $c_g=c$，可作为检查。
<!-- 题15 -->
**第一步：代入复指数。** 设 $u'=\hat u e^{i(kx-\omega t)}$，实 $k$，则 $\partial_t\to-i\omega$、$\partial_x\to ik$、$\partial_x^2\to-k^2$、$\partial_x^3\to-ik^3$。方程成为
$$-i\omega+i\bar uk=-\mu k^2+i\beta k^3.$$
**第二步：求复频率。** 两边乘 $i$ 并整理，得 $\omega=\bar uk-\beta k^3-i\mu k^2$。因此时间振幅为 $e^{-\mu k^2t}$，实相速 $c_p=\bar u-\beta k^2$，实群速 $c_g=\bar u-3\beta k^2$。

**第三步：逐类判断（针对非零波数的一般波谱）。** $\mu=0$ 时无耗散；$\mu>0$ 时衰减；$\mu<0$ 是反扩散增长而非耗散。$\beta=0$ 时传播相速无频散；$\beta\ne0$ 时有频散。

**第四步：组合条件。** 无频散且有耗散为 $\beta=0,\mu>0$；无耗散且有频散为 $\mu=0,\beta\ne0$；两者皆无为 $\mu=\beta=0$。不同波数在扩散下衰减不同仍可改变波形，但这是选择性阻尼，不能因此把实相速也判为频散。
<!-- 题16 -->
**第一步：选均匀静止基本态。** $u=0+u'$、$\rho=\rho_0+\rho'$、$p=p_0+p'$，$p_0=\rho_0RT_0$。忽略扰动乘积，动量与连续方程分别为 $u_t'+p_x'/\rho_0=0$、$\rho_t'+\rho_0u_x'=0$；等温状态关系为 $p'=RT_0\rho'=c_T^2\rho'$。

**第二步：消元。** 对连续方程求时间导数，再用动量方程，$\rho_{tt}'=-\rho_0u_{xt}'=p_{xx}'=c_T^2\rho_{xx}'$，故 $\rho_{tt}'-c_T^2\rho_{xx}'=0$。

**第三步：代入简谐波。** 令 $(u',\rho',p')=(U,R_1,P)e^{i(kx-\omega t)}$，得 $\omega^2=c_T^2k^2$，$R_1=\rho_0kU/\omega$、$P=c_T^2R_1=\rho_0\omega U/k$。

**第四步：振幅和位相。** 密度与压力始终同相。取沿 $+x$ 的分支 $\omega/k=c_T>0$，则 $P=\rho_0c_TU$、$R_1=\rho_0U/c_T$，三者同相；反向分支 $\omega/k=-c_T$ 时速度与压力、密度反相。对应实解可统一取各实振幅乘 $\cos(kx-\omega t)$，负振幅表示相差 $\pi$。
<!-- 题17 -->
**第一步：线性化绝热关系。** 对均匀静止基本态，题中的对数式一阶为 $p_t'/p_0=\kappa\rho_t'/\rho_0$，所以传播的非零频率声学分支满足 $p'=c_s^2\rho'$，$c_s^2=\kappa p_0/\rho_0=\kappa RT_0$。

**第二步：线性动量和连续方程。** 仍有 $u_t'=-p_x'/\rho_0$、$\rho_t'=-\rho_0u_x'$，时间微分连续式并代入动量式，得到 $\rho_{tt}'=c_s^2\rho_{xx}'$。

**第三步：求频率和振幅。** 简谐代入得 $\omega=\pm c_sk$，$\hat\rho=\rho_0k\hat u/\omega$、$\hat p=c_s^2\hat\rho$。故 $|\hat\rho|=\rho_0|\hat u|/c_s$、$|\hat p|=\rho_0c_s|\hat u|$。正向波三者同相，反向波压力与密度同相而与速度反相。绝热声速比等温声速大 $\sqrt\kappa$ 倍。

**第四步：交代零频率解。** 积分热力式只给出 $p'/p_0-\kappa\rho'/\rho_0$ 不随时间变；一般初值还可含静止熵扰动，不应声称所有线性扰动都满足声学支的 $p'=c_s^2\rho'$。非零波数下熵支可取 $u'=p'=0$、$\rho'\ne0$，温度补偿维持压力不变。
<!-- 题18 -->
**第一步：消去 $v'$。** 对第一动量式求时间导数：$u_{tt}'-f_0v_t'=-\Phi_{xt}'$。由第二式 $v_t'=-f_0u'-\Phi_y'$，代入得 $(\partial_t^2+f_0^2)u'=-\Phi_{xt}'-f_0\Phi_y'$。

**第二步：消去 $u'$。** 对第二动量式求时间导数：$v_{tt}'+f_0u_t'=-\Phi_{yt}'$。用 $u_t'=f_0v'-\Phi_x'$，得到 $(\partial_t^2+f_0^2)v'=-\Phi_{yt}'+f_0\Phi_x'$。

**第三步：先取水平散度。** 第一结果对 $x$ 求导、第二结果对 $y$ 求导相加，交叉项 $-f_0\Phi_{xy}'+f_0\Phi_{xy}'$ 相消，故 $(\partial_t^2+f_0^2)D'=-\nabla_h^2\Phi_t'$。

**第四步：代连续方程。** $D'=-\Phi_t'/c_0^2$，因此 $(\partial_t^2+f_0^2)\Phi_t'=c_0^2\nabla_h^2\Phi_t'$。注意这是对 $\Phi_t'$ 的波动方程，保留了 $\Phi_t'=0$ 的地转定常支；直接对时间积分时须保留积分函数，不能无条件把 $\Phi'$ 全部当作自由波。
<!-- 题19 -->
**第一步：代入简谐形式。** 取 $e^{i(kx+ly-\omega t)}$，第18题的位势方程化为 $(-\omega^2+f_0^2)(-i\omega)\hat\Phi=-c_0^2(k^2+l^2)(-i\omega)\hat\Phi$。

**第二步：分清分支。** 频率方程为 $\omega[\omega^2-f_0^2-c_0^2K_h^2]=0$，$K_h^2=k^2+l^2$。$\omega=0$ 是地转支；传播的重力惯性外波为 $\omega=\pm\sqrt{f_0^2+c_0^2K_h^2}$。

**第三步：相速和群速。** 对 $K_h\ne0$，
$$\mathbf c_p=\frac{\omega}{K_h^2}(k,l),\qquad \mathbf c_g=(\omega_k,\omega_l)=\frac{c_0^2}{\omega}(k,l).$$
**第四步：证明共线。** 两矢量都乘同一波数矢量，叉积为零；比例 $\mathbf c_g/\mathbf c_p=c_0^2K_h^2/\omega^2>0$，在每个传播分支上同向。且 $|c_p|\,|c_g|=c_0^2$。$K_h=0$ 为无空间传播的惯性振荡，相速公式不定义。
<!-- 题20 -->
**第一步：先解水平振幅。** 令 $\Phi'=\Phi_a\cos\Theta$，$\Theta=kx+ly-\omega t$，$\omega^2=f_0^2+c_0^2K_h^2$。复动量矩阵为
$$\begin{pmatrix}-i\omega&-f_0\\f_0&-i\omega\end{pmatrix}\binom{\hat u}{\hat v}=\binom{-ik\Phi_a}{-il\Phi_a}.$$
行列式 $f_0^2-\omega^2$，求逆得 $\hat u=(\omega k+if_0l)\Phi_a/(\omega^2-f_0^2)$、$\hat v=(\omega l-if_0k)\Phi_a/(\omega^2-f_0^2)$。

**第二步：取实部。**
$$u'=\frac{\Phi_a(\omega k\cos\Theta-f_0l\sin\Theta)}{c_0^2K_h^2},\quad v'=\frac{\Phi_a(\omega l\cos\Theta+f_0k\sin\Theta)}{c_0^2K_h^2}.$$
**第三步：求散度和垂直速度。** 连续方程给出 $D'=-\Phi_t'/c_0^2=-\omega\Phi_a\sin\Theta/c_0^2$。因水平风不随高且底部 $w'(0)=0$，$w'=-zD'=z\omega\Phi_a\sin\Theta/c_0^2$。顶端 $w'(H_0)=h_t'$ 可直接验证。

**第四步：取 $l=0$。** $u'=\Phi_a\omega\cos\Theta/(c_0^2k)$、$v'=\Phi_af_0\sin\Theta/(c_0^2k)$、$w'=z\omega\Phi_a\sin\Theta/c_0^2$。若 $k,\omega,f_0>0$，$u'$ 与 $\Phi'$ 同相，$v'$ 和 $w'$ 同相，二者与前两者相差四分之一周期。振幅比 $|v_a/u_a|=f_0/|\omega|$、$|w_a/u_a|=z|k|$；分支或方向改变时要保留系数符号。
<!-- 题21 -->
**修改意见：** 结论对应北半球 $f_0>0$、流体占 $x>0$ 的沿岸开尔文模态。刚壁只规定壁上法向速度为零，并不能单独排除所有其他浅水波；以下求随离岸距离衰减的沿岸陷获支。

**第一步：设模态。** 取各量 $\propto e^{-sx}e^{i(ly-\omega t)}$，$s>0$。单指数的法向速度在壁上为零，迫使其振幅为零，故此模态 $u'\equiv0$。

**第二步：沿岸动量和连续方程。** $-i\omega\hat v=-il\hat\Phi$，$-i\omega\hat\Phi+ilc_0^2\hat v=0$，所以 $\hat v=l\hat\Phi/\omega$，$\omega^2=c_0^2l^2$，$c=\omega/l=\pm c_0$。

**第三步：用横岸平衡选分支。** $-f_0v'=-\Phi_x'=s\Phi'$，即 $f_0\hat v=-s\hat\Phi$。结合 $\hat v=\hat\Phi/c$ 得 $s=-f_0/c$。北半球要求 $s>0$，只能 $c=-c_0$，且 $s=f_0/c_0$。

**第四步：写实解。** $\Phi'=\Phi_a e^{-f_0x/c_0}\cos[l(y+c_0t)]$，$v'=-\Phi'/c_0$，$u'=0$。振幅在壁处最大，以变形半径 $c_0/f_0$ 衰减；传播时海岸在右侧。南半球或流体位于壁另一侧，所选方向相反。
<!-- 题22 -->
**修改意见：** 第三个方程的首项应为 $\partial\Phi'/\partial t$；原稿写成 $\partial\Phi'/\partial x$，量纲不一致。陷获边界应在 $y\to\pm\infty$ 都衰减。

**第一步：施加 $v'=0$。** 修正方程化为 $u_t'=-\Phi_x'$、$\beta yu'=-\Phi_y'$、$\Phi_t'+c_0^2u_x'=0$。

**第二步：求频率。** 取 $u',\Phi'\propto e^{i(kx-\omega t)}$，第一、三式给出 $\omega\hat u=k\hat\Phi$、$\omega\hat\Phi=c_0^2k\hat u$，因此 $c=\omega/k=\pm c_0$、$\hat\Phi=c\hat u$。

**第三步：求经向结构。** 第二式给出 $d\hat\Phi/dy=-\beta y\hat\Phi/c$。分离变量积分，$\ln\hat\Phi=-\beta y^2/(2c)+\text{常数}$。若 $\beta>0$，只有 $c=c_0>0$ 才在两侧都衰减。

**第四步：列出特征。**
$$\Phi'=\Phi_a e^{-y^2/(2L_e^2)}\cos[k(x-c_0t)],\quad u'=\Phi'/c_0,\quad v'=0,\quad L_e=\sqrt{c_0/\beta}.$$
这是赤道开尔文波：向东无频散传播，赤道振幅最大，纬向风与位势同相、关于赤道对称，纬向惯性—压力梯度平衡与经向地转平衡并存。
<!-- 题23 -->
**第一步：写位温定义。** 本题 $\kappa=c_p/c_v$，故通常干绝热指数 $R/c_p=(\kappa-1)/\kappa$。位温 $\theta=T(p_r/p)^{R/c_p}$，取对数对 $z$ 求导。

**第二步：利用等温条件。** $d\ln T/dz=0$、$d\ln p/dz=-1/H$，所以
$$\sigma=\frac{d\ln\bar\theta}{dz}=-\frac{R}{c_p}\frac{d\ln\bar p}{dz}=\frac{\kappa-1}{\kappa H}.$$
**第三步：换用声速。** $c_s^2=\kappa R\bar T=\kappa gH$，所以 $1/(\kappa H)=g/c_s^2$，从而 $\sigma=g(\kappa-1)/c_s^2$。

**第四步：求浮力频率。** $N^2=g\sigma=g^2(\kappa-1)/c_s^2>0$。此处 $\sigma$ 单位为 $\mathrm{m^{-1}}$，不是第十一章 $p$ 坐标中的 $\sigma_s$，同名符号不能直接互换。
<!-- 题24 -->
**第一步：积分静力关系。** $d\bar p/dz=-\bar\rho g$，又 $\bar p=\bar\rho R\bar T$、$\bar T$ 为常数，故 $d\bar p/\bar p=-dz/H$。从0积分到 $z$，$\ln[\bar p(z)/\bar p(0)]=-z/H$，于是 $\bar p(z)=\bar p(0)e^{-z/H}$。

**第二步：用状态方程求密度。** 等温时 $\bar\rho(z)/\bar\rho(0)=\bar p(z)/\bar p(0)$，所以 $\bar\rho(z)=\bar\rho(0)e^{-z/H}$。

**第三步：求位温。**
$$\frac{\bar\theta(z)}{\bar\theta(0)}=\frac{\bar T(z)}{\bar T(0)}\left[\frac{\bar p(0)}{\bar p(z)}\right]^{R/c_p}=e^{Rz/(c_pH)}.$$
因此 $\bar\theta(z)=\bar\theta(0)e^{Rz/(c_pH)}$。压力、密度随高减小，位温随高增大，与等温大气稳定层结的结论相符。
