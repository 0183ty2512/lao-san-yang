<!-- 题25 -->
**修改意见：** 第四式末项应为 $(\kappa N^2/g)w'$，不是 $N^2w'$。原式左右量纲不同；从对数热力式独立展开可确定系数。

**第一步：水平动量。** 静止基本态仅依赖 $z$，$\bar p_x=0$。一阶为 $u_t'+p_x'/\bar\rho=0$。令 $P=p'/\bar p$、$R_1=\rho'/\bar\rho$，因 $\bar p/\bar\rho=c_s^2/\kappa$，得 $u_t'+(c_s^2/\kappa)P_x=0$。

**第二步：垂直动量。** 展开 $1/\rho=1/\bar\rho-\rho'/\bar\rho^2$，减去基本态静力式 $\bar p_z/\bar\rho=-g$，得 $w_t'+p_z'/\bar\rho+gR_1=0$。而 $p_z'=\bar p P_z+\bar p_zP$，故 $w_t'+(c_s^2/\kappa)P_z+g(R_1-P)=0$。

**第三步：连续方程。** 一阶为 $\rho_t'+w'\bar\rho_z+\bar\rho(u_x'+w_z')=0$。除以 $\bar\rho$ 并用 $\bar\rho_z/\bar\rho=-1/H$，得到 $R_{1t}+u_x'+w_z'-w'/H=0$，其中 $1/H=g\kappa/c_s^2$。

**第四步：热力关系。** 分别展开两个物质导数，得
$$P_t+w'\frac{d\ln\bar p}{dz}=\kappa\left(R_{1t}+w'\frac{d\ln\bar\rho}{dz}\right).$$
两背景对数梯度均为 $-1/H$，故 $P_t-\kappa R_{1t}+(\kappa-1)w'/H=0$。第23题 $N^2=g(\kappa-1)/(\kappa H)$，因此系数 $(\kappa-1)/H=\kappa N^2/g$。四式均为线性，含热力、静力背景效应而未去掉声波。
<!-- 题26 -->
**修改意见：** 采用第25题已修正的热力式。还需明确 $k,m,\omega,\alpha$ 为实数、$m\ne0$，讨论中性垂直传播支；若允许复频率或指数增长，不能只凭原题一句话强制推出唯一的 $\alpha$。

**第一步：建立代数方程。** 记 $s=\alpha+im$、$h=1/H$、$a=c_s^2/\kappa=gH$。把题设形式代入，得到
$$-i\omega A+ikaC=0,$$
$$-i\omega B+a(s-h)C+gD=0,$$
$$-i\omega D+ikA+(s-h)B=0,$$
$$-i\omega C+i\kappa\omega D+(\kappa-1)hB=0.$$
**第二步：先消去 $A,D$。** 第一式给 $A=kaC/\omega$；第三式给 $D=ak^2C/\omega^2-i(s-h)B/\omega$。代入第四式，化为
$$\frac{i(c_s^2k^2-\omega^2)}{\omega}C+(\kappa s-h)B=0.$$
第二式则化为
$$a\left(s-h+\frac{gk^2}{\omega^2}\right)C-i\left[\omega+\frac{g(s-h)}{\omega}\right]B=0.$$
**第三步：令两式行列式为零。** 消去 $C,B$ 得
$$a\omega^2\left(s-h+\frac{gk^2}{\omega^2}\right)(\kappa s-h)-(\omega^2+g(s-h))(c_s^2k^2-\omega^2)=0.$$
展开后，$a\kappa=c_s^2$、$ah=g$ 使一次交叉项抵消，剩下
$$\omega^2c_s^2(s^2-hs)+\omega^4-c_s^2k^2\omega^2+g^2(\kappa-1)k^2=0.$$
除以 $\omega^2c_s^2$，用 $N^2=g^2(\kappa-1)/c_s^2$，得 $s^2-hs+\omega^2/c_s^2-k^2+N^2k^2/\omega^2=0$。

