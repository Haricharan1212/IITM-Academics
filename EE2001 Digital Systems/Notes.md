>Haricharan
# Digital Systems

## 2nd May

Week 1 outline!
![600](../Images/Pasted%20image%2020220502083915.png)

**What are the advantages of digital systems?**
- Resilience to noise -> Noise forms a Gaussian distribution around the actual value. Filtering analog signals is hard, especially with noise.
- Ease of storage -> Flash/CD/DVD
	- Previously stored in analog form in magnetic tapes
- More secure (encrypted)
- Flexible signal processing (e.g. noise removal)

**What are some examples and applications of digital systems?**
- Digital thermometers
- automated driving
- digital computer stuff
- augmented reality, etc.
- The AI

**What is the anatomy of a digital system?**
- Top down methodology: we talk about big things and break it into smaller pieces
- Implement
	- Sequential logic
	- Combinational logic

**Blocks in a Mobile Phone!**

![300](../Images/Pasted%20image%2020220502082603.png)

**What is a system on a chip?**

Microprocesser | Microcontroller
--- | ---
It's used in computer systems like desktops, etc. | It's used in embedded systems like washing machine, etc.

**Anatomy of a smartphone- What is the iPhone SOC?**
Huge number of logic blocks
CLB-> configurable logic block
Logic blocks-> consists of logic gates like NOR gates, AND gates, etc. and clocks

**Combinational logic gate that does comparison**

![300](../Images/Pasted%20image%2020220502083345.png)

Sequential logic: uses clock cycles and does stuff, and synchronizes stuff!

---
## 3rd May

**Any base to decimal conversion-> just multiply it out**

$7392 = 7 \times 10^{3}+ 3 \times 10^{2}+ 9 \times 10^{1}+ 2 \times 10^0$
$$a_{n}a_{n-1} ... a_{0}. a_{-1} ... a_{-m} = \sum_{i = -m}^{n} a_{i} \text{base}^i$$

**Decimal to binary**:

Eg. 41

41 | Dividing by 2
-- | --
20 | 1
10 | 0
5|0
2|1
1|0
0|1

Then write it from bottom up
Answer is *100101*.

**Decimal to Octal**
Eg. 153

153 | Dividing by 8
-- | --
19|1
2|3
0|2
Answer *231*

0.6875 in binary:
$0.6875 \times 2 = 1, 0.3750$
$0.3750 \times 2 = 0, 0.7500$
$0.7500 \times 2 = 1, 0.5$
$0.5000 \times 2 = 1, 0$

The number is written top-down.
0.1011

**Binary, Hex, Octal conversion is lite, use 2, 4, and 3 digits respectively**

8 bits makes up one byte (little children know this)

**Summary**
![](../Images/Pasted%20image%2020220505161013.png)

## 5th May
#### Complements
Given two n-digit numbers in base 'r'

Nice video: https://www.youtube.com/watch?v=4qH4unVtJkE
**Negative numbers:**
- Sign-magnitude
	- First bit for sign, remaining digits as usual binary
	- There's a problem: 5 + -5 in this representation is NOT zero.
- Ones' complement
	- Positive numbers as usual, negative numbers are just 1s complement (which is toggling every bit)
	- 5   -> 0101
	- -3 -> 1100
	- 5 - 3 -> 10001 -> 0001 -> 1
	- So, it is offset by one and we have to do some juggling around while carrying out subtraction
- 2s complement
	- Take twos complement of every number to get its negative
	- you get one extra number
	- there are *no* signed zeroes
	- The numbers are the same as unsigned numbers mod (2^N)
	- First digit represent -2^N digit really
	- Number + its negative is 0

**Addition of numbers:** lite

**Subtraction of numbers: M - N, where M and N are unsigned numbers** 
- M + (r^n - N)
- if M >= N:
	- Produces end carry, and leftmost carry digit corresponds to r^n, which needs to be discarded (n carry is formed when the first digit is +ve)
	- M - N
- if M < N:
	- Doesn't produce n carry, and result is r^n - (N - M) -> We have to take r's complement and place negative sign at front

Eg. 6 - 13

- +6 -> 00000110
- -13 -> 
	- Binary representation:     (+13) -> 00001101
	- Toggle: 1s complement:  (-13) -> 11110010
	- Add 1 to ones complement -> Twos complement -> 11110011
