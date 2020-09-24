import numpy as np
import matplotlib.pyplot as plt

"""
Step-step membuat plot
1. Membuat data
2. Membuat plot
    - Setting axis
3. Menampilkan plot
"""

# 1. Membuat data
# Rumus sinusoidal = sin(2wt + theta)


def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t, y


# 2. Membuat Plot
t1, y1 = sinusGenerator(1, 1, 4, 0)
dataPlot1 = plt.plot(t1, y1)

# setting axis, minimum dan maximum
# plt.axis([xmin, xmax, ymin, ymax])
# plt.axis([0, 4, -1, 1])
# plt.axis([0, 4, -2, 1])
# plt.axis([0, 4, -1, 2])
plt.axis([0, 4, -2, 2])

# 3. Menampilkan plot
plt.show()
