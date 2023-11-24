from cmath import *
from tabulate import tabulate
from matplotlib import pyplot as plt
import numpy as np

R = [0.02, 0.1, 0.4, 1, 1.4, 2, 5, 10, 20, 100]

L = 1e-5
C = 1e-5

w_n = sqrt(1/(L * C))

def eta(R):
    return R/2 * sqrt(C/L)

def Q(R):
    return 1/(2 * eta(R))

def s_1(R):
    return w_n * (-eta(R) + sqrt(eta(R)**2 - 1))

def s_2(R):
    return w_n * (-eta(R) - sqrt(eta(R)**2 - 1))

lis = [[r, eta(r), Q(r), s_1(r), s_2(r), abs(s_1(r)), abs(s_2(r))] for r in R]

print(tabulate(lis, headers = ["R", "eta", "Q", "s1", "s2", "abs(s1)", "abs(s2)"]))

x1 = []
y1 = []
x2 = []
y2 = []

for i in range(len(R)):
    x1.append(lis[i][3].real)
    y1.append(lis[i][3].imag)

plt.axvline(x = 0, alpha = 0.3)
plt.axhline(y = 0, alpha = 0.3)
plt.plot(x1, y1, 'o', alpha = 0.7)

for i in range(len(R)):
    x2.append(lis[i][4].real)
    y2.append(lis[i][4].imag)

plt.plot(x2, y2, 'o', alpha = 0.7)

plt.legend(["x-axis", "y-axis", "s1", "s2"])
plt.show()

gm1 = 1e-4
gm2 = 1e-4
r1 = 1e6
r2 = 1e6

A0 = gm1 * gm2 * r1 * r2

# Open loop
# (s * c1 + 1/r1) * (s * c2 + 1/r2)

def loopgain(s, c1, c2):
    return gm1 * gm2 / ((s * c1 + 1/r1) * (s * c2 + 1/r2))

def loopgain_w1(c1, c2):
    return 1/(r1 * c1)

def loopgain_w2(c1, c2):
    return 1/(r2 * c2)

def w_ugf(c1, c2):
    w_sq = (np.sqrt((r1 **2 * c1 **2 + r2 **2 * c2 **2)**2 - 4 * (r1 * r2 * c1 * c2)**2 * (1 - (gm1 * r1 * gm2 * r2)**2)) - (r1 **2 * c1 **2 + r2 **2 * c2 **2))/(2 * ((r1 * r2 * c1 * c2)**2))
    return np.sqrt(w_sq)

def phase_margin(c1, c2):
    return 180 / np.pi * (np.pi - np.arctan(w_ugf(c1, c2)/loopgain_w1(c1, c2)) - np.arctan(w_ugf(c1, c2)/loopgain_w2(c1, c2)))

# Closed loop

def eta(c1, c2):
    return (1/(2 * sqrt(gm1 * gm2 * r1 * r2))) * (sqrt((r2 * c2)/(r1 * c1)) + sqrt((r1 * c1)/(r2 * c2)))

def Q(c1, c2):
    return 1 / (2 * eta(c1, c2))

def pole1(c1, c2):
    p1 = 1/(r1 * c1)
    p2 = 1/(r2 * c2)
    A0 = gm1 * gm2 * r1 * r2
    return ((-(p1 + p2) + sqrt(p1**2 + p2**2 + 2 * p1 * p2 - 4 * p1 * p2 * A0))/(2))

def pole2(c1, c2):
    p1 = 1/(r1 * c1)
    p2 = 1/(r2 * c2)
    A0 = gm1 * gm2 * r1 * r2
    return ((-(p1 + p2) - sqrt(p1**2 + p2**2 + 2 * p1 * p2 - 4 * p1 * p2 * A0))/(2))

C = np.array([[1e-9, 1e-9], [1e-8, 1e-10], [4e-8, 2.5e-11], [1e-7, 1e-11], [1.41e-7, 7.07e-12], [2e-7, 5e-12], [5e-7, 2e-12], [1e-6, 1e-12], [2e-6, 5e-13], [1e-5, 1e-13]])

liss = [[c1, c2, loopgain_w1(c1, c2), loopgain_w2(c1, c2), w_ugf(c1, c2), phase_margin(c1, c2), eta(c1, c2), Q(c1, c2), abs(pole1(c1, c2)), abs(pole2(c1, c2))] for (c1, c2) in C]
liss = np.array(liss)

print(tabulate(liss, headers = ["c1", "c2", "w1", "w2", "wug", "pm", "eta", "Q", "pole1", "pole2"]))

p1_real = []
p2_real = []
p1_cl_real = []
p1_cl_complex = []
p2_cl_real = []
p2_cl_complex = []

pole1 = np.vectorize(pole1)
pole2 = np.vectorize(pole2)
loopgain_w1 = np.vectorize(loopgain_w1)
loopgain_w2 = np.vectorize(loopgain_w2)
eta = np.vectorize(eta)
phase_margin = np.vectorize(phase_margin)

loopgain_w1_real = -loopgain_w1(C[:, 0], C[:, 1])
loopgain_w1_complex = -loopgain_w1(C[:, 0], C[:, 1]) * 0

loopgain_w2_real = -loopgain_w2(C[:, 0], C[:, 1])
loopgain_w2_complex = -loopgain_w2(C[:, 0], C[:, 1]) * 0

p1_real = pole1(C[:, 0], C[:, 1])
p1_complex = pole1(C[:, 0], C[:, 1]).imag

p2_real = pole2(C[:, 0], C[:, 1]).real
p2_complex = pole2(C[:, 0], C[:, 1]).imag

plt.axvline(x = 0, alpha = 0.3)
plt.axhline(y = 0, alpha = 0.3)
plt.plot(loopgain_w1_real, loopgain_w1_complex, '.', alpha = 0.8)
plt.plot(loopgain_w2_real, loopgain_w2_complex, '.', alpha = 0.8)
plt.plot(p1_real, p1_complex, '.', alpha = 0.8)
plt.plot(p2_real, p2_complex, '.', alpha = 0.8)
plt.legend(["x-axis", "y-axis", "p1", "p2", "s1", "s2"])

plt.show()

eta_array = eta(C[:7, 0], C[:7, 1])
phase_margin_array = phase_margin(C[:7, 0], C[:7, 1])

plt.plot(eta_array, phase_margin_array, 'o-')

x_values = np.linspace(0, eta_array[-1], 100)
plt.plot(x_values, x_values * 100)
plt.plot(x_values, x_values * 90)
plt.plot(x_values, x_values * 110)

plt.legend(["Theoretical Curve", "PM = 100 * damping factor", "PM = 90 * damping factor", "PM = 110 * damping factor"])

plt.show()