**第四步：分离虚部。** $s^2-hs=(\alpha^2-m^2-h\alpha)+im(2\alpha-h)$。其余项实，因此 $m(2\alpha-h)=0$；$m\ne0$ 时 $\alpha=h/2=1/(2H)$。

**第五步：取实部并整理。** $s^2-hs=-m^2-h^2/4$，于是
$$m^2=k^2\left(\frac{N^2}{\omega^2}-1\right)+\frac{\omega^2-\omega_a^2}{c_s^2},\qquad\omega_a=\frac{c_s}{2H}.$$
乘以 $\omega^2c_s^2$ 后移项，即得 $\omega^4-[c_s^2(k^2+m^2)+\omega_a^2]\omega^2+c_s^2N^2k^2=0$。增长因子 $e^{z/(2H)}$ 与背景密度减小相配合，使 $\bar\rho|\mathbf V'|^2$ 不随高指数增加，不能把它直接判为时间不稳定。
<!-- 题27 -->
**第一步：化为二次式。** 令 $X=\omega^2$、$S=c_s^2(k^2+m^2)+\omega_a^2$、$P=c_s^2N^2k^2$，频率方程为 $X^2-SX+P=0$。

**第二步：求根。**
$$\omega_\pm^2=\frac{S\pm\sqrt{S^2-4P}}2.$$
每个正的 $\omega^2$ 又有正负两个频率分支。大根 $\omega_+^2$ 是受层结和重力影响的声波，小根 $\omega_-^2$ 是受可压缩性影响的重力波。

**第三步：检查判别式。** 因 $\omega_a^2\ge N^2$，$S\ge c_s^2k^2+N^2$，故 $S^2-4c_s^2N^2k^2\ge(c_s^2k^2-N^2)^2\ge0$；稳定等温大气的这两支为实频率。

**第四步：解释极限。** 若 $P/S^2\ll1$，用 $\sqrt{1-4P/S^2}\simeq1-2P/S^2$，得声支 $\omega_+^2\simeq S-P/S$，重力支 $\omega_-^2\simeq P/S=N^2k^2/[k^2+m^2+1/(4H^2)]$。只有进一步 $k^2+m^2\gg1/(4H^2)$ 才化为熟悉的不可压缩内波式，不能把该近似当成完整精确根。
<!-- 题28 -->
**第一步：写传播判据。** 对实水平波数 $k$，垂直传播要求
$$m^2=k^2(N^2/\omega^2-1)+(\omega^2-\omega_a^2)/c_s^2>0.$$
令 $X=\omega^2>0$，乘 $c_s^2X$ 后得 $X^2-(\omega_a^2+c_s^2k^2)X+c_s^2N^2k^2>0$。

**第二步：求给定 $k$ 的边界。**
$$X_\pm(k)=\frac{\omega_a^2+c_s^2k^2\pm\sqrt{(\omega_a^2+c_s^2k^2)^2-4c_s^2N^2k^2}}2.$$
开口向上的二次多项式在两根之外为正，故重力内波传播带是 $0<X<X_-$，声内波带是 $X>X_+$；根上 $m=0$ 为边界。

**第三步：求普遍上、下限。** 当 $N^2<X<\omega_a^2$，原式两个项均为负，所以不可能垂直传播。并且 $X_-\le N^2$、$X_+\ge\omega_a^2$。因此重力内波 $|\omega|<N$，声内波 $|\omega|>\omega_a$ 是必要范围；给定非零 $k$ 时还要满足第二步更严格的范围，不能把必要条件当成充分条件。

