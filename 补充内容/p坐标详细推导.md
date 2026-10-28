我们一步步从最基础的高坐标系（`z`坐标）推导到气象上最常用的**气压坐标系**（`p`坐标系）。这个过程的核心是利用静力平衡，将垂直坐标从几何高度 `z` 替换为气压 `p`。

---

### 1. 为什么需要 p 坐标系？
在 `z` 坐标系中，密度 `ρ` 时刻变化，连续方程非常复杂，不容易过滤声波。而大气近似满足**静力平衡**，气压 `p` 随高度单调递减，因此可以用 `p` 作为垂直坐标。这样做最大的好处是：
- **连续方程变成线性诊断方程**，形式上像不可压缩流体；
- **气压梯度力变成位势梯度**，避开了密度；
- 便于等压面分析和等熵分析。

---

### 2. 坐标变换的数学准备
假设大气满足静力平衡：
$$\frac{\partial p}{\partial z} = -\rho g \tag{1}$$
因为 `p` 随 `z` 严格单调递减，我们可以把因变量和自变量从 `(x,y,z,t)` 转换到 `(x,y,p,t)`。
在 `p` 坐标系中，几何高度 `z` 变成了一个依赖变量，通常用**位势** `Φ = gz` 代替，`Φ(x,y,p,t)` 就描述了等压面的起伏。

对于任意场变量 `A`，在两种坐标下表示：
- `z` 坐标：`A = A(x,y,z,t)`
- `p` 坐标：`A = A(x,y,p(x,y,z,t), t)`

我们的目标是把 `z` 坐标中的偏导数用 `p` 坐标中的偏导数表达出来。

#### 水平梯度转换
在 `z` 坐标中对 `x` 的偏导数（保持 `z` 不变）写作 `(∂A/∂x)_z`。在 `p` 坐标中，我们要的是等压面上的导数 `(∂A/∂x)_p`。利用链式法则：
$$\left( \frac{\partial A}{\partial x} \right)_z = \left( \frac{\partial A}{\partial x} \right)_p + \frac{\partial A}{\partial p} \left( \frac{\partial p}{\partial x} \right)_z \tag{2}$$
这个式子暂时还用不上，我们需要的是反过来用 `(∂A/∂x)_p` 表示 `(∂A/∂x)_z`。由 (2) 移项：
$$\left( \frac{\partial A}{\partial x} \right)_p = \left( \frac{\partial A}{\partial x} \right)_z - \frac{\partial A}{\partial p} \left( \frac{\partial p}{\partial x} \right)_z \tag{3}$$

但我们手头往往知道 `z` 坐标的方程，里面会出现 `(∂p/∂x)_z`。更直接的办法是利用隐函数关系：
在等压面上，`p(x,y,z,t) = const`，所以对该面求水平微分得：
$$\left( \frac{\partial p}{\partial x} \right)_z + \frac{\partial p}{\partial z} \left( \frac{\partial z}{\partial x} \right)_p = 0$$
即：
$$\left( \frac{\partial p}{\partial x} \right)_z = - \frac{\partial p}{\partial z} \left( \frac{\partial z}{\partial x} \right)_p \tag{4}$$
代入静力平衡 (1) `∂p/∂z = -ρg`，得到：
$$\left( \frac{\partial p}{\partial x} \right)_z = \rho g \left( \frac{\partial z}{\partial x} \right)_p = \rho \left( \frac{\partial \Phi}{\partial x} \right)_p \tag{5}$$
同理，`y` 方向有：
$$\left( \frac{\partial p}{\partial y} \right)_z = \rho \left( \frac{\partial \Phi}{\partial y} \right)_p$$

**结论：z 坐标中的水平气压梯度力可以直接用 p 坐标中的位势梯度代替。**

---

### 3. 运动方程的转换
忽略摩擦的 `z` 坐标水平动量方程（矢量形式）：
$$\frac{d\mathbf{V}}{dt} + f\mathbf{k} \times \mathbf{V} = -\frac{1}{\rho} \nabla_z p \tag{6}$$
其中 `∇_z` 是保持 `z` 不变的梯度算子，`\mathbf{V} = (u,v)` 是水平风。

将 (5) 代入 (6) 的右边：
$$-\frac{1}{\rho} \nabla_z p = -\frac{1}{\rho} \cdot \rho \nabla_p \Phi = -\nabla_p \Phi \tag{7}$$
所以 **p 坐标下的水平动量方程**为：
$$\frac{d\mathbf{V}}{dt} + f\mathbf{k} \times \mathbf{V} = -\nabla_p \Phi \tag{8}$$
这里物质导数变为：
$$\frac{d}{dt} = \left( \frac{\partial}{\partial t} \right)_p + u \left( \frac{\partial}{\partial x} \right)_p + v \left( \frac{\partial}{\partial y} \right)_p + \omega \frac{\partial}{\partial p} \tag{9}$$
其中 **p 坐标垂直速度**定义为：
$$\omega \equiv \frac{dp}{dt} \tag{10}$$

---

### 4. 静力方程在 p 坐标下的形式
由 `Φ = gz`，对 `p` 求导：
$$\frac{\partial \Phi}{\partial p} = g \frac{\partial z}{\partial p} = g \cdot \frac{1}{\partial p/\partial z} = \frac{g}{-\rho g} = -\frac{1}{\rho} \tag{11}$$
即 p 坐标的静力方程：
$$\frac{\partial \Phi}{\partial p} = -\frac{1}{\rho} \quad \text{或} \quad \frac{\partial \Phi}{\partial p} = -\alpha \tag{12}$$
其中 `α = 1/ρ` 是比容。这与 `z` 坐标的 `∂p/∂z = -ρg` 完全等价。

---

