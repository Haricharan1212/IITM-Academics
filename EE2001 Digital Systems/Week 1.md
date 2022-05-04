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
Signals:
1. Analog
2. Digital signal -> discrete time signal

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

153 | 8
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