**第四步：核实等温关系。** $\omega_a^2/N^2=\kappa^2/[4(\kappa-1)]$，减去1为 $(\kappa-2)^2/[4(\kappa-1)]\ge0$。空气 $\kappa\simeq1.4$，比值约1.0208，故确有小的禁带。$m^2<0$ 仅说明该频率与波数下垂直消逝；要成为真正的外模态，还要满足垂直边界条件。
<!-- 题29 -->
**第一步：用静力关系求水平压力梯度。** 自由面压力常量 $p_s$，常密度且静力时 $p=p_s+\rho g(h-z)$。固定几何高度求导得 $p_x/\rho=gh_x$、$p_y/\rho=gh_y$，所以两条水平动量式正是题给形式。这里还采用浅水假设，水平速度近似整层一致。

**第二步：积分不可压缩连续方程。** $u_x+v_y+w_z=0$，从底 $h_B$ 到面 $h$ 积分，得 $H(u_x+v_y)+w(h)-w(h_B)=0$，其中 $H=h-h_B$。

**第三步：使用运动学边界。** 固定地形底部 $w(h_B)=u h_{Bx}+v h_{By}$；自由面 $w(h)=h_t+u h_x+v h_y$。相减并用 $H_t=h_t$、$\nabla H=\nabla h-\nabla h_B$，得到 $H_t+uH_x+vH_y+H(u_x+v_y)=0$。

**第四步：写守恒形式。** 乘法求导规则给出 $\partial_x(uH)=uH_x+Hu_x$，$y$ 同理，因此 $H_t+(uH)_x+(vH)_y=0$。动力方程中的高度是自由面 $h$，质量方程中的厚度是 $H$；有地形时二者不能互换。
<!-- 题30 -->
**题目说明：** 原稿本条仅附第29题的示意图，没有新的计算或证明要求，因此作为图示条目保留，不虚构问句。

**第一步：确认三个高度。** 相同固定基准面上，$h_B(x,y)$ 是底部高程，$h(x,y,t)$ 是自由面高程；两者之间的距离为流体厚度 $H=h-h_B$。

**第二步：说明动力含义。** 水平压力梯度取决于自由面坡度 $\nabla h$；即使 $h$ 水平，倾斜底部仍会使水柱厚度有空间梯度，但不会凭空产生静止流体中的水平压力梯度。

**第三步：连接后续题。** 气块跨越地形时，柱厚改变；浅水位涡 $(\zeta+f)/H$ 守恒将厚度变化转换成相对涡度变化，这是地形罗斯贝波的恢复机制。
<!-- 题31 -->
**第一步：区分常自由面与变厚度。** 静止基本态自由面为 $H_0$，底高为 $h_B(x,y)$，所以背景厚度 $H_b=H_0-h_B$，扰动后 $h=H_0+\eta$、$H=H_b+\eta$。原题 $H_0\gg\eta$ 还不足以保证浅水线性化处处有效，须背景水深 $H_b>0$ 且 $|\eta|\ll H_b$。

**第二步：线性化动量。** $u,v,\eta$ 均为一阶，舍去 $uu_x,vu_y$ 等二阶项，得 $u_t-fv=-g\eta_x$、$v_t+fu=-g\eta_y$。

**第三步：线性化厚度方程。** $\eta_t+\partial_x[u(H_b+\eta)]+\partial_y[v(H_b+\eta)]=0$。舍去 $u\eta,v\eta$，得到
$$\eta_t+\partial_x(H_bu)+\partial_y(H_bv)=0,$$
或 $\eta_t+H_b(u_x+v_y)-u h_{Bx}-v h_{By}=0$。地形是给定背景，$u\nabla h_B$ 是一阶，不能当成扰动乘积舍去。

**第四步：浅地形近似。** 若还取 $|h_B|\ll H_0$，可在散度系数中近似 $H_b\simeq H_0$，同时按研究尺度保留 $-\mathbf V\cdot\nabla h_B$，得到后续地形波所需的约束。
<!-- 题32 -->
**修改意见：** 原题引用“第30题的扰动方程”应为第31题。以下取北半球常 $f_0$，保留地形的背景位涡梯度。

