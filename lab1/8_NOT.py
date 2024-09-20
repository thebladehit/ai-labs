import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import gaussmf

def Not(y):
    return 1 - y

x = np.linspace(0, 10, 100)

y1 = gaussmf(x, 3, 2)
y2 = Not(y1)

plt.plot(x, y1)
plt.plot(x, y2, linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
