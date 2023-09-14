import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 300)
y1 = x**2
plt.plot(x,y1, color="r")
plt.grid()

plt.show()
