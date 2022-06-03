> Haricharan
# Signals and Systems
## 3rd May

### Signal
#### Some definitions:
*Signal:* Mathematical function that depends on some variables

**Classification**
- Continuous or Discrete time
- Digital or analog signal: has to do with the amplitude of the signal
	- Digital: amplitude can take discrete values. With "M" different values, it's called an M-ary signal
	- Analog: amplitude can take any value
- Even or odd signal
- Conjugate symmetry x(t) = x*(t)
	- Real part is even, Imaginary part is odd
- Periodic and aperiodic:
	- x(t) = x(t + T0), $\omega =  \frac{2 \pi}{T_0}$
	- x[n] = x[n + N], $\Omega = \frac{2 \pi}{N}$
- Causal Signal:
	- x(t) = 0 for t < 0
	- Anticausal: x(t) = 0 for t >= 0
- Deterministic or Random
	- Deterministic can be predicted
	- Random cannot be predicted

#### Power and Energy
For current and resistor:

$$P(t) = i(t) v(t)$$
$$E = \int_{t_1}^{t_{2}}P(t) dt$$
Analogously, for any signal x(t):
$$P(t) = |x(t)|^2$$
$$E = \int_{t_1}^{t_{2}}|x(t)|^{2}dt$$
$$P_{\text{avg}} = \frac{E}{t_{2}- t_1}$$

![](../Images/Pasted%20image%2020220504145648.png)

---
If energy is finite, power is zero and is called **energy signal**.
Eg. 
1. x(t) is 1 if 0 < t < 1, 0 otherwise
$$E_{\infty} = 1, P_{\infty} = 0$$
If energy is infinite, power is finite, it is called **power signal**
Eg. 
2. x[n] = 2 for all n

$$P_{\infty} = 4, E_{\infty} = \infty$$
We can have neither power nor energy signal also (Ramp signal).
Eg. 
3. x(t) = t

$$E_{\infty} = \infty, P_{\infty} = \infty$$
---
#### Signal Transformation

**Time shifting**

x(t) -> x(t - T)
T units delayed

x(t) -> x(t + T)
T units advanced

Eg.
![500](../Images/Pasted%20image%2020220504201147.png)

**Time Scaling**

**CT**
- x(a t) squishes the signal by a times
- x(t / a) stretches the signal by a times
- x(-t) -> reflection about y axis

**DT:**
- x (at) squishes the signal, but they are losing information. For eg, x \[3 n]: x[1], x[2], x[4], x[5], x[6], etc. are thrown away.
- x (at) stretches the signal. For eg, x[n/2] would stretch the signal.
	- However, what do we do for intermediate values? We *Interpolate* the signal.

**Amplitude Scaling**:
- Stretch about y axis
- - x(t) flip about x axis

#### Elementary Signals
---
**1. Exponential**

$\bar A e^{\bar s t} = A e^{j \phi} e^{(\sigma + j \omega)t}$
$\bar s$ -> complex frequency

Real Signal = x(t) + x*(t)
Imaginary Signal = x(t) - x*(t)

s can be thrown into the complex plane

Depending on sign of $\sigma$:
- Anything in the left-half plane is decaying exponential
- Anything on imaginary axis is neither growing nor decaying, i.e. it is pure sinusoid
- Anything on right half plane is growing exponential
---
**2. Unit step function or heavyside step function**
CT: u(t) = 1 for t > 0, 0 for t < 0
DT: u[n] = 1 for t $>=$ 0, 0 for t < 0

- Make any signal into a causal signal: x(t) u(t) is causal.
- Gating:
![](../images/Pasted%20image%2020220504212454.png)
---
**3. Unit impulse or Unit Delta or Dirac delta function: a generalized function**

- $\delta(x) = \delta(-x)$
- Sifting property: $\int_{- \infty} ^{\infty} f(t) \delta(t - T) dt = f(T)$
---
**4. Unit Ramp function**
r(t) = t u(t)

$\delta(t) = \frac{d u(t)}{dt} = \frac{d^{2} r(t)}{d t^{2}}$
---

### System
#### Continuous Time System
Input Signal -> System -> Output Signal
     x (t)                                     y(t)

