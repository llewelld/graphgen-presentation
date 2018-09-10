import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("strange.txt")

fig1 = plt.figure(figsize=(6.5, 8))

ax1 = fig1.gca()

ax1.set_title("Strange Attractor")
ax1.set_xlabel("Time")
ax1.set_ylabel("x position")

ax1.plot(data[:,0], data[:,1])

plt.savefig("strange01.pdf", format="pdf", transparent=True, bbox_inches='tight', pad_inches=0)

