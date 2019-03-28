import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_knots = np.linspace(-3*np.pi,3*np.pi,201)
y_knots = np.linspace(-3*np.pi,3*np.pi,201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+Y**2)
Z = np.cos(R)**2*np.exp(-0.1*R)
Z1 = np.cos(R*a) ** 2 * np.exp(-0.1 * R + a)


#ax = Axes3D(plt.figure(figsize=(8, 5)))
fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.title("Original graph of the function")
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.title("Changed function graph")
plt.show()