**第一步：由涡度与连续方程消去散度。** $\zeta_t+f_0D=0$；线性厚度式为 $\eta_t+H_0D-vh_{By}=0$，故 $D=-\eta_t/H_0+vh_{By}/H_0$。代入得 $\partial_t(\zeta-f_0\eta/H_0)+(f_0h_{By}/H_0)v=0$。

**第二步：用准地转关系。** $\psi=g\eta/f_0$、$u=-\psi_y$、$v=\psi_x$、$\zeta=\nabla_h^2\psi$；令 $L_0^2=gH_0/f_0^2$、$\beta_T=f_0h_{By}/H_0$，得到 $\partial_t(\nabla_h^2\psi-L_0^{-2}\psi)+\beta_T\psi_x=0$。

**第三步：简谐代入。** 取 $e^{i(kx+ly-\omega t)}$，有 $i\omega(k^2+l^2+L_0^{-2})+i\beta_Tk=0$，故 $\omega=-\beta_Tk/(k^2+l^2+L_0^{-2})$。

**第四步：求纬向速度。**
$$c_x=\frac\omega k=-\frac{\beta_T}{k^2+l^2+L_0^{-2}},\quad c_{gx}=\frac{\partial\omega}{\partial k}=\frac{\beta_T(k^2-l^2-L_0^{-2})}{(k^2+l^2+L_0^{-2})^2}.$$
若仅依赖 $x$，令 $l=0$ 即可。地形坡度通过 $\beta_T$ 完全占据行星 $\beta$ 在该线性方程中的位置；坡度反向，传播性质的符号相应反转。
<!-- 题33 -->
**修改意见：** 本题原第④问末尾大小关系写反；第⑥问的分母 $g$ 应为数字8。下面严格从题给的 $c_2$ 推导，不擅自换用另一种基本态下的浅水罗斯贝公式。取 $U=\bar u>0,\beta>0,a=L_0^{-2}>0$。

**第一步：化简两个相速并求群速。** $c_1=U-\beta/k^2$，$\omega_1=Uk-\beta/k$，所以 $c_{g1}=U+\beta/k^2$。第二式化为 $c_2=(Uk^2-\beta)/(k^2+a)=U-(Ua+\beta)/(k^2+a)$。对 $\omega_2=kc_2$ 求导：
$$c_{g2}=c_2+k\frac{dc_2}{dk}=U+\frac{(Ua+\beta)(k^2-a)}{(k^2+a)^2},\quad c_{g2}-c_2=\frac{2k^2(Ua+\beta)}{(k^2+a)^2}>0.$$
**第二步：算静止波。** $c_1=0$ 给 $k_s^2=\beta/U$，$L_s=2\pi\sqrt{U/\beta}$。取地球半径 $a_E=6.371\times10^6\ \mathrm m$，$\beta=2\Omega\cos45^\circ/a_E=1.619\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$，得 $L_s\simeq6.048\times10^6\ \mathrm m$。纬圈长度 $2\pi a_E\cos45^\circ\simeq2.831\times10^7\ \mathrm m$，波数约4.68，即约5个波；连续模型所得4.68不是必须恰为整数的全球本征模。

**第三步：无辐散波的长短波性质。** $L\to0$ 意味 $|k|\to\infty$，二速度均趋向 $U$；有限非零 $k$ 下 $c_{g1}-c_1=2\beta/k^2>0$。$L>L_s$ 即 $k^2<\beta/U$，因此 $c_1<0$；$L<L_s$ 则 $c_1>0$。原稿的 $L=0$ 应理解为极限，零波长不是实际波。

