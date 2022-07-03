> Haricharan
# Digital Systems

## May 23
### Sequential circuits
![500](../Images/Pasted%20image%2020220523082447.png)
Specified by a time sequence of inputs, outputs, internal states

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
- Clear_b
	- is 1 by default
	- is 0, all flip-flops are set to 0

> [!failure] Problems:
> The output changes during clock-edge if inputs are changed. There are two ways to "store" the information:
> - Clock should be held in pause
> - Input should be held constant
> 
Messing around with either of them is not a good idea!

#### Synchronous register
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

#### Asynchronous
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
0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 
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

![](Pasted%20image%2020220603112546.png)

Eg. BCD counter with parallel load
- ![400](../Images/Pasted%20image%2020220606211734.png)
All inputs are 0, when A3 A0 are like 11, we reach 1001 we load the counter with 0000

- ![400](Pasted%20image%2020220606211827.png)
When A3 A1 are like 11, we've hit 1001 and we clear the counter

**Ring counter**
Inputs going like 1000, 0100, 0010, 0001, 1000, etc.

For $2^{n}$ timing circuit

**Shift register: Shift input is T3**
![300](Pasted%20image%2020220606213631.png)
- $2^n$ flip-flops

**2-bit counter and decoder**
![300](../Images/Pasted%20image%2020220606212325.png)
$n$ flip-flops and $2^{n}$ n input and gates

**Johnson Counter/Twisted ring counter/Switch tail counter**

![500](../Images/Pasted%20image%2020220607232222.png)

![500](../Images/Pasted%20image%2020220606215708.png)

For n timing sequences, there are n/2 flip-flops and n gates required, and all are two input gates

## June  6
#### Memory Units

**Word:** Groups of bits stored by memory units
Modern computers are 64-bit computers
**Address:** Integer from $0 \rightarrow 2^k - 1$, where k is the number of address lines

Read-Only Memory | Random Access Memory
-- | --
Non-volatile, i.e. doesn't lose information when powered down | Volatile
Hard-wired (look-up table)| Faster than a ROM
"Read" only | Both read and write

#### Random access memory
Diagram of a memory unit and its functionality:
![400](../Images/Pasted%20image%2020220606091313.png)

Memory Enable | Read/Write | Operation
-- | -- | --
0 | X | None
1 | 0 | Write
1 | 1 | Read

-> Access time: Time required for read operation
-> Cycle time: Time required for write operation
Access time and cycle time < Clock time of CPU

Clocked at 50 MHz, i.e. Time period of one pulse is 20 nsec
![600](Pasted%20image%2020220611143253.png)

SRAM | DRAM
-- | --
Static RAM | Dynamic RAM
Latches and flip-flops | Capacitor, needs refreshing
Retains data for a long timescale | Shorter timescale
Faster | Slower
Expensive |  Less expensive
More power | Less power
Address multiplexing is more complicated, as it uses 4 transistors | Address multiplexing is easier, as it uses transistor + capacitor

###### Memory Cell
- Stores one bit of information
- For a RAM with m words and n bit word length, there are m x n memory cells

![](Pasted%20image%2020220606092101.png)

Select | Read/Write | Input | Output | $Q_+$
-- | -- | -- | -- | --
0 | X | X | 0 | Q
1 | 0 | I | 0 | I
1 | 1 | X | Q | Q

![400](../Images/Pasted%20image%2020220606092450.png)

Construction of 4 x  4 RAM
![600](../Images/Pasted%20image%2020220606092814.png)

> [!failure] Issues
> k inputs and $2^k$ words
> The decoder requires $2^k$ AND gates with k inputs (k + 1, if we have the enable pin) each

**Coincident decoding**
Keep track of x and y coordinates, using ${k/2}$ bits for x coordinates and ${k/2}$ bits for y coordinate.
This uses 2 * (32 5-input AND gates) and the memory cell is at the intersection of these two rows and columns.

1024 words memory, using coincident decoding
![600](Pasted%20image%2020220606094034.png)

**Address Multiplexing in DRAM**
![500](../Images/Pasted%20image%2020220606094258.png)
**Strobes**: Essentially enable pins, that enable the data in register to the decoder when 0
- RAS: Row address strobe
- CAS: Column address strobe
First, RAS is made 0, a particular row is chosen, then CAS is made 0, the respective column is chosen, then the data is read/written. After that, both strobes are reset to 1
---
#### Programmable Logic Devices

- I/O Block -> Programmable switch matrix -> I/O Block
- Implemented using AND-OR gates

Programmable Read Only Memory:
![](Pasted%20image%2020220611210837.png)

Programmable Logic Array:
![](Pasted%20image%2020220611210953.png)

