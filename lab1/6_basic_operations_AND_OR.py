import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import gaussmf


def And(a, b):
    return np.minimum(a, b)

def Or(a, b):
    return np.maximum(a, b)

x = np.linspace(0, 10, 100)

y1 = gaussmf(x, 3, 1)
y2 = gaussmf(x, 5, 2)

and_result = And(y1, y2)
or_result = Or(y1, y2)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, and_result, )
plt.plot(x, or_result)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