**第四步：有辐散波的符号。** $c_2$ 的分母正，零点仍是 $k_s$。短于 $L_s$ 时 $c_2>0$ 且 $c_{g2}>c_2>0$。群速零点满足
$$Us^2+(3Ua+\beta)s-\beta a=0,\quad s=k^2.$$
正根 $s_*=[-(3Ua+\beta)+\sqrt{(3Ua+\beta)^2+4U\beta a}]/(2U)$，令 $L_s'=2\pi/\sqrt{s_*}$。因群速在 $k_s$ 处仍正、在 $k=0$ 处为负，$L_s'>L_s$。当 $L>L_s'$，两速度均负，但始终 $c_{g2}>c_2$，故应是 $|c_{g2}|<|c_2|$，与原题相反。

**第五步：证明负极值。** $dc_2/ds=(Ua+\beta)/(s+a)^2>0$，故 $s\ge0$ 上最小值在0，$\min c_2=-\beta/a$。对群速，
$$\frac{dc_{g2}}{ds}=\frac{(Ua+\beta)(3a-s)}{(s+a)^3}.$$
因此从 $s=0$ 增加到 $3a$ 时递增，之后递减趋向正的 $U$，全局最小值仍为 $c_{g2}(0)=-\beta/a$。$k=0$ 的相速取极限定义。

**第六步：求群速最大值。** 导数在 $s=3a$ 变号为正到负，故
$$\max c_{g2}=U+\frac{(Ua+\beta)2a}{(4a)^2}=\frac98U+\frac{\beta}{8a}=\frac98U+\frac{\beta L_0^2}{8}.$$
原式 $\beta L_0^2/g$ 量纲也不是速度，因而不能成立。
<!-- 题34 -->
**修改意见：** 稳定层结的绝热热力式应为 $D_0(\theta'/\bar\theta)+(N^2/g)w'=0$，原题写成减号；用原符号无法推出题目要求的正号位涡项。以下取 $N^2>0$ 常数、布西内斯克常参考密度，$D_0=\partial_t+U\partial_x$。

**第一步：消去浮力和垂直速度。** 静力式给 $\theta'/\bar\theta=p_z'/(g\bar\rho)$。代入修正热力式，得 $D_0p_z'/\bar\rho+N^2w'=0$，所以 $w'=-D_0p_z'/(N^2\bar\rho)$。再对 $z$ 求导，$w_z'=-D_0p_{zz}'/(N^2\bar\rho)$。

**第二步：代入涡度方程。** $D_0\zeta'+\beta v'-f_0w_z'=0$ 化为
$$D_0\left(\zeta'+\frac{f_0p_{zz}'}{N^2\bar\rho}\right)+\beta v'=0.$$
若 $N^2$ 随高变化，正确形式应将 $\partial_z[N^{-2}\partial_zp']$ 保留，不能把系数移出导数。

**第三步：引入地转流函数。** $\psi=p'/(f_0\bar\rho)$ 给 $u'=-\psi_y$、$v'=\psi_x$、$\zeta'=\nabla_h^2\psi$，所以
$$D_0\left(\nabla_h^2\psi+\frac{f_0^2}{N^2}\psi_{zz}\right)+\beta\psi_x=0.$$
**第四步：代入简谐波。** 令 $Q=k^2+l^2+f_0^2m^2/N^2$，算子 $D_0\to-i(\omega-Uk)$、位涡振幅为 $-Q\psi$，故 $i(\omega-Uk)Q+i\beta k=0$，即 $\omega=k[U-\beta/Q]$。

**第五步：求定常波垂直传播条件。** 对 $k\ne0$ 的定常波 $\omega=0$，有 $Q=\beta/U$，因此
$$m^2=\frac{N^2}{f_0^2}\left[\frac\beta U-(k^2+l^2)\right].$$
要 $m^2>0$，且 $\beta>0$，必须 $0<U<\beta/(k^2+l^2)$。东风 $U<0$ 或过强西风均使 $m^2<0$，垂直呈消逝。$k=0$ 时没有纬向变化，不能通过除以 $k$ 推得上述结论；局地传播还不自动保证穿过整层，真实大气的转向层、临界层及随高变的背景须另检验。