Programmable Array Logic:
![](Pasted%20image%2020220611210859.png)

#### Programmable Read only memory (PROM)
- Memory elements are interconnections patterns along with decoder/OR gates
- $2^k$ words, each word is n bits long
![600](Pasted%20image%2020220611210837.png)
- Programmable OR array is built with fuses intact, fuses broken while programming the device

Eg. 32 x 8 PROM
![500](Pasted%20image%2020220610102128.png)
*Note*: Each OR gate is a 32 input OR gate

**Sample truth table**
![](Pasted%20image%2020220610102436.png)

**Using PROMs to design functions**
- Each of $A_{0} \dots A_{7}$ can be used as a function 

Eg. Design a combinational circuit using a programmable read only memory to accept a 3-bit number and outputs a binary number equal to square of the input number

$A_2$ | $A_1$ | $A_0$ | $B_5$ | $B_4$ |  $B_3$ |  $B_2$ |  $B_1$ |  $B_0$ 
-- | -- | -- | -- | -- | -- | -- | -- | --
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 
0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1
0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0
0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1
1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0
1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1
1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0
1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1

- $B_{0}= A_{0}$
- $B_{1}= 0$
- $B_{2}\dots B_{5}$ all depend on the input, so they the word length has to be 4 

ROM would be an 8x4 ROM, where word length is 4 and we have to address 8 locations.  We can burn appropriate connections corresponding to $B_{5}\dots B_2$ in the above table
![300](../Images/Pasted%20image%2020220610103638.png)

#### Programmable Logic Array (PLA)
![](Pasted%20image%2020220611210953.png)
Both AND gates and OR gates are programmable

Three parts:
- AND gate inputs are programmable
- OR gate inputs are also programmable
- Complemented outputs can be XOR-ed to get proper output
- Using common outputs is better

**PLA size:**
- n inputs
- k 2n-input AND gates
- m Outputs
- $2n \times k$ Number of connections between input and AND
- $m \times k$ connections between AND and OR

Typical PLA size would be $16/48/8 \rightarrow n/k/m$

Eg.
$F_1 = AB' + AC + A'BC'$
$F_{2}= (AC + BC)'$

Programming Table

A | B | C | | $F_{1} (T)$ | $F_{2} (C)$
-- | -- | -- | -- | -- | --
1 | 0 | - | | 1 | _
1 | _ | 1 | | 1 | 1
_ | 1 | 1 | | _ | 1
0 | 1 | 0 | | 1 | _

![600](../Images/Pasted%20image%2020220610104234.png)

**Eg.**
$F_1$ = $\sum$ (0, 1, 2, 4)
$F_2$ = $\sum$ (0, 5, 6, 7)

$F_{1} = A'B' + B'C' + A'C'$
$F_1' = AB + BC + AC$
$F_{2}= A'B'C' + AC + AB$

Programming Table

A | B | C | | $F_{1} (C)$ | $F_{2}(T)$
-- | -- | -- | -- | -- | --
1 | 1 | - | | 1 | 1
1 | _ | 1 | | 1 | 1
_ | 1 | 1 | | 1 | _
0 | 0 | 0 | | _ | 1

![](../Images/Pasted%20image%2020220610110716.png)

#### Programmable Array Logic
![](Pasted%20image%2020220611210859.png)
- Fixed OR array (not as flexible as PLA)
- Typical 4 inputs and 4 outputs with 3 AND + OR gate at each output

![550](../Images/Pasted%20image%2020220610111803.png)

- Lines $1 \dots 8$
- Lines 9 and 10 can be used to feed in the first input

Eg.
W = $\sum$ (2, 12, 13)
X = $\sum$ (7, 8, 9, 10, 11, 12, 13, 14, 15)
Y = $\sum$ (0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 15)
Z = $\sum$ (1, 2, 8, 12, 13)

W = A'B'CD' + A B C'
X = A + BCD
Y = A' B + CD + B'D'
Z = W + AC'D' + A'B'C'D

Programming Table

Product Term | A | B | C | D | w | Output
-- | -- | -- | -- | -- | -- | -- 
1 | 1 | 1 | 0 | _ | _ |
2 | 0 | 0 | 1 | 0 | _ |  w = ABC' + A'B'C D'
3 | _ | _ | _ | _ | _ |
  |  
4 | 1 | _ | _ | _ | _ |
5 | _ | 1 | 1 | 1 | _ | x = A + BCD
6 | _ | _ | _ | _ | _ |
  |  
7 | 0 | 1 | _ | _ | _ |
8 | _ | _ | 1 | 1 | _ | y = A'B + CD + B'D'
9 | _ | 0 | _ | 0 | _ | 
  |  
