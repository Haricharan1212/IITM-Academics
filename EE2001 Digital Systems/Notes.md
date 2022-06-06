> Haricharan
# Digital Systems

## May 23
### Sequential circuits
![500](../Images/Pasted%20image%2020220523082447.png)
Specified by a time sequency of inputs, outputs, internal states

- Synchronous -> 
	- happens at a particular clock frequency
	- action only at discrete instance
	- easy to define specific states
- Asynchronous ->
	- if we know the time it takes to propagate through a gate or conducting line
	- propagates delay of logic gates
	- may become unstable

#### Synchronous sequential circuit

Latch: storage element changes state based on input level
Flip-flop: storage element changes state based on input transition (clock transition)

#### Latches

**1. SR(set-reset) Latch**
NOR implementation: Inputs zero by default, become 1 when triggered

S | R | Q | Q'
-- | -- | -- | --
1 | 0 | **1** | 0 -> *Set condition*
0 | 0 | 1 | 0 after S = 1, R = 0
0 | 1 | **0** | 1 -> *Reset condition*
0 | 0 | 0 | 1, after S =  0, R = 1
1 | 1 | 0 | 0 -> *Forbidden state*

![400](../Images/Pasted%20image%2020220523084906.png)

NAND implementation: Inputs 1 by default, zero when triggered

S | R | Q | Q'
-- | -- | -- | --
1 | 0 | **0** | 1 -> *Set condition*
1 | 1 | 0 | 1 after S = 1, R = 0
0 | 1 | **1** | 0 -> *Reset condition*
1 | 1 | 1 | 0, after S =  0, R = 1
0 | 0 | 1 | 1 -> *Forbidden state*

![300](../Images/Pasted%20image%2020220523085603.png)

NAND implementation with enable pin:
![400](../Images/Pasted%20image%2020220531210835.png)

E | S | R | Q | Q'
-- | -- | -- | -- | --
0 | X | X | No change | No change
1 | 1 | 1 | No change | No change
1 | 0 | 1 | 1 | 0
1 | 1 | 0 | 0 | 1
1 | 0 | 0 | 1 | 1

**2. D Latch (Transparent latch)**
![400](../Images/Pasted%20image%2020220523091127.png)

E | D | Q | Q'
-- | -- | -- | --
0 | X | No change | No change
1 | 0 | 0 | 1
1 | 1 | 1 | 0

#### Flip-flop

**Negative edge triggered master-slave D Flip-flop**
![500](../Images/Pasted%20image%2020220523092244.png)

Clk | Y | Q
-- | -- | --
0 | No change | Y
1 | D | No change 
0 -> 1 | No change -> D | Y -> No change
1 -> 0 | D -> No change | No change -> Y = D

> [!IMPORTANT]
> **Q(t + 1) = D**

> It is example of Moore machine, output is independent of previous state

**Positive triggered D flip-flop:**
Complement clock

![400](../Images/Pasted%20image%2020220523093009.png)

**JK Flip flop**
![300](../Images/Pasted%20image%2020220531222908.png)

D = JQ' + K'Q

J | K | D | Q (t + 1)
-- | -- | -- | --
0 | 0 | Q | Q
0 | 1 | 0 | 0
1 | 0 | 1 | 1
1 | 1 | 1 | Q'

**Excitation Tables**

$A_t$ | $A_{t + 1}$ | $J_A$/$J_B$ | $K_A$/$J_B$
-- | -- | -- | --
0 | 0 | 0 | X
0 | 1 | 1 | X
1 | 0 | X | 1
1 | 1 | X | 0

**T flip-flop**
set J = K in JK flip-flop

![300](Pasted%20image%2020220531223759.png)

T | Q(t + 1)
-- | --
0 | Q(t)
1  | Q'(t)

$Q(t + 1) = T \oplus Q$

**Excitation Table:**

$A_t$ | $A_{t + 1}$ | T 
-- | -- | -- 
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0

**SR Flip-flop**

S | R | Q | Q'
-- | -- | -- | --
0 | 0 | No change | No change
0 | 1 | 0 | 1
1 | 0 | 1 | 0
1 | 1 | 1 | 1

![](../Images/Pasted%20image%2020220601180211.png)

**Excitation Table:**

Q(t)| Q(t + 1) | S | R
-- | -- | -- | --
0 | 0 | 0 | X
0 | 1 | 1 | 0
1 | 0 | 0 | 1
1 | 1 | X | 0

## May 26
#### Analysis of synchronous sequential circuits
The idea is to find what the circuit does (in the form of say a state diagram) given the circuit diagram

Eg.
![500](Pasted%20image%2020220531225105.png)

$A_{t + 1} = A_{t} x_{t}+ B_{t}x_{t}$
$B_{t + 1} = A_{t}' x_{t}$
$y = (A_{t}+ B_{t}) x_{t}'$

**State Table:**
![400](../Images/Pasted%20image%2020220526112616.png)

**State Diagram**
![400](../Images/Pasted%20image%2020220526113205.png)

This circuit detects zeroes after a series of ones

