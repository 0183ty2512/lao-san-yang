# Boussinesq 近似推导

> 自然对流、大气边界层、海洋内波等流动中，密度变化微小，仅在浮力效应中起主导作用。Boussinesq 近似（Joseph Boussinesq, 1903）通过合理简化，使方程既保留了浮力驱动又极大降低了复杂度。

---

## 1. 原始控制方程

考虑粘性流体的质量、动量、能量守恒，状态方程联系密度与温度（忽略压力对密度的影响）。
$$
\begin{align}
\frac{\partial \rho}{\partial t} + \nabla\cdot(\rho \mathbf{u}) &= 0 \tag{1a} \\
\rho\left(\frac{\partial \mathbf{u}}{\partial t} + \mathbf{u}\cdot\nabla\mathbf{u}\right) &= -\nabla p + \mu\nabla^2\mathbf{u} + \rho\,\mathbf{g} \tag{1b} \\
\rho c_p\left(\frac{\partial T}{\partial t} + \mathbf{u}\cdot\nabla T\right) &= k\nabla^2 T + \Phi \tag{1c}
\end{align}
$$

重力矢量 $\mathbf{g} = -g\,\mathbf{k}$（$\mathbf{k}$ 为垂直向上单位矢量，$g$ 为重力加速度大小），$\Phi$ 为粘性耗散，在 Boussinesq 近似中忽略。流体物性 $\mu,\,c_p,\,k$ 均视为常数。

> [!note] 为什么要近似？
> 完全可压缩 Navier-Stokes 方程中，密度 $\rho$ 同时出现在连续性方程、动量方程的惯性项和重力项中，且通过状态方程与温度和压力耦合。声波与对流的时间尺度相差数个量级，直接数值求解代价极高。Boussinesq 近似通过**滤除声波**（使 $\nabla\cdot\mathbf{u}=0$），同时**仅在重力项中保留密度扰动**（浮力驱动），实现了物理本质与计算效率的折中。

---

## 2. 静力参考状态

设背景流体静止，参考密度 $\rho_0$ 为常数，参考压力 $p_0(z)$ 满足静力平衡：

$$
\frac{d p_0}{d z} = -\rho_0 g \quad\Longrightarrow\quad \nabla p_0 = \rho_0\,\mathbf{g}.
$$

将瞬时场分解为参考值与扰动量：

$$
\rho = \rho_0 + \rho'(\mathbf{x},t),\quad
p = p_0(z) + p'(\mathbf{x},t),\quad
T = T_0 + \theta(\mathbf{x},t),
$$

且假设 $|\rho'| \ll \rho_0,\ |p'| \ll |p_0|,\ |\theta| \ll T_0$。

> [!warning] 关键前提
> Boussinesq 近似要求**垂直尺度远小于密度标高** $H_\rho = \rho_0/|d\rho_0/dz|$。在大气边界层（~1 km）中此条件自然满足；但在整个对流层（~10 km）中，背景密度变化显著，标准 Boussinesq 近似不再适用，需采用**非弹性近似**（anelastic approximation）或**扩展 Boussinesq 近似**。

---

## 3. 连续性方程的简化

将分解代入 (1a)：

$$
\frac{\partial \rho'}{\partial t} + \nabla\cdot\big[(\rho_0+\rho')\mathbf{u}\big]
= \frac{\partial \rho'}{\partial t} + \rho_0\nabla\cdot\mathbf{u} + \nabla\cdot(\rho'\mathbf{u}) = 0.
$$

利用尺度分析：$\rho'/\rho_0 \sim \epsilon \ll 1$，特征速度 $U$，长度 $L$，时间 $L/U$。各项量级为：

