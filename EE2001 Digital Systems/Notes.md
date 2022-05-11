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
