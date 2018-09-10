import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.loadtxt("strange.txt")

fig1 = plt.figure(figsize=(9, 8))

ax1 = fig1.gca(projection='3d')

ax1.set_title("Strange Attractor")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

ax1.plot(data[:,1], data[:,2], data[:,3])

plt.savefig("strange03.pdf", format="pdf", transparent=True, bbox_inches='tight', pad_inches=0)
