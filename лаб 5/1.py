import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
x = np.arange(xmin, xmax, round((xmax-xmin)/100, 2))
 
plt.plot(x,x**2 - 1)
plt.plot(x, x**2 - 8*x + 15)
plt.plot(x, -x**2 + 4*x)

plt.grid(True)
plt.legend(['x**2 - 1', 'x**2 - 8*x + 15', '-x**2 + 4*x'] )
plt.show()

plt.plot(x, (x**2 - 6*x + 10)*(x>=1) + (x + 2)*(x<1))
plt.grid(True)
plt.show()