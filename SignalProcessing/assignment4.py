import matplotlib.pyplot as plt
import numpy as np

w = 10
Y = 10
# r = np.linspace(0, 10, 11, endpoint=True)
r = 10
x = np.linspace(-10,10, 1000)
y_posi = np.sqrt(r**2-x**2)
y_nega = -np.sqrt(r**2-x**2)
plt.plot(x, y_posi,c="k")
plt.plot(x, y_nega,c="k")
plt.show()