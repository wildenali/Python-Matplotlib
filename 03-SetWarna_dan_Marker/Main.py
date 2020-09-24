import numpy as np
import matplotlib.pyplot as plt

"""
Step-step membuat plot
1. Membuat data
2. Membuat plot
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
print(t1)
print(y1)
plt.plot(t1, y1)

# 3. Menampilkan plot
plt.show()
