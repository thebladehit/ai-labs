import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

def gaussmf(x, sigma, c):
    return np.exp(-(x-c)**2/(2*sigma**2))

def gauss2mf(x, sigma1, c1, sigma2, c2):
    return fuzz.gauss2mf(x, c1, sigma1, c2, sigma2)

x = np.linspace(0, 10, 100)

y = gaussmf(x, 1, 5)
y2 = gaussmf(x, 2, 4)
# y3 = gauss2mf(x, 1, 3, 1, 4)

plt.plot(x, y)
plt.plot(x, y2)
# plt.plot(x, y3)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()