Eg.
![400](../Images/Pasted%20image%2020220526113755.png)

$A_{t + 1} = A \oplus x \oplus y$

**State Table**

A | x | y | $A_{t + 1}$
-- | -- | -- | --
0 | 0 | 0 | 0
0 | 0 | 1 | 1
0 | 1 | 0 | 1
0 | 1 | 1 | 0
1 | 0 | 0 | 1
1 | 0 | 1 | 0
1 | 1 | 0 | 0
1 | 1 | 1 | 1

**State Diagram**
![400](../Images/Pasted%20image%2020220526114214.png)

Eg.
![500](../Images/Pasted%20image%2020220531230044.png)

$J_{A} = B$
$K_{A} = Bx'$
$J_{B} = x'$
$K_{B} = A \oplus x$

**State Table**

$A_t$ | $B_t$ | x | $A_{t + 1}$ | $B_{t + 1}$ | $J_A$ | $K_A$ | $J_B$ |  $K_B$
-- | -- | -- | -- | -- | -- | -- | -- | --
0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0
0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1
0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0
0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1
1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1
1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0
1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1
1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0

**State Diagram**
![400](../Images/Pasted%20image%2020220527103722.png)

#### Finite State Machines:

**Mealy Machine**
- Output depends directly on input
![](Pasted%20image%2020220531230631.png)

**Moore Machine:**
![](Pasted%20image%2020220531230644.png)
- Output doesn't depend directly on input

## May 27
#### State Reduction

Eg.
![400](../Images/Pasted%20image%2020220527105619.png)

![400](../Images/Pasted%20image%2020220531231427.png)
There are some redundant terms here. For example, e and g do the same thing, so we can get rid of it. If we set e = g, d and f also turn out to be the same.
![](../Images/Pasted%20image%2020220531231504.png)

#### Design Procedure
- Derive state table
- Reduce number of states
- Assign unique binary value for each state
- Obtain binary coded state table
- Choose type of flip flops to be used
- Derived simplified flip-flop input equation
- Draw logic circuit

**Two bit counter**
4 states are required
- 2 bits/flip-flops
- 1 input

![400](../Images/Pasted%20image%2020220527111629.png)

$A_t$ | $B_t$ | x | $A_{t + 1}$ | $B_{t + 1}$ | y
-- | -- | -- | -- | -- | -- 
0 | 0 | 0 | 0 | 0 | 0 
0 | 0 | 1 | 0 | 1 | 0 
0 | 1 | 0 | 0 | 0 | 0 
0 | 1 | 1 | 1 | 0 | 0 
1 | 0 | 0 | 0 | 0 | 0 
1 | 0 | 1 | 1 | 1 | 0 
1 | 1 | 0 | 0 | 0 | 1 
1 | 1 | 1 | 1 | 1 | 1 

