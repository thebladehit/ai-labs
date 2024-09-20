import numpy as np
import matplotlib.pyplot as plt

def triangle_np(x, a, b, c):
    return np.clip(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0, 1)

def triangle_manual(x, a, b, c):
    res = []
    for element in x:
        if element < a:
           res.append(0)
        elif element > c:
            res.append(0)
        elif a <= element <= b:
            res.append((element - a) / (b - a))
        elif b <= element <= c:
            res.append((c - element) / (c - b))
    return res

x = np.linspace(0, 10, 100)

a, b, c = 2, 5, 7
y = triangle_np(x, a, b, c)

plt.plot(x, y, label=f'Triangular MF ({a}, {b}, {c})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