10 | _ | _ | _ | _ | 1 |
11 | 1 | _ | 0 | 0 | _ | z = w + A C'D' + A'B'C'D
12 | 0 | 0 | 0 | 1 | _ | 

![600](Pasted%20image%2020220611220633.png)

#### Sequential Programmable Logic Devices
![600](../Images/Pasted%20image%2020220613085335.png)

**Eg. Field Programmable logic sequencer**
- PLA with the output driving a flip-flop

Macro-cell
![600](../Images/Pasted%20image%2020220613090158.png)
Output enable (OE): three state buffer
- if OE is 0, output is not obtained
- if OE is 1, output is obtained

Eg. 3-bit up counter which counts when input = 1, remains in same state when input is 0
State Table:
![400](Pasted%20image%2020220613090300.png)
$Q_2^+ = Q_2 Q_0' + Q_2Q_1' + Q_2 x' + Q_2' Q_1 Q_0 x$
$Q_1^+ = Q_1 Q_0' + Q_1 x' + Q_1' Q_0 x$
$Q_0^+ =  Q_0 x' + Q_0' x$

Eg. Design a PLD circuit using PAL/PLA for detecting 1101 Sequence
![500](Pasted%20image%2020220613091438.png)

A | B | x | A+ | B+ | y
-- | -- | -- | -- | -- | --
0 | 0 | 0 | 0 | 0 | 0
0 | 0 | 1 | 0 | 1 | 0
0 | 1 | 0 | 0 | 0 | 0
0 | 1 | 1 | 1 | 0 | 0
1 | 0 | 0 | 1 | 1 | 0
1 | 0 | 1 | 1 | 0 | 0
1 | 1 | 0 | 0 | 0 | 0
1 | 1 | 1 | 0 | 1 | 1

$A_+ = A' B x + A B'$
$B_+ = A'B'x + A B'x' + A B x$
$y = A B x$

#### Field programmable gate array (FPGA)
- Reconfigurability
- Rapid prototyping
- Parallel processing (multiple cores)
- Low latency
- Low power consumption-> we're only turning on the gates we want

## June 17
#### Asynchronous sequential circuits

![500](../Images/Pasted%20image%2020220617102535.png)

Eg.
![400](../Images/Pasted%20image%2020220617103602.png)

$x/y_1y_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | 0 | 1 | 1 | 0
1 | 0 | 0 | 1 | 1

$x/y_1y_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | 0 | 1 | 1 | 0
1 | 1 | 1 | 0 | 0

**Transition Table**

$x/y_1y_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | 00 | 11 | 11 | 00
1 | 01 | 01 | 10 | 10

Stable states -> 00, 11, 01, 10
If any other states are attained, we change to some other state in the next instant

Eg.
**Flow Table**
Two states with two inputs and one output

$y / x_1x_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
a | a, 0 | a, 0 | a, 0 | b, 0
b | a, 0 | a, 0 | b, 1 | b, 0

$y / x_1x_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | 0 | 0 | 0 | 1
1 | 0 | 0 | 1 | 1
$Y = x_1x_2' + x_1y$

$y / x_1x_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | 0 | 0 | 0 | 0
1 | 0 | 0 | 1 | 0
$z = x_1x_2y$
![400](../Images/Pasted%20image%2020220617105409.png)

**Race conditions**
The process of obtaining the logic circuit from the flow table is not always simple
11 -> 00  or 01 -> 10: might go through some intermediate state, which is fine
*Critical Race condition:* End up at different state depending on delays
Non-critical Race condition: End up at same state. It can cause hazards though

Eg.

$x/y_1y_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | ==00== |  |  | 
1 | 11 | 11 | ==11== | 11
00 -> 11
00 -> 01 -> 11
00 -> 10 -> 11
This is *non-critical race condition*

Eg.

$x/y_1y_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | ==00== |  |  | 
1 | 11 | ==01== | ==11== | ==10==
00 -> 11 if delays are equal
00 -> 01 or 00 -> 10 if delays are unequal
This is *critical race condition*

Eg.

$x/y_1y_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | ==00== |  |  | 
1 | 11 | ==01== | 01 | 11
00 -> 01
00 -> 10 -> 11 -> 01
*Non-critical race condition*

Eg.

$x/y_1y_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | ==00== |  |  | 
1 | 11 | 11 | ==11==| ==10==
00 -> 01 -> 11
00 -> 10
Critical Race condition

Eg.

$x/y_1y_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | ==00== |  |  | 
1 | 01 | 11 | 10 | 01
For x = 1, output is unstable and cycles as follows: *00 -> 01 -> 11 -> 10 -> 01 -> 11 -> 10...*

