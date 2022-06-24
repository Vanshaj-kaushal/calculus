import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return x*x


x = np.arange(-10, 10, 0.1)
y = func(x)
plt.plot(x, y)

plt.title("SQUARE FUNCTION")
plt.show()