$A_{t + 1} = x(A_{t}+ B_{t})$
$B_{t + 1} = x(A_{t} + B_{t}')$
$y = AB$

#### Synthesis using D Flip-flop
Extreme peace
![500](../Images/Pasted%20image%2020220531234252.png)

#### Synthesis using JK Flip-flop

$A_{t + 1} = x(A_{t}+ B_{t})$
$B_{t + 1} = x(A_{t} + B_{t}')$
$y = AB$

**State Table**
![](../Images/Pasted%20image%2020220527114249.png)

## May 30
#### 3-bit Counter
**Synthesis using T flip-flop**

**Excitation Table**


![](../Images/Pasted%20image%2020220530091308.png)

$T_{A_{0}} = 1$
$T_{A_{1}} = A_0$
$T_{A_{2}} = A_{1}A_{0}$

![](../Images/Pasted%20image%2020220530091559.png)

**Timing Circuits**
![400](../Images/Pasted%20image%2020220601193618.png)

**Setup time** is defined as the minimum amount of time before the clock edge, during which the data must be held stable i.e. the input should not change within the setup time duration so as to ensure proper data to be latched.
**Hold time** is defined as the minimum amount of time after the clock edge, during which the data must be held stable i.e. the input should not change within the Hold time duration so as to ensure proper data to be latched.

## Registers and Counters
Registers are a group of flip-flops and gates that store data

**Asynchronous register using D flip-flops**

![300](../Images/Pasted%20image%2020220605171919.png)
- I0, I1, I2, I3 are the inputs stored
- Clear_b is 1 by default
- When Clear_b is 0, all flip-flops are set to 0

> [!failure] Problems:
> The output changes during clock-edge if inputs are changed. There are two ways to "store" the information:
> - Clock should be held in pause
> - Input should be held constant
> 
Messing around with either of them is not a good idea!

#### 4-bit parallel load registers

Holds the output in a given state until you are ready to change the state ("loading")

![500](../Images/Pasted%20image%2020220605174407.png)

- When load is 1, Input data is transferred
- When load is 0, existing data is stored undisturbed

#### Shift Register
Shifts data to neighbouring flip-flops during each clock cycle
![](../Images/Pasted%20image%2020220605174706.png)

#### Serial Adder
4-bit serial adder by loading through shift resistor and storing sum in another shift register
![500](../Images/Pasted%20image%2020220605192240.png)

Present State $Q_t$| Inputs : x | y | Next State $Q_{t + 1}$ = C | S | $J_Q$ | $K_Q$
-- | -- | -- | -- | -- | -- | --
0 | 0 | 0 | 0 | 0 | 0 | X 
0 | 0 | 1 | 0 | 1 | 0 | X
0 | 1 | 0 | 0 | 1 | 0 | X
0 | 1 | 1 | 1 | 0 | 1 | X
1 | 0 | 0 | 0 | 1 | X | 1
1 | 0 | 1 | 1 | 0 | X | 0 
1 | 1 | 0 | 1 | 0 | X | 0 
1 | 1 | 1 | 1 | 1 | X | 0

$J_{Q}= xy$
$K_{Q} = x'y'$
S = $x \oplus y \oplus Q_t$

## June 2
## Bidirectional Universal Shift register
- Parallel/serial in, parallel/serial out
- Shift from left to right and right to left

$S_0$ | $S_1$ | Operation |  
-- | -- | -- | --
0 | 0 | No change | $Q_{t + 1} = Q_{t}$
0 | 1 | Shift right | $A_{3} \rightarrow A_{2} \rightarrow A_{1} \rightarrow A_{0}$
1 | 0 | Shift left | $A_{0} \rightarrow A_{1} \rightarrow A_{2} \rightarrow A_{3}$
1 | 1 | Parallel load | Parallel input

- Clear is used to asynchronously reset the D flip-flops

![600](../Images/Pasted%20image%2020220602112437.png)

Diagram:
![400](Pasted%20image%2020220605191732.png)

## June 3
#### Counters
Subset of register, in which it goes through pre-defined sequence of binary states

#### Ripple counter
- flip-flop transition triggers the next flip-flop (it's not synchronized by a common clock)

![](../Images/Pasted%20image%2020220603101829.png)

#### Synchronous counter
- Flip flops triggered by common clock

**Up-Down counter**
Use T flip-flop instead of JK flip-flop
![400](../Images/Pasted%20image%2020220603103145.png)

**BCD Counter using T flip-flop**

A3|A2 | A1 | A0 | A3 | A2 | A1 | A0 | y | $T_{A3}$ | $T_{A2}$ | $T_{A1}$ | $T_{A0}$ 
-- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- 
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 
0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 
0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 
0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 
0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 
0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 
0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 
0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 
1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1
1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1

$T_{A0}$ =  1
$T_{A1}$ = A3' A0
$T_{A2}$ = A3' A1 A0 (can be simplified further)
$T_{A3}$ = A3' A2 A1 A0 + A3 A2' A1' A0 (can be simplified further)
y = A3 A2' A1' A0

#### Binary counter with parallel load
- We want parallel loading capacity, as we often want to start the counter at a particular state instead of some arbitrary state

![](../Images/Pasted%20image%2020220603111328.png)

![](Pasted%20image%2020220603111805.png)


uplupup
![](Pasted%20image%2020220603112546.png)

![](Pasted%20image%2020220603113218.png)

**Ring counter**
Inputs going in a cycle
![](../Images/Pasted%20image%2020220603114524.png)

**Johnson Counter**
# Fill later

## June  6
#### Programmable Logic Devices
 
                     Programable logic devices
                                           |
I/O Block -> Programmable switch matrix -> I/O Block

**Field programmable gate array (FPGA)**
- Reconfigurability
- Rapid prototyping
- Parallel processing (multiple cores)
- Low latency
- Low power consumption-> we're only turning on the gates we want

#### Memory
Read-Only Memory | Random Access Memory
-- | --
Non-volatile, i.e. doesn't lose information when powered down | Volatile
Hard-wired (look-up table)| Faster than a ROM
"Read" only | Both read and write

#### Random access memory

SRAM | DRAM
-- | --
Static RAM | Dynamic RAM
Latches and flip-flops | Capacitor, needs refreshing
Retains data for a long timescale | Shorter timescale
Faster | Slower
Expensive |  Less expensive
More power | Less power

Memory Enable | Read/Write | Operation
-- | -- | --
0 | X | None
1 | 0 | Wrote
1 | 1 | Read

![](../Images/Pasted%20image%2020220606091313.png)

Clocked at 50 MHz
![600](../Images/Pasted%20image%2020220606091418.png)
![600](Pasted%20image%2020220606091908.png)

###### Memory Cell
![](Pasted%20image%2020220606092101.png)

![400](../Images/Pasted%20image%2020220606092450.png)

![600](../Images/Pasted%20image%2020220606092814.png)

> [!failure] Issues
> k inputs
> $2^k$ words
> $2^k$ AND gates with k inputs each

**Coincident decoding**
Keep track of x and y coordinates, using $2^{k/2}$ bits for x coordinates and $2^{k/2}$ bits for y coordinate.

![](Pasted%20image%2020220606094034.png)

![500](../Images/Pasted%20image%2020220606094258.png)