Eg. Some electric Circuit:
![600](../Images/Pasted%20image%2020220504141625.png)

$V_s = x(t)$
$$i = \frac{V_s - V_{c}}{R} = C \frac{d V_{c}}{d t}$$
$$\frac{d V_{c}}{dt}+ \frac{V_{c}}{RC} = \frac{V_s}{RC}$$

Eg. Cart: This is similar to cart with friction: x(t) is the external force, a y(t) corresponds to friction.
$$\frac{d y(t)}{dt} + a y(t) = b x(t)$$
This is first-order system!

---
#### Discrete Time system
Input Signal -> System -> Output signal
      x[n]                                     y[n]
$n = 0, \pm 1, \pm 2, ...$

Eg. Bank monthly balance:
- y[n] is monthly balance
- x[n] is net amount deposited = Deposit - Withdrawal
- 1% Interest also

$$y[n] = x[n] + 1.01 y [n-1]$$
This is a difference equation

Eg. For the same cart, it can be represented as DT also, where time would be like $\Delta n$.

$\frac{d y(t)}{dt} + a y(t) = b x(t)$ becomes

$$ \frac{v[n] - v[n-1]}{\Delta n} + \frac{\rho v[n]}{m} = \frac{f[n]}{m}$$
---
**For CT-> Differential equation, For DT-> Difference equation**

> [!INFO] Imp
> If we come up with methods to solve one class of system, we can do same thing for other systems in same class.

---
#### Classification of systems
Interconnection of subsystems, devices, to transform input into output
- CT and DT systems
- Systems with and without memory
	- Without memory:
		- Resistor system: v(t) = i (t) R
		- Output depends only on present value
	- With memory:
		- Depends on present/future
		- It "stores" energy!
		- capacitor system: $v(t) = \frac{\int_{- \infty} ^{t} i(t) dt}{C}$ 
		- summer: $y[n] = \sum_{k = - \infty}^{n} x[k]$ -> computes running average
- Invertible and non-invertible
	- Invertible: If there exists S2 for S1, such that x(t) -> S1 -> y(t) -> S2 -> x(t), S1 is said to be invertible
		- Eg. y(t) = 2 x(t)
	- Non-invertible
		- Eg. y(t) = 0
- Causal and Non-causal *system* (*not signal*)
	- Causal:
		- Output at any time depends on values from present or past times *not future*
		- Eg: y(t) = x(t) cos (t + 1)
	- Non-causal
		- Eg. y[n] = x[n] - x[n + 1]
- Stability
	- Stable system:
		- Small input leads to responses which do not diverge
		- If |x(t)| < $B_x$ < $\infty$  implies |y(t)| < $B_y$ < $\infty$
		- BIBO -> Bounded input, bounded output
- Time invariance
	- Time invariant: If behaviour and characteristics do not vary with time
		- $x(t) \rightarrow y(t) \implies x(t - T_{0})\rightarrow y(t - T_0)$ 
		- x(t) -> S -> Delay -> y(t - $T_0$) = x(t) -> Delay -> x(t - $T_0$) -> S -> y(t - $T_0$)
		- Eg. y(t) = sin (x(t)) 
		- No explicit time dependence
	- Time variant
		- Eg. y(t) = n (x(t))
		- Explicit Time dependence
- Linearity
	- Linear system:
		- a x1(t) + b x2(t) -> S -> a y1 (t) + b y2(t)
		- Eg. y(t) = t x(t)
	- Non-linear
		- Eg. y(t) = m x(t) + c

**We're worried only about LTI systems in this course.**

## 11th May

Convolution of two functions:
$x[n] * y[n] = \sum_{k = -\infty} ^{\infty} x[k] y[n - k]$

Imagine a DT system that is linear

**Sifting property**
$$\sum_{- \infty} ^{\infty} x[k] \delta[n - k] = x[n]$$
Consider LTI system
- x[k] -> S -> y[k]
- $\delta [n - k]$ -> S -> $h_{k}[n] = h[n - k]$
- $x[n] = \sum_{-\infty}^{\infty} x[k] \delta[k] \rightarrow \sum_{-\infty}^{\infty} x[k] h[n - k] = y[n]$
This is called the superposition sum or convolution sum -> $y[n] = \sum_{-\infty}^{\infty} x[n] h[n - k]$
where $h[n]$ is the unit impulse response.

