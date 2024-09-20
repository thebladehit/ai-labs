import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

x = np.linspace(0, 10, 100)
y = fuzz.sigmf(x, 5, 5)
y2 = fuzz.smf(x, 1, 5)
y3 = fuzz.pimf(x, 1, 2, 3, 5)

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()