### 5. 连续方程的转换 —— p 坐标的巨大优势
`z` 坐标的连续方程：
$$\frac{\partial \rho}{\partial t} + \nabla_z \cdot (\rho \mathbf{V}) + \frac{\partial (\rho w)}{\partial z} = 0 \tag{13}$$
使用拉格朗日方法推导更直接。考虑一个微小的空气块，质量 `δm = ρ δx δy δz`。在运动过程中质量守恒：
$$\frac{d(\delta m)}{dt} = 0 \tag{14}$$
在静力平衡下，`δp` 与 `δz` 的关系为 `δp = -\rho g δz`（忽略扰动与基本态的差别），因此：
$$\rho \delta z = -\frac{\delta p}{g}$$
于是质量元可写为：
$$\delta m = \rho \delta x \delta y \delta z = \delta x \delta y \left( -\frac{\delta p}{g} \right) = \frac{1}{g} \delta x \delta y (-\delta p)$$
（若定义 `p` 向上增加为正，则深度为 `-δp`，质量元为 `(1/g) δx δy δp`。更严谨地取 `δm = ρ |δz| δx δy = (1/g) δx δy |δp|`，因垂直坐标正向取向下时符号需统一。我们按常规取 `p` 向下减小，用 `-δp` 表示厚度。）

为简洁，令 `δp > 0` 表示气层厚度，则质量元为 `δm = \frac{1}{g} \delta x \delta y \delta p`。
质量守恒 `d(δm)/dt = 0` 展开为：
$$\frac{d}{dt} (\delta x \delta y \delta p) = 0$$
即：
$$\frac{1}{\delta x}\frac{d(\delta x)}{dt} + \frac{1}{\delta y}\frac{d(\delta y)}{dt} + \frac{1}{\delta p}\frac{d(\delta p)}{dt} = 0 \tag{15}$$
根据速度散度的几何意义，`(1/δx) d(δx)/dt = ∂u/∂x`，对 `y` 同理；对于垂直方向，`(1/δp) d(δp)/dt = ∂ω/∂p`（因为 `ω = dp/dt`，两等压面间 `δp` 的变化率由上下边界的 `ω` 差决定）。所以 (15) 直接给出：
$$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial \omega}{\partial p} = 0 \tag{16}$$
这就是 **p 坐标的连续方程**，注意所有导数都保持在等压面上。它的形式与不可压缩流体的连续方程完全相同，极为简洁。

> 若要从 `z` 坐标方程显式推导，需将 `w` 用 `ω` 和等压面变化表示，过程繁琐但结果一致。

---

### 6. 热力学能量方程
绝热条件下的热力学第一定律在 `z` 坐标下：
$$\frac{d\ln\theta}{dt} = 0 \quad \text{或} \quad \frac{dT}{dt} - \frac{1}{\rho C_p} \frac{dp}{dt} = 0$$
其中 `θ` 是位温。在 `p` 坐标中，`d/dt` 已包含 `ω ∂/∂p`，所以能量方程直接写成：
$$\frac{\partial \theta}{\partial t} + u\frac{\partial \theta}{\partial x} + v\frac{\partial \theta}{\partial y} + \omega \frac{\partial \theta}{\partial p} = 0 \tag{17}$$
或者用温度表示：
$$\frac{\partial T}{\partial t} + u\frac{\partial T}{\partial x} + v\frac{\partial T}{\partial y} - \omega \frac{R_d T}{C_p p} = 0 \quad \text{(对于干空气)}$$
其中使用了 `κ = R_d/C_p` 和 `Exner函数 Π = (p/p_0)^κ` 时，`- ω (T/θ) ∂θ/∂p` 可转化为 `ω κ T / p`，但注意静力稳定度的作用。更常用的形式是引入**静力稳定度参数** `σ = - (α/θ) ∂θ/∂p`，此处不展开。

---

### 7. p 坐标系完整方程组总结
对于干空气、绝热、无摩擦的大尺度运动：

1. **水平动量方程**  
   $$\frac{d\mathbf{V}}{dt} + f\mathbf{k} \times \mathbf{V} = -\nabla_p \Phi \tag{18}$$
2. **静力方程**  
   $$\frac{\partial \Phi}{\partial p} = -\frac{R_d T}{p} \quad \text{(用状态方程 } p = \rho R_d T \text{)} \tag{19}$$
3. **连续方程**  
   $$\nabla_p \cdot \mathbf{V} + \frac{\partial \omega}{\partial p} = 0 \tag{20}$$
4. **热力学方程**  
   $$\frac{d\theta}{dt} = 0 \quad \text{或} \quad \frac{dT}{dt} - \frac{\kappa T}{p}\omega = 0 \tag{21}$$
5. **状态方程**  
   $$p = \rho R_d T \quad \text{可内置于 } \Phi \text{ 与 } T \text{ 的积分关系}$$

边界条件：下边界（如1000 hPa）给定 `ω` 或与地形相关，上边界（`p→0`）`ω=0`。

---

### 8. ω 与 w 的关系（补充）
由 `ω = dp/dt` 以及全导数的展开：
$$\omega = \frac{\partial p}{\partial t} + \mathbf{V} \cdot \nabla_z p + w\frac{\partial p}{\partial z}$$
大尺度运动中，局地变化项和水平平流项通常比最后一项小一个量级，故有近似：
$$\omega \approx w\frac{\partial p}{\partial z} = -\rho g w \tag{22}$$
上升运动（`w>0`）对应 `ω<0`。

---

以上便是从 `z` 坐标系到 `p` 坐标系的完整推导。核心步骤是：利用静力平衡将气压梯度力转化为位势梯度，并用质量守恒导出极简连续方程，最终获得一套在天气和气候动力学中极为实用的方程组。