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

**Latches**
- Storage element whose state changes based on *input level*

Eg. SR(set-reset) Latch

S | R | Q | Q'
-- | -- | -- | --
1 | 0 | **1** | 0 -> *Set condition*
0 | 0 | 1 | 0 after S = 1, R = 0
0 | 1 | **0** | 1 -> *Reset condition*
0 | 0 | 0 | 1, after S =  0, R = 1
1 | 1 | 0 | 0 -> *Forbidden state*
NOR implementation
![400](../Images/Pasted%20image%2020220523084906.png)
NAND implementation
![300](../Images/Pasted%20image%2020220523085603.png)

S | R | Q | Q'
-- | -- | -- | --
1 | 0 | **0** | 1 -> *Set condition*
1 | 1 | 0 | 1 after S = 1, R = 0
0 | 1 | **1** | 0 -> *Reset condition*
1 | 1 | 1 | 0, after S =  0, R = 1
0 | 0 | 1 | 1 -> *Forbidden state*

![400](../Images/Pasted%20image%2020220523090414.png)

**D Latch (Transparent gate)**
![400](../Images/Pasted%20image%2020220523091127.png)
Q = D if E = 1, else 0

**Flip-flop**
- Changes value during *clock transitions*

**Edge-triggered D Flip-flop**
![500](../Images/Pasted%20image%2020220523092244.png)

Negative triggered D flip-flop:
When clk -> 0, Master is disabled, slave is enabled, Q = Y
When clk -> 0 - 1, Master is enabled, slave is disabled, Y = D
When clk -> 1 - 0, Master is disabled, slave is enabled, Q = D

Positive triggered D flip-flop:
Complement clock

**Symbols:**
![400](../Images/Pasted%20image%2020220523093009.png)

**Some other flip-flops**
![600](Pasted%20image%2020220523093614.png)

## May 26
#### Analysis of synchronous sequential circuits
# DO THIS PROPERLY LATER
Eg.
![500](../Images/Pasted%20image%2020220526112403.png)
$A_{t + 1} = A_{t} x_{t}+ B_{t}x_{t}$
$B_{t + 1} = A_{t}' x_{t}$
$y = (A_{t}+ B_{t}) x_{t}'$

**State Table:**

![400](../Images/Pasted%20image%2020220526112616.png)

**State Diagram**
![400](../Images/Pasted%20image%2020220526113205.png)

This circuit detects a series of zeroes after ones

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

#### Finite State Machines:

![600](Pasted%20image%2020220526115225.png)

**JK Flip - Flop**
State Table

$J_{A} = B$
$K_{A} = Bx'$
$J_{B} = x'$
$K_{B} = A \oplus x$

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

![400](../Images/Pasted%20image%2020220527103722.png)

**T Flip Flop**

## May 27
#### State Reduction

Eg.
![400](../Images/Pasted%20image%2020220527105619.png)

![400](../Images/Pasted%20image%2020220527105741.png)

![](../Images/Pasted%20image%2020220527110348.png)

Design Procedure:
- Derive state table
- Reduce number of states
- Assign unique binary value for each state
- Obtain binary coded state table
- 
