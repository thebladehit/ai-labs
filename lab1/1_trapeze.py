import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_np(x, a, b, c, d):
    return np.clip(np.minimum(np.minimum((x - a) / (b - a), (d - x) / (d - c)), 1), 0, 1)

def trapezoidal_manual(x, a, b, c, d):
    res = []
    for element in x:
        if element < a:
            res.append(0)
        elif element > d:
            res.append(0)
        elif a <= element <= b:
            res.append((element - a) / (b - a))
        elif b < element <= c:
            res.append(1)
        elif c < element <= d:
            res.append((d - element) / (d - c))
    return res


x = np.linspace(0, 10, 100)

a, b, c, d = 1, 2, 7, 9
y = trapezoidal_np(x, a, b, c, d)

plt.plot(x, y, label=f'Trapezoidal MF ({a}, {b}, {c}, {d})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trapezoidal Membership Function')
plt.legend()
plt.grid(True)
plt.show()
