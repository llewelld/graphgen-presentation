import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#data = np.loadtxt("data.txt")
data = np.loadtxt("automark.txt")
x, y = np.meshgrid(np.arange(0,40,1), \
                   np.arange(0,40,1))
fig1 = plt.figure(figsize=(10, 8))

ax1 = fig1.gca(projection='3d')

#ax1.set_title("Optimisation")
#ax1.set_xlabel("Threshold $a$")
#ax1.set_ylabel("Threshold $b$")
#ax1.set_zlabel("Error")
ax1.set_title("Optimisation of indentation mark allocation\nFor indentation errors $e$, score $s = (0.5 * (e < a)) + (0.5 * (e < b))$")
ax1.set_xlabel("Threshold $a$")
ax1.set_ylabel("Threshold $b$")
ax1.set_zlabel("Error $\sigma^2$ of calculated vs. actual")


ax1.plot_surface(x, y, data, \
  cstride=1, rstride=1, cmap='rainbow')

ax1.view_init(35, 15)

#plt.savefig("fig.pdf", format="pdf")
plt.savefig("automark01.pdf", format="pdf", transparent=True, bbox_inches='tight', pad_inches=0)

