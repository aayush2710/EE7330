import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

C1 = 1 - (-x*np.log2(x) - (1-x)*np.log2(1-x))
print(1 - (-0.1*np.log2(0.1) - (1-0.1)*np.log2(1-0.1)))
C2 = 1 - x
C1[0] = 1
C1[-1] = 1
plt.plot(x, C1, label="BSC")
plt.plot(x, C2, label="BEC")
plt.grid()
plt.legend()
plt.show()