$y[n] = x[n] * h[n]$

**CT LTI system**

> [!note] Wow!
> The response of the system is determined by unit impulse response
> - We can give an unit impulse, see what it does, then convolve x[n] to figure out y[n]!

$\delta_{\Delta} (t - k_{0}) \rightarrow h_{k \Delta} (t)$
$x(t) = \sum_{-\infty} ^{\infty} x(k \Delta) \delta_{\Delta} (t - k_{0})\Delta$
$$\int_{-\infty} ^{\infty} x(\tau) \delta (t - \tau) d \tau = x(t)$$

Using Linearity: 
$\sum_{\infty} ^{\infty} x(k \Delta) \delta_{\Delta} (t - k) \rightarrow \sum_{\infty} ^{\infty} x(k \Delta) h_{k \Delta} (t)$

Using time invariance:
$$y(t) = \int_{-\infty} ^{\infty} x(\tau) h(t - \tau) d \tau = x(\tau) * h(t)$$

## 17th May

**Properties:**
- **Commutative property**
**x[n] * h[n] = h[n] * x[n]**

$y[n] = \sum_{-\infty} ^{\infty} x[k] x[n - k] = \sum_{-\infty} ^{\infty} x[n - k] x[k]$
(Property of reversing summation)

-** Distributive property
$x[n] * (h_1[n] + h_2[n]) = x[n] * h_1[n] + x[n] * h_2[n]$**
Proof: $y[n] = \sum_{- \infty} ^{\infty} x[k] (h_{1} [n - k] + h_{2}[n- k]) = = \sum_{- \infty} ^{\infty} x[k] h_{1}[n - k] + \sum_{-\infty}^{\infty} x[k] h_{2}[n - k] = y_1[n] + y_2[n]$
-**Associative property**
$(x[n] * h1[n]) * h2[n] = x[n] * (h1[n] * h2[n])$

x(t) -> S1 -> y1(t) -> S2 -> y2(t)
$\delta[n] \rightarrow h_1[n]$, $\delta[n] \rightarrow h_2[n]$

Using commutativity, 
$(x[n] * h_1[n]) * h_2[n] = (x[n] * h_2[n]) * h_1[n]$
If we're passing a signal x(t) through many LTI systems, order doesn't matter.

-**For memoryless systems**
$h[n] = A \delta [n]$
$y[n] = \sum_{- \infty} ^{\infty} x[k] A \delta [n - k] = A x[n]$

-**Invertibility**
$x[n] * (h_1[n] * h_{2}[n])= x[n] = x[n] * \delta[n]$
$\implies h_{1}[n] * h_{2}[n] = \delta[n]$

-**Causality**
$h[n] < 0 \hspace{5 px} \text{for} \hspace{5 px}n < 0$
Reason-> Unit impulse function is 0 for n < 0, so as it is causal, unit impulse response is also 0 for n < 0

-**Stability**
Consider giving a Bounded input x[n] < B.
$y[n] = \sum_{- \infty} ^{\infty} x[k] h[n - k] < B \sum_{\infty} ^{\infty} |h[k]|$
$\sum\limits_{-\infty}^{\infty} |h[k]| < \infty$

## 18th May

#### Unit Step Response:
u(t) -> System -> s(t)

s(t) = u(t) * h(t)
       = h(t) * u(t)

s[n] = h[n] * u[n]
       = $\sum_{- \infty} ^{\infty} h[k] u[n - k]$
       = $\sum_{- \infty} ^{n} h[k]$

h[n] = s[n] - s[n - 1]

$s(t) = \int_{-\infty} ^{\infty} u(t - \tau) h(\tau) d \tau = \int_{- \infty} ^{t} h(\tau) d \tau$
$h(t)= \frac{d s(t)}{d t}$

## 19th May

> [!important] FOURIER LESGOO
> Lesgoo