- Adding them both: 11111001 (first bit, i.e. sign bit is 1)
- end carry not there, so now do twos complement: 00000111
- This is **-7**!

Eg. 15 - 7:
- 15 -> 00001111
- -7 ->  11111001
- Add up: 
100001000 -> **8**!

## May 6
#### Boolean Algebra

**Postulates of Boolean Algebra:**
For a set B (not necessarily {0,1} btw):
1. Closure
2. Identity
	1. x + 0 = x
	2. x . 1 = x
3. Commutative
4. Distributive
	1. x + yz = (x + y)(x + z)
	2. x (y + z) = xy + xz 
5. Complement
	5. x + x' = 1
	6. x x' = 0
6. There are at least two elements x and y such that x $\neq$ y

To solve question, we need identity, distributive, complement

![700](../Images/Pasted%20image%2020220506160806.png)

**Theorems of Boolean Algebra**
1. **x + x = x, x. x = x**
= x (1 + 1) -> Distributive Law
= x . 1 -> OR definition
= x -> Identity element property

2. **x + 1 = 1, x . 0 = 0**
= x + 1
= x + x + x' -> Complement
= x + x' -> Theorem 1
= 1 -> Complement definition

3. **Involution: (x')' = x**
(x')' = (x')' + 0
= (x')' + x x' -> Complement definition
= (x + (x')')(x' + (x')') -> Distributive Law
= x + (x')' -> Complement
= (x + (x')')(x + x') -> Complement
= x + (x') x -> Property again!
= x (1 + x') -> Distributive
= x

**4. Associativity**
xy = yx (Commutativity)
x = (a +  b) + c
y = a + (b + c)
xy = ((a + b) + c)(a + (b + c)) = y
By symmetry, yx = x
So, x = y

**5. De morgan!**
**Lemma:** 
Given: 
- a + b = a + a' = 1
- ab = aa' = 0
To prove:
- a = b'

Multiply first one by b
ab + b = ab + a'b
0 + b = a'a + a'b
b = a'(a + b) = a' 1 = a'

**Now**
x'y' + (x + y) = 1 (Using lemma)
(x + y)' + (x + y) = 1

Therefore:
- (x + y)' = x'y'

**6.  Absorption** 
x + xy
= x (1 + y) -> Distributive
= x

**Usefulness of Boolean algebra: simplifying Boolean expression**
The electrical idea is to keep number of gates minimum

a) AB + A' B = (A + A') B = B
![](../Images/Pasted%20image%2020220506154657.png)

**Canonical Form of Boolean Expressions**
Boolean expression consists of variables in either normal form or its complement

n variables with AND (lowercase)
- We can have 2^n "minterms" (minterm is just every possibility basically)
- minterms are ordered as if they were binary numbers (the image below makes it clear)
- $m_0 m_1 m_2 ... m_{2^n-1}$
- We consider "1" here, as the output 1 is unique
n variables with OR (uppercase):
- We have 2^n "maxterms"
- $M_0 M_1 M_2 ... M_{2^n-1}$
- We consider "0" here, as the output 0 is unique

![](../Images/Pasted%20image%2020220506162055.png)

> [!INFO] Boolean
> Any boolean function can be expressed as
> - sum of minterms
> - products of maxterms!

**Consider the function**
f1(x, y, z) = xyz' + xy'z + xy'z'
This function is 1 when:
x | y | z
-- | -- | --
1 | 1 | 0
1 | 0 | 1
1 | 0 | 0
And 0 for anything else
f1(x, y, z) -> $\Sigma \hspace{5px} 4, 5, 6$
f1 -> $\Pi \hspace{5px} 0, 1, 2, 3, 7$

f2(x, y) -> xy + xy' + x'y'
-> $\Sigma \hspace{5 px} 0, 2, 3$
-> $\Pi \hspace{5px} 1$ = (x' + y)
This is intuitive enough!

**f = $\Pi$ Some maxterms = $\Sigma$ of other minterms**
- It's easy enough to see that $m_{i}' = M_{i}$
	- Say $m_2$ = x + y' + z
	- $m_{2}' = x' y z' = M_{2}$
- $(\sum_{\text{i runs over whatever}} m_{i})'= \sum_{\text{i runs over everything else}} m_i$
	- Proof:
		- $f = \sum m_{i}$
		- f is 1 for certain values of i
		- f' is 0 for those values of i
		- f' is 1 for all other values of i
		- $f' = \sum_{\text{j runs over everything else}} m_j$
- $m_{i} = \Pi_{\text{j = everything else}} M_{\text{j}}$
- $f = \Sigma_{\text{i runs over whatever}} m_{i}$
- $f' = \sum_{\text{i runs over everything else}} m_i$
- $f'' = f = \prod_{\text{i runs over everything else}} m_{i}' = \prod_{\text{i runs over everything else}} M_{i}$

Dual of a function:
- Replacing all AND by OR and vice versa
- Replacing all 1s by 0s

Taking complement of a function is the same as taking dual of the function and replacing each literal by it's complement (this follows from de Morgan's theorem).

To go from positive logic to negative logic, we just have to take the dual!

## May 9

#### Gate level minimization: K-maps
- The objective is find the optimal gate level implementation of the Boolean function
	- Complexity of digital logic circuit is related to the complexity of the algebraic expression
	- Truth tables are unique
	- Pictorial representation is Karnaugh map
- Consider f(x,y,z)
![](../Images/Pasted%20image%2020220509082627.png)

Only one bit changes between adjacent cells (in both axes)

Adjacencies | Literals
-- | --
1 | 3
2 | 2
4 | 1
8 | 0

**f2 = Sum(3,5,6,7)**
x \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0** | 0 | 0 | 1 | 0
**1** | 0 | 1 | 1 | 1

Adjacent cells in K-map represent whatever didn't change!

f2 doesn't change once in x direction, once in y direction, once in z direction
So, $f2 = xy + yz + zx$

**f1 = Sum(1,4,7)**
x \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0** | 0 | 1 | 0 | 0
**1** | 1 | 0 | 1 | 0
No adjacency, so it's simplified already

**f3** = sum(3,4,6,7)
x \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0** | 0 | 0 | *1*| 0
**1** | *1* | 0 | *1* | *1*
f3 = yz + xy + xz' = yz + xz'

- Reason: xy terms is redundant!

So the aim is to cover all minterms.

**f4** = sum (0,2,3,4,5)
x \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0** | 1 | 0 | 0 | 1
**0** | 1 | 1 | 0 | 1
- Four cell adjacency!

f4 = z' + x y'

**f5** = Sum(1,2,5,6,7) = Prod(0, 3, 4)
x \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0** | 0 | 1 | 0 | 1
**1** | 0 | 1 | 1 | 1
f5 = y'z + yz'+ xy 

f5 = (y + z) . (x + y' + z')


**f6** = A'C + A'B + A B' C + B C

A \ BC | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0** | 0 | 1 | 1 | 1
**1** | 0 | 1 | 1 | 0

f6 = C + A'B

**Four variable K-maps**
wx \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**00** | 0 | 0 | 0 | 0
**01** | 0 | 0 | 0 | 0
**11** | 0 | 0 | 0 | 0
**10** | 0 | 0 | 0 | 0

Adjacencies | Literals
-- | --
1 | 4
2 | 3
4 | 2
8 | 1
16 | 0

**f1** = Sum(0,1,2,4,5,6,8,9,12,13,14)

wx \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**00** | 1 | 1 | 0 | 1
**01** | 1 | 1 | 0 | 1
**11** | 1 | 1 | 0 | 1
**10** | 1 | 1 | 0 | 0

f1 = y' + w'z' + x z' = y' + z' (x + w')

f1' = yz + w x' y
f1 = (y' + z') (w' + x +y') = w'y' + w'z' + x y' + x z' + y'z' + y'
                                         = y' + z' (x + w')

Prime Implicant: Total number of adjacencies in the K-map (including redundancies)
Essential Prime Implicant: Prime implicants that cover a minterm no other implicant covers
Redundant Implicant: Implicant for which each minterm is covered by some other implicant

AB \ CD | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**00** | 1 | 0 | 1 | 1
**01** | 0 | 1 | 1 | 0
**11** | 0 | 1 | 1 | 0
**10** | 1 | 1 | 1 | 1

Eg.
- m5 is covered only by one prime implicant, BD is essential prime implicant
- m0 is covered only by B' D'

**Simplification of Kmap**
![](../Images/Pasted%20image%2020220509094525.png)


**F**

1.
AB \ CD | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**00** | 1 | 1 | 0 | 1
**01** | 0 | 1 | 0 | 0
**11** | 0 | 0 | 0 | 0
**10** | 1 | 1 | 0 | 1

2. Essential implicants: 
- B'D' (for 0010 and 1010)
- B'C'
- A'C D

3. All minterms are covered!
4. F = B'D' + B'C' + A' C' D

## May 12
#### Don't care conditions:
Eg. Binary coded decimal (BCD)
Representation of decimals in binary numbers
396 -> Each value is represented by corresponding value
396 -> 0011 1001 0110

BCD doesn't care about remaining inputs like 1111 (corresponding to 15). So, *we don't care* about that part.
Don't cares are represented by X in K-map

F = $\Sigma (1, 3, 7, 11, 15)$
d = $\Sigma (0, 2, 5)$

wx \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**00** | X | 1 | 1 | X
**01** | 0 | X | 1 | 0
**11** | 0 | 0 | 1 | 0
**10** | 0 | 0 | 1 | 0

SOP
F = yz + w'x' or yz + w'z
POS
F = z (w' + y)

## May 13
> **NAND and NOR gates are easier to realize**

AND, NOT, OR gates -> NAND and NOR gates
NAND and NOR gate -> universal gate -> we can create any other gates using these gates

- NOT gate -> NAND(x, x)
- AND gate -> NOT(NAND(x, x))
- OR gate -> NAND(NOT(x), NOT(y))

> [!INFO] Boolean function implementation
> 1. Represent function in K-map
> 2. Obtain simplified function in terms of Boolean operators
> 3. Convert function to NAND/NOR logic
> 4. Implement using NAND/NOR gates

Eg. 
F = AB + CD
NAND logic
- (A' + B')' + (C' + D')' = NOR(NOR(NOR(NOR(A),  NOR (B)), NOR(NOR(C), NOR(D))))

Eg. F = $\Sigma (1,2,3,4,5,7)$

1.
A \ BC | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0** | 0 | 1 | 1 | 1
**1** | 1 | 1 | 1 | 0
F = A B' + A' B + C
2. Done
3. 
NAND((NAND(A, NAND(B)), (NAND(NAND(A), B)), NAND(C))
NOR(NOR(C, NOR(NOR(A), B), NOR(A, NOR(B))))

Eg. F = ((A + B)(C + D)E)'
NOR(NOR(NOR(A, B)), NOR(C, D), NOR(E)))

In general, look at complement:
- AND-NOR <-> NAND-AND -> SOP form combining 1s
- OR-NAND <-> NOR-OR -> POS form combining 0s

x \ yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0** | 1 | 0 | 0 | 0
**1** | 0 | 0 | 0 | 1
**SOP form**
From zeroes, we get F'
F' = z + xy' + x'y
F = (z + xy' + x'y)' -> AND-NOR realization
F = ((x'y)' (x'y)' z') -> NAND-AND realization

**POS form**
F' = (x + y + z)(x' + y + z')
F = ((x + y + z) (x' + y + z'))' -> OR-NAND realization
F = (x + y + z)' + (x' + y + z')' -> NOR-OR realization

#### XOR gate
- Parity checking
- Binary adders
- Error detection and correction

$x \oplus y = xy' + x'y = (x +  y')(x' + y)$

**Identities:**
- $x \oplus 0 = x$
- $x \oplus 1 = x'$
- $x \oplus x = 0$
- $x \oplus x' = 1$
- $x \oplus y' = x' \oplus y = (x \oplus y)'$
-  Using NAND gate: NAND(NAND(x, y'), NAND(x', y))

Eg. $A \oplus B$
AB \ CD | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**00** | 0 | 0 | 0 | 0
**01** | 1 | 1 | 1 | 1
**11** | 1 | 1 | 1 | 1
**10** | 0 | 0 | 0 | 0

$A \oplus B \oplus C$
AB \ CD | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**00** | 0 | 0 | 1 | 1
**01** | 1 | 1 | 0 | 0
**11** | 0 | 0 | 1 | 1
**10** | 1 | 1 | 0 | 0

$A \oplus B \oplus C \oplus D$
AB \ CD | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**00** | 0 | 1 | 0 | 1
**01** | 1 | 0 | 1 | 0
**11** | 0 | 1 | 0 | 1
**10** | 1 | 0 | 1 | 0



## 17th May
### Combinatorial Logic Circuits
Interconnection of logic gates to accomplish a logic operation
- Binary addition
- Binary subtraction
- Binary multiplication
- Comparison between binary numbers
- Encoding, decoding, etc.

**Design Procedure**
1. Determine number of inputs and outputs
2. Derive truth table
3. Obtain simplified Boolean expressions
4. Implement logic circuit

#### Half-adder
Carries out binary addition of two binary inputs

x | y | | c | s
-- | -- |--| -- | --
0 | 0 || 0 | 0
0 | 1 || 0 | 1
1 | 0 || 0 | 1
1 | 1 || 1 | 0

$s = x \oplus y$
$c  = x y$

#### Full Adder

x | y | z| | c | s
-- | -- |--|--| -- | --
0 | 0 |0|| 0 | 0
0 | 0 |1|| 0 | 1
0 | 1 |0|| 0 | 1
0 | 1 |1|| 1 | 0
1 | 0 |0|| 0 | 1
1 | 0 |1|| 1 | 0
1 | 1 |0|| 1 | 0
1 | 1 |1|| 1 | 1

K-map
x/yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0**|0|1|0|1 
**1**|1|0|1|0

$s = xy'z' + x' y z' + x'y'z + xyz= z' (x \oplus y) + z((x \oplus y)') = (x \oplus y) \oplus z$

x/yz | 00 | 01 | 11 | 10
-- | -- | -- | -- | --
**0**|0|0|1|0 
**1**|0|1|1|1

$c = xy + x'yz + xy'z = xy + z (x \oplus y)$

> We can just use the XOR used in s for c

**Full Adder-> 2 Half Adder + OR gate**

#### 4-bit adder
**Ripple Carry adder**
Augend + Addend

Output carry of ones place becomes input to next digit
Output carry of twos place becomes input to fours digit, etc.

![600](../Images/Pasted%20image%2020220517084200.png)

> [!failure] Problems with this method
> We have to do this sequentially, one by one, so it takes time. We have to wait for the carry

**Carry look ahead logic**
$C_{i + 1} = A_{i}B_{i} + C_i (A_i \oplus B_i)$
Carry Generate -> $G_{i}= A_i B_i$
Carry Propagate -> $P_{i} = (A_{i} \oplus B_i)$

$C_0$ -> Input carry
$C_1$ -> $G_{0}+ P_{0} C_0$
$C_2$ -> $G1 + P1 G_{0} + P_{1} P_{0} C_0$
$C_3$ -> $G_{2}+ P_{2} G_{1} + P_{2}P_{1}G_{0}+ P_{2}P_{1}P_{0}C_0$

#### Binary Subtraction
+49 ->00110001
-49  ->1s: 11001110 -> Accomplished by XOR gate
           2s: 11001111 -> Can be done using initial carry $C_0$

Extra sign bit **M** -> M = 0, add; M = 1, subtract

![](../Images/Pasted%20image%2020220517132541.png)

70 -> 01000110
80 -> 01010000
**10010110**
=150

2s complement of this:
**01101010**
So, we actually get -106

-70 -> 10111010
-80 -> 10110000
**01101010   (C8 = 1) -> 106**

If $\text{Overflow Bit} = V = C_{4} \oplus C_{3}$ = 0 -> Correct
Else -> Wrong

Eg.
M ->0
A -> 1000
B -> 1001
        **(1)0001**
Carry bits are 0 and 1
A + B -> 0001, overflow is there

Eg. 1100, 1000

1100
0111
0001
**(1)0100**
Carry bits are 1, 1, so there is NO overflow

#### Binary Multiplication
Multiplicand -> B1 B0
Multiplier -> A1 A0

B1 B0
A1 A0

P0 = A0B0
P1 =  A0B1 + A1B0
P2 = Carry + A1B1
P3

2x2 multiplication ->4 AND gates and 2 HA

