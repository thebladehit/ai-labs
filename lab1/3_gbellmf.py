import numpy as np
import matplotlib.pyplot as plt

def gbellmf(x, a, b, c):
    return 1 / (1 + np.abs((x - c) / a) ** (2 * b))

x = np.linspace(0, 10, 100)

a, b, c = 1, 4, 4
y = gbellmf(x, a, b, c)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