**Determining Stability**
![400](../Images/Pasted%20image%2020220620122908.png)
$Y = (x_1y)'x_2$

Transition Table:

$y/x_1x_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | ==0== | 1 | <mark style="color: red">1</mark> | ==0==
1 | 0 | ==1== | <mark style="color: red">0</mark> | 0

Unstable circuit, as for input 11, output switches rapidly between two states

**Analysis**
- Determine all feedback loops
- Derive Boolean function for each $y_i$
- Plot each y in a map
- Combine all maps (transition table)
- Identify and circle stable states
- Identify race conditions

**SR latch:**
$Y = ((S+y)' + R)' = (S + y)R' = R'S + R'y$
![400](../Images/Pasted%20image%2020220620123616.png)

y / SR | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | ==0== | ==0== | ==0== | 1
1 | ==1== | 0 | 0 | ==1==
- It is stable
- Race conditions checking
	- 00 -> 11
		- 00 -> 01 -> 11
		    0       0       0
		- 00 -> 10 -> 11 -> 11  
		    0        1       0         0
		- 00 -> 01 -> 11
		    1        0      0
		- 00 -> 10 -> 11 -> 11
		    1        1      0       0
	- 11 -> 00
		- **11 -> 10 -> 00**
		   **0        1       1**
		- **11 -> 01 -> 00**
		   **0       0       0**
		- 11 -> 10 -> 00
		    1   Unstable
		- 11 -> 01 -> 11
		    1 Unstable
	- 01 -> 10
		- 01 -> 00 -> 10 -> 10
		    0       0       1        1
		- 01 -> 11 -> 10 -> 10
		    0       0      1        1
		- 01 -> 00 -> 10
		    1 Unstable
		- 01 -> 00 -> 10
		    1 Unstable
	- 10 -> 01
		- 10 -> 00 -> 01
	        0 Unstable
		- 10 -> 11 -> 01
		    0 Unstable
		- 10 -> 00 -> 01 -> 01
		    1       1        0       0
==,		- 10 -> 11 -> 01==
==,		    1       0==

11 -> 00
S -> 0 first y -> 0
R -> 0 first y -> 1
- we have to ensure $SR = 0$ to prevent 11 state

$Y = ((S+y)' + R)' = (S + y)R' = R'S + R'y + 0 = R'S + R'y + SR = S + R'y$

**Finding Critical Race conditions**
Eg. 

![600](../Images/Pasted%20image%2020220620142116.png)
Transition Table:

$y_1 y_2 /x_1 x_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
00 | ==00== | ==00== | 01 | ==00==
01 | ==01== | ==01== | 11 | 11
11 | 00 | ==11== | ==11== | 10
10 | 00 | ==10== | 11 | ==10==
For each input, at least one stable state -> stable

Race condition:
- Input 00
No 00 -> 11, 11 -> 00, 01 -> 10, 10 -> 01 conditions

- Input 01, state 11
11 -> 00: can be done when input is 00
But, $y_1 y_2$ might go as follows:
- 11 -> 10 -> 00
- 11 -> 01
*Critical Race condition*

- Input 01, no other conditions possible

- Input 11, state 11
11 -> 00, input given must be 00
- 11 -> 01 -> 01
- 11 -> 10 -> 00
*Critical Race condition*

- Input 10, no other conditions possible

**Implementation of circuit using SR latch**
Eg. $Y = x_1x_2' + x_1y$

$y / x_1x_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | 0 |  0 | 0 | 1
1 | 0 | 0 | 1 | 1

Excitation Table

y | Y | S | R
-- | -- | -- | --
0 | 0 | 0 | X
0 | 1 | 1 | 0
1 | 0 | 0 | 1
1 | 1 | X | 0

**S**

$y / x_1x_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | 0 |  0 | 0 | 1
1 | 0 | 0 | X | X
S = $x_1x_2'$

R

$y / x_1x_2$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | X | X | X | 0
1 | 1 | 1 | 0 | 0
R = $x_1'$

**Hazards** -> Malfunction/switching transient due to unequal delays

**Static 1 hazard**
![400](Pasted%20image%2020220620145950.png)
$x_1 = 1, x_3 = 1, x_2: 1 \rightarrow 0$
Y becomes 0 for an instant, then becomes 1 again

The function is $Y = x_1 x_2 + x_3 x_2'$

$x_1 / x_2x_3$ | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
0 | 0 | 1 | 0 | 0
1 | 0 | 1 | 1 | 1

Adjacent 1s without common implicant is static 1 hazard

**Static 0 hazard**
![400](Pasted%20image%2020220620150227.png)

Adjacent 0s without common implicant is static 0 hazard