$$
\frac{\partial \rho'}{\partial t} \sim \frac{\epsilon\rho_0 U}{L},\quad
\rho_0\nabla\cdot\mathbf{u} \sim \frac{\rho_0 U}{L},\quad
\nabla\cdot(\rho'\mathbf{u}) \sim \frac{\epsilon\rho_0 U}{L}.
$$

保留最高阶项 $\rho_0\nabla\cdot\mathbf{u}$，立刻得到**不可压缩约束**：

$$
\boxed{\nabla\cdot\mathbf{u} = 0}. \tag{2}
$$

严格的低马赫数渐近分析表明，当流速远小于声速，且 $\partial\rho'/\partial t \sim \mathbf{u}\cdot\nabla\rho'$ 均远小于 $\rho_0\nabla\cdot\mathbf{u}$ 时，此近似成立。若结合能量方程，$\nabla\cdot\mathbf{u} \approx \beta\kappa\nabla^2\theta$ 极微，故可直接取零。

> [!note] 物理直觉
> 连续性方程退化为 $\nabla\cdot\mathbf{u}=0$，意味着**声波被完全滤除**，流体在运动学上是不可压缩的——速度场的散度为零，如同不可压缩等温流动。密度变化仅通过浮力项间接影响速度场，而不直接参与质量守恒。这是 Boussinesq 近似在数值计算中效率远高于完全可压缩模型的根本原因。

---

## 4. 动量方程的浮力项——核心简化

将分解代入 (1b)，左端惯性项中 $\rho=\rho_0+\rho' \approx \rho_0$（忽略 $\rho'$ 的惯性效应）。右端：

$$
-\nabla p + \mu\nabla^2\mathbf{u} + \rho\mathbf{g}
= -\nabla p_0 - \nabla p' + \mu\nabla^2\mathbf{u} + \rho_0\mathbf{g} + \rho'\mathbf{g}.
$$

代入静力平衡 $\nabla p_0 = \rho_0\mathbf{g}$，则 $-\nabla p_0$ 与 $\rho_0\mathbf{g}$ 相互抵消，得到：

$$
\rho_0\frac{D\mathbf{u}}{Dt} = -\nabla p' + \mu\nabla^2\mathbf{u} + \rho'\mathbf{g}.
$$

除以 $\rho_0$，并令运动压力 $\pi = p'/\rho_0$，运动粘度 $\nu=\mu/\rho_0$，则

$$
\frac{D\mathbf{u}}{Dt} = -\nabla\pi + \nu\nabla^2\mathbf{u} + \frac{\rho'}{\rho_0}\mathbf{g}. \tag{3}
$$

定义**扰动浮力** $b \equiv -g\,\rho'/\rho_0$。利用 $\mathbf{g} = -g\,\mathbf{k}$，浮力项化为 $b\mathbf{k}$，于是动量方程化为

$$
\boxed{\frac{\partial\mathbf{u}}{\partial t} + \mathbf{u}\cdot\nabla\mathbf{u} = -\nabla\pi + \nu\nabla^2\mathbf{u} + b\,\mathbf{k}}. \tag{4}
$$

> [!note] 物理意义
> 只有密度扰动 $\rho'$ 产生净浮力。若 $\rho'<0$（轻流体），$b>0$，流体获得向上的加速度。这是 Boussinesq 近似的精髓——**密度变化仅在乘以 $\mathbf{g}$ 时被保留，在其他所有项中均被忽略**。

---

## 5. 能量方程与线性状态方程

忽略压力功和粘性耗散 $\Phi$，且设 $c_p,\,\rho_0$ 常数，方程 (1c) 约化为温度的对流-扩散方程。利用 $T=T_0+\theta$，若背景温度 $T_0$ 均匀，则有

$$
\boxed{\frac{\partial\theta}{\partial t} + \mathbf{u}\cdot\nabla\theta = \kappa\nabla^2\theta}, \qquad \kappa = \frac{k}{\rho_0 c_p}. \tag{5}
$$

为闭合浮力，采用热膨胀线性状态方程（忽略压力影响）：

$$
\rho = \rho_0\big[1 - \beta(T - T_0)\big] \quad\Longrightarrow\quad \rho' = -\rho_0\beta\theta,
$$

其中 $\beta$ 为体胀系数（对于理想气体 $\beta=1/T_0$）。扰动浮力简化为

$$
\boxed{b = g\beta\theta}. \tag{6}
$$

> [!summary] Boussinesq 方程组（最终形式）
> $$
> \begin{aligned}
> \nabla\cdot\mathbf{u} &= 0, \\
> \frac{\partial\mathbf{u}}{\partial t} + \mathbf{u}\cdot\nabla\mathbf{u} &= -\nabla\pi + \nu\nabla^2\mathbf{u} + g\beta\theta\,\mathbf{k}, \\
> \frac{\partial\theta}{\partial t} + \mathbf{u}\cdot\nabla\theta &= \kappa\nabla^2\theta.
> \end{aligned}
> $$

---

## 6. 近似成立条件

| 条件 | 数学表述 | 物理含义 |
|:---|:---|:---|
| 密度扰动极小 | $\|\rho'\|/\rho_0 \ll 1$ | 状态方程可线性化 |
| 低马赫数 | $\mathrm{Ma} = U/c_s \ll 1$ | 声波可忽略，流动接近不可压缩 |
| 垂直尺度远小于密度标高 | $L_z \ll H_\rho$ | 背景密度分层可视为均匀 |
| 粘性耗散可忽略 | $\mathrm{Ec} = U^2/(c_p\Delta T) \ll 1$ | 动能 $\rightarrow$ 内能的加热可忽略 |

### 6.1 马赫数与 Boussinesq 近似的定量关系

由低马赫数渐近展开（Spiegel & Veronis, 1960; Mihaljan, 1962）：

$$
\nabla\cdot\mathbf{u} = -\frac{1}{\rho_0}\frac{D\rho'}{Dt} \sim \mathcal{O}(\mathrm{Ma}^2).
$$

当 $\mathrm{Ma} < 0.3$ 时，$\nabla\cdot\mathbf{u}$ 的相对误差小于 $\sim 10\%$，Boussinesq 近似可安全使用。典型的室内自然对流 $\mathrm{Ma} \sim 10^{-5}$，近似精度极高。

---

## 7. 无量纲化与关键无量纲数

将 Boussinesq 方程无量纲化，取特征长度 $L$、速度 $U$、温差 $\Delta T$，定义：

$$
\mathbf{x}^* = \frac{\mathbf{x}}{L},\quad \mathbf{u}^* = \frac{\mathbf{u}}{U},\quad
t^* = \frac{tU}{L},\quad \pi^* = \frac{\pi}{U^2},\quad \theta^* = \frac{\theta}{\Delta T}.
$$

代入得到无量纲 Boussinesq 方程：

$$
\begin{aligned}
\nabla^*\cdot\mathbf{u}^* &= 0, \\
\frac{D\mathbf{u}^*}{Dt^*} &= -\nabla^*\pi^* + \frac{1}{\mathrm{Re}}\nabla^{*2}\mathbf{u}^* + \frac{\mathrm{Gr}}{\mathrm{Re}^2}\,\theta^*\mathbf{k}, \\
\frac{D\theta^*}{Dt^*} &= \frac{1}{\mathrm{Re}\,\mathrm{Pr}}\nabla^{*2}\theta^*.
\end{aligned}
$$

### 关键无量纲数

| 符号 | 名称 | 定义 | 物理意义 |
|:---|:---|:---|:---|
| $\mathrm{Re}$ | Reynolds 数 | $UL/\nu$ | 惯性力与粘性力之比 |
| $\mathrm{Pr}$ | Prandtl 数 | $\nu/\kappa$ | 动量扩散与热扩散之比 |
| $\mathrm{Gr}$ | Grashof 数 | $g\beta\Delta T L^3/\nu^2$ | 浮力与粘性力之比 |
| $\mathrm{Ra}$ | Rayleigh 数 | $\mathrm{Gr}\,\mathrm{Pr} = g\beta\Delta T L^3/(\nu\kappa)$ | 浮力驱动强度；$\mathrm{Ra} > \mathrm{Ra}_c$ 时对流起振 |
| $\mathrm{Ri}$ | Richardson 数 | $\mathrm{Gr}/\mathrm{Re}^2 = g\beta\Delta T L/U^2$ | 浮力与惯性力之比；$\mathrm{Ri} \gg 1$ 时浮力主导 |
| $\mathrm{Pe}$ | Péclet 数 | $\mathrm{Re}\,\mathrm{Pr} = UL/\kappa$ | 对流输运与扩散输运之比 |
| $\mathrm{Nu}$ | Nusselt 数 | $hL/k$ | 实际传热与纯导热之比（诊断量） |

> [!note] Ra 与 Pr 的联合作用
> - **高 $\mathrm{Ra}$**（$>10^6$）：湍流对流，热羽流主导传热，$\mathrm{Nu} \propto \mathrm{Ra}^{1/3}$。
> - **低 $\mathrm{Ra}$**（$\sim 10^3$）：层流对流，规则的胞状结构。
> - **$\mathrm{Pr} \ll 1$**（液态金属）：热扩散快，温度场光滑而速度场仍可湍流。
> - **$\mathrm{Pr} \gg 1$**（硅油、地幔）：动量扩散远快于热扩散，惯性效应弱，$\mathrm{Re}$ 通常很小。

---

## 8. 常见变体

### 8.1 双扩散系统（温盐对流）

在海洋中，温度和盐度共同决定密度：

$$
\frac{\rho'}{\rho_0} = -\beta_T\theta + \beta_S S', \qquad
b = g(\beta_T\theta - \beta_S S'),
$$

需额外增加盐度扩散方程：

$$
\frac{\partial S'}{\partial t} + \mathbf{u}\cdot\nabla S' = \kappa_S\nabla^2 S'.
$$

由于 $\kappa_S \ll \kappa_T$（热扩散约为盐扩散的 100 倍），形成**盐指**（salt fingers）和**双扩散阶梯**等丰富现象。

### 8.2 含背景分层

引入平均密度廓线 $\bar{\rho}(z)$，浮力频率（Brunt–Väisälä 频率）为：

$$
N^2(z) = -\frac{g}{\rho_0}\frac{d\bar{\rho}}{dz}.
$$

能量方程中温度扰动与背景梯度耦合：

$$
\frac{D\theta}{Dt} + w\frac{d\bar{T}}{dz} = \kappa\nabla^2\theta,
$$

其中 $w = \mathbf{u}\cdot\mathbf{k}$ 为垂直速度分量。$N^2 > 0$ 对应稳定层化（扰动振荡），$N^2 < 0$ 对应静力不稳定（对流）。

### 8.3 非弹性近似（Anelastic Approximation）

当垂直尺度与密度标高可比（如整个对流层），密度变化不可忽略。Ogura & Phillips (1962) 提出：

$$
\nabla\cdot(\bar{\rho}(z)\mathbf{u}) = 0,
$$

保留背景密度分层对质量通量的约束，同时仍滤除声波。适用于深层大气对流、恒星内部对流。

---

## 9. 典型应用场景

### 9.1 Rayleigh–Bénard 对流

**经典问题**：两水平平板间，下板加热（$T_h$）、上板冷却（$T_c$），温差 $\Delta T = T_h - T_c$ 驱动对流。

- **临界 $\mathrm{Ra}_c$**：当 $\mathrm{Ra} > \mathrm{Ra}_c \approx 1708$（两侧固壁、无滑移），静止传导解失稳，对流起振。
- **流态转捩**：
  - $\mathrm{Ra} \lesssim 10^4$：稳态二维滚胞
  - $10^4 \lesssim \mathrm{Ra} \lesssim 10^6$：三维稳态 / 振荡流
  - $\mathrm{Ra} \gtrsim 10^6$：湍流对流（热羽流 + 大尺度环流 LSC）
- **Nusselt 数标度律**：$\mathrm{Nu} \propto \mathrm{Ra}^\gamma \mathrm{Pr}^\delta$
  - 经典湍流区：$\gamma \approx 1/3$（Malkus, 1954; Grossmann & Lohse, 2000）
  - 终极区（$\mathrm{Ra} \gtrsim 10^{14}$）：$\gamma \to 1/2$（Kraichnan, 1962）

> [!example] 实验参数估算
> 室温（$T_0 \approx 300\,\mathrm{K}$）下，$L = 0.1\,\mathrm{m}$ 的水层（$\mathrm{Pr} \approx 7$），$\Delta T = 10\,\mathrm{K}$：$\mathrm{Ra} \approx 2.3 \times 10^7$，已进入湍流区间。

### 9.2 大气边界层

白天日照加热地面 → 近地空气升温 → 热力对流（热泡 thermal）：

- **对流边界层（CBL）**：浮力为主，湍流混合强烈，位温廓线近均匀，$\mathrm{Ri} \ll 1$。
- **稳定边界层（SBL）**：夜间地面辐射冷却，浮力抑制湍流，临界 $\mathrm{Ri} \approx 0.25$。
- **Monin–Obukhov 相似理论（MOST）**：
  $$
  \zeta = \frac{z}{L_\mathrm{MO}}, \qquad
  L_\mathrm{MO} = -\frac{u_*^3}{\kappa_v g\,\overline{w'\theta'}_s / \bar{\theta}},
  $$
  其中 $L_\mathrm{MO}$ 为 Obukhov 长度，$\kappa_v \approx 0.4$ 为 von Kármán 常数。$|\zeta| \ll 1$ 为自由对流区，$\zeta \gg 1$ 为近中性剪切主导区。

气象 LES 模式（如 PALM、WRF-LES）广泛使用 Boussinesq 近似。

### 9.3 海洋内波与混合

层化海洋中，扰动偏离平衡密度面产生回复力 → **内重力波**：

- 色散关系：$\omega^2 = N^2 \dfrac{k_h^2}{k_h^2 + k_z^2}$，频率上限为浮力频率 $N$（典型值 $N \sim 10^{-3}$–$10^{-2}\,\mathrm{s}^{-1}$，周期数分钟至数小时）。
- 内波破碎 → 湍流混合 → 驱动大洋经向翻转环流（MOC），是全球气候系统的关键过程。
- 数值模式（MITgcm、ROMS）的非静力 Boussinesq 选项直接求解上述方程。

### 9.4 建筑通风与室内环境

- **置换通风**：冷风从地板送入，热源（人、设备）驱动热羽流上升，形成分层流场。
- **火灾烟气运动**：火源上方强浮力羽流，Boussinesq 近似适用于远离火源的中远场（$\Delta T/T_0 \lesssim 0.1$）；近火源高温区需变密度模型。
- **洁净室设计**：层流 + 热浮力效应，通过 Ra 预测流态转捩。

### 9.5 地幔对流

地球地幔在百万年尺度上表现为高黏度流体（$\mathrm{Pr} \sim 10^{23}$）：

- $\mathrm{Ra} \sim 10^7$，惯性项完全可忽略（$\mathrm{Re} \to 0$），动量方程退化为 Stokes 方程：
  $$
  0 = -\nabla\pi + \nu\nabla^2\mathbf{u} + g\beta\theta\,\mathbf{k},
  $$
  即"无限 Prandtl 数"极限。
- Boussinesq 近似是地幔对流数值模拟（如 ASPECT、CitcomS）的标准假设。

### 9.6 晶体生长与材料加工

Czochralski 法生长单晶硅：熔体中温度梯度驱动浮力对流 → 影响掺杂均匀性和晶体缺陷分布。工业 CFD 多基于 Boussinesq 近似快速迭代工艺参数。

---

## 10. 近似失效与扩展方案

| 失效情形 | 原因 | 替代方案 |
|:---|:---|:---|
| 大温差 $\Delta T/T_0 > 0.1$ | 状态方程非线性显著，$\rho'/\rho_0$ 不再 $\ll 1$ | 完全可压缩 / 低温 Boussinesq 修正 |
| 垂直尺度 $\sim H_\rho$ | 背景密度分层不可忽略 | 非弹性近似（Anelastic） |
| $\mathrm{Ma} > 0.3$ | 压缩功和声波不可忽略 | 完全可压缩 Navier-Stokes |
| 燃烧 / 化学反应 | 组分剧烈变化→密度变化大 | 低马赫数变密度方程 |
| 近临界流体 | $\beta$ 发散 → 浮力异常放大 | 完整状态方程（如 Peng–Robinson） |

> [!warning] 判断流程
> 1. 计算 $\mathrm{Ma} = U/c_s$：若 $>0.3$，不可用 Boussinesq。
> 2. 计算 $\Delta\rho/\rho_0$：若 $>0.1$，需考虑变密度效应。
> 3. 计算 $L_z/H_\rho$：若 $>0.1$，需引入背景分层或非弹性近似。

---

## 11. 数值实现要点

### 11.1 时间步进

Boussinesq 方程滤除了声波，CFL 条件由对流速度决定：$\Delta t < \mathrm{CFL} \cdot \Delta x / |\mathbf{u}|_{\max}$，而非声速 $c_s$。与完全可压缩求解器相比，时间步长可大 $10^2$–$10^3$ 倍。

### 11.2 压力-速度耦合

不可压缩约束 $\nabla\cdot\mathbf{u}=0$ 使压力成为 Lagrange 乘子，每步需解 Poisson 方程：

$$
\nabla^2\pi = \nabla\cdot(-\mathbf{u}\cdot\nabla\mathbf{u} + \nu\nabla^2\mathbf{u} + b\mathbf{k}).
$$

常用投影法（Chorin, 1968）或 SIMPLE/SIMPLER/PISO 系列算法。

### 11.3 常用开源代码

| 代码                                           | 方法       | 典型场景          |
| :------------------------------------------- | :------- | :------------ |
| **Nek5000**                                  | 谱元法      | 高精度 RB 对流 DNS |
| **AFiD**                                     | 交错网格有限差分 | RB 对流（GPU 加速） |
| **MITgcm**                                   | 有限体积     | 海洋 / 大气多尺度    |
| **OpenFOAM** (`buoyantBoussinesqPimpleFoam`) | 有限体积     | 工程对流换热        |
| **Dedalus**                                  | 谱方法      | 理想化地球物理流体     |
| **PALM**                                     | 有限差分 LES | 大气 / 城市边界层    |

---

## 12. 历史注记

Joseph Valentin Boussinesq 于 1903 年在其著作 *Théorie analytique de la chaleur* 中首次系统阐述了这一近似。Oberbeck (1879) 率先独立推导了类似方程组，故有时亦称 **Oberbeck–Boussinesq 近似**。Spiegel & Veronis (1960) 和 Mihaljan (1962) 从低马赫数渐近展开给出了严格的数学论证，确立了近似的适用范围。

---

*扩展阅读：* [[Navier-Stokes方程]] | [[无量纲数（Re, Ra, Pr）]] | [[热对流稳定性分析]] | [[Rayleigh-Bénard对流]] | [[大气边界层]] | [[非弹性近似]]

#Boussinesq #流体力学 #近似推导 #浮力驱动流 #热对流 #计算流体力学
