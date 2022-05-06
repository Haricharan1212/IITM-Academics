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
Two n-digit numbers in base 'r' (prof went in a different order, this order is easier)

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
	- 3  -> 1010
	- -5 -> 0011
	- So, it is offset by one
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