**CT system**
$x(t) = e^{s t}$
$y(t) = \int_{- \infty} ^{\infty} h(\tau) e^{s(t - \tau)} d \tau = e^{-st} \int_{- \infty} ^{\infty} h(\tau) e^{- s \tau} d \tau = e^{st} H(s)$

$e^{st}$ -> Eigenfunction of system
H(s) -> Eigenvalue of the system

**DT system**
$x[n] = z^n$
$y[n] = \sum_{- \infty} ^{\infty} h[k] z^{n}z^{-k} = z^{n} \sum_{-\infty} ^{\infty} h[k] z^{-k}$
$z^n$ is the Eigenfunction of system
$H(z)$ is Eigenvalue of system

If I can decompose x(t):
$x(t) = \sum_{-\infty} ^{\infty} a_{k}e^{s_{k} t} \rightarrow \sum_{- \infty} ^{\infty} a_{k}H(s_{k}) e^{sk}$

**For real functions**
- Synthesis equation
$$x(t) = \sum_{-\infty} ^{\infty}  a_{k}e^{j  w_{o} t}$$
- Analysis equation
$$a_{k}= \frac{\int_{0}^ {T} x(t) e^{- j k w_{o}t}}{T}$$

$x(t) = a_{o}+ \sum_{k = 1} ^{\infty} (2 B_{k} \cos (w_{o} k t) - 2 C_{k} \sin (w_{o} k t)) = a_{o} + 2 A_{k} \cos (w_{o}k t + \theta_k)$

**Dirichlet conditions for convergence:**
- Over a period, $\int_{T} |x(t)| dt < \infty$
- Finite maxima and minima
- Finite interval of time -> Finite number of discontinuities

## May 24
#### Properties of Fourier series

