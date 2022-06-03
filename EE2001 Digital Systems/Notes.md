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
#### Counter
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

#### 4-bit parallel load registers

Holds the output in a given state until you are ready to change the state ("loading")

![](../Images/Pasted%20image%2020220530093316.png)

#### Shift Register

![](../Images/Pasted%20image%2020220530093632.png)

Copy contents of Register A into Register B

## June 2
## Universal Shift register
- Parallel/serial in, parallel/serial out
- Shift from left to right and right to left

$S_0$ | $S_1$ | Operation |  
-- | -- | -- | --
0 | 0 | No change | $Q_{t + 1} = Q_{t}$
0 | 1 | Shift right | $A_{3} \rightarrow A_{2} \rightarrow A_{1} \rightarrow A_{0}$
1 | 0 | Shift left | $A_{0} \rightarrow A_{1} \rightarrow A_{2} \rightarrow A_{3}$
1 | 1 | Parallel load | Parallel input

![600](../Images/Pasted%20image%2020220602112437.png)

- Clear is used to asynchronously reset the D flip-flop

Eg. 4-bit serial adder by loading through shift resistor and storing sum in another shift register

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