- **Linearity:** $a x(t) + b y(t) \leftrightarrow a a_k + b b_k$
Proof: Just throw this into the integral and separate stuff
- **Time shifting:** $x (t - t_{0}) \leftrightarrow a_{k}e^{- j k w_{0} t_{0}}$
Proof: $a_{k'}= \frac{1}{T} \int_{- \frac{T}{2}}^{\frac{T}{2}} x(t - t_{0}) e^{- k w_{0}t} dt = \frac{1}{T} \int_{- \frac{T}{2}}^{\frac{T}{2}}$
- **Frequency Shifting:** $e^{j M w_{0} t} x(t) \leftrightarrow a_{k - M}$
- **Conjugate Input:** $x^ *(t) \leftrightarrow a_{- k} ^ *$
- **Time reversal:** $x(-t) \leftrightarrow a_{- k}$
Just integrate and substitute
- **Time Scaling:** $x(a t) \leftrightarrow a_k$
![400](../Images/Pasted%20image%2020220524111422.png)
- **Differentiation:** $\frac{d x(t)}{d t} \leftrightarrow j k w_{0} a_k$
- **Integration:** $\int_{- \infty} ^{\infty} x(t) \leftrightarrow \frac {a_{k}} {j k w_0}$
- **Conjugate symmetry for real x(t):** $a_{k}= a_{- k} ^ *$
- **Fourier Series of x(t) y(t)**
$c_{n} = a_{n}* b_{n}$

**Parseval's Theorem:**
Power = $\sum_{k = - \infty} ^ {\infty} |a_k|^2$

## May 26
#### Filter Design and Analysis

- Frequency reshaping
- Frequency selecting

![400](../Images/Pasted%20image%2020220526221701.png)
**Taking output over $V_c$, we get low pass filter!**
$RC \frac{d V_o}{dt} + V_o = V_i$

$RC j w H(j w) e^{j w t} + H(jw) e^{j w t}  = e^{j w t}$
$H(jw) = \frac{1}{1 + R C j w}$

$|H(jw)| \text{  vs  } w$
![400](../Images/Pasted%20image%2020220526081850.png)

$\angle H(jw) \text{  vs  } w$
![400](../Images/Pasted%20image%2020220526082128.png)

**Taking output over $V_r$ we get High pass filter,
$V_{r}= V_{s} - V_{c} = V_{i} - H(s) V_{i}= (1 - \frac{1}{1 + R C j w})V_{i}$

$H(jw) = \frac{j w R C}{1 + j w R C}$

$|H(jw)| \text{  vs  } w$
![](../Images/Pasted%20image%2020220526083348.png)

$\angle H(jw) \text{  vs  } w$
![](../Images/Pasted%20image%2020220526083913.png)

## June 6
#### Continuous time Fourier transform
- A aperiodic signal is periodic with $T \rightarrow \infty$
- $w \rightarrow 0$

$\tilde x(t) = \sum_{-\infty} ^{\infty} a_{k}e^{j k w_{0}t}$
$a_{k}= \frac 1T \int_{- \infty} ^ {\infty} \tilde x(t) e^{- j k w_{0} t} dt$
Spectrum$= a_k T = X(jk w_{0}) = \int_{- \infty} ^{\infty} x(t) e^{- j k w_{0}t} dt$
$\tilde x(t) = \frac {1}{2 \pi} \sum_{-\infty} ^{\infty} X(j k w_{0}) e^{j k w_{0}t} w_{0}= \frac{1}{2 \pi} \int_{- \infty} ^{\infty} X(j w) e^{j w t} dw = x(t)$

> [!important] FOURIER TRANSFORM FORMULAE
> **Fourier transform**
> $X(jw) = \int_{- \infty} ^{\infty} x(t) e^{- j w t} dt$
> **Inverse Fourier Transform**
> $x(t) = \frac{1}{2 \pi} \int_{- \infty} ^{\infty} X(j w) e^{j w t} dw$

> [!tip] AWESOME DUAL
> Rectangular pulse in time domain -> Sinc in frequency domain
> $X(jw) = \frac {2}{\omega} \sin(w T)$
> Rectangular pulse in frequency domain -> Sinc in time domain
> $x(t) = \frac{1}{\pi t} \sin(W t)$

## June 2
- $x(t) \leftrightarrow X(jw)$
- $y(t)\leftrightarrow Y(jw)$
- $h(t) \leftrightarrow H(jw)$

$$Y(jw) = \int_{-\infty} ^{\infty} \int_{-\infty} ^{\infty} x(\tau) h(t - \tau) d \tau e^{- j w t} dt = \int_{- \infty} ^{\infty} x(\tau) \left(\int_{\infty} ^{\infty} h(t - \tau) e^{- j w t} dt\right) d\tau$$
$$Y(jw) = \int_{- \infty} ^{\infty} x(\tau) e^{- j w \tau} H(jw) d \tau = H(jw) X(jw)$$

To get output from a system, multiplication is easier than convolution, so we can take Fourier transforms of h(t) and x(t), multiply, then take inverse Fourier transform to get y(t)

#### Properties
1. Linearity $a x_{1}+ b x_{2}\leftrightarrow a{X_1(jw)}+ b{X_2(jw)}$
2. Time shifting $x(t - t_{0})\leftrightarrow e^{- j w t_{0}} X(jw)$
3. Frequency Shifting $e^{j w t_{0}}x(t) \leftrightarrow X(w - w_0)$
4. Conjugation
$x^*(t) = X^*(- j w)$
5. Time and frequency scaling
$x(at) = \frac{X(\frac{jw}{a})}{|a|}$
6. Time reversal 
x(-t) <-> X(- j w)
7. Convolution
$x(t) * y(t) \leftrightarrow X(jw) Y(jw)$
8. Multiplication
x(t) y(t) <-> $\frac{1}{2 \pi} \int_{- \infty}^{\infty} X(j \theta) Y(j (w - \theta)) d \theta$
9. Differentiation $\frac{d x(t)}{dt} \leftrightarrow j w X(jw)$
10. Integration $\int_{- \infty} ^{t} x(t) dt \leftrightarrow \frac{X(jw)}{j w} + \pi X(0) \delta (w)$
11. Differentiation in frequency domain $t x(t) \leftrightarrow j \frac{d X(jw)}{d w}$
12. Conjugate symmetry for real signal x(t)
$X(jw) = X^*(- jw)$
Real parts are equal
Imaginary parts are negatives of each other

Fourier transform of periodic function
$X(jw) = \sum_{k = -\infty} ^{\infty} 2 \pi a_{k}\delta (w - w_0)$
