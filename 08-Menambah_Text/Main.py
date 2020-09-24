import numpy as np
import matplotlib.pyplot as plt

"""
Step-step membuat plot
1. Membuat data
2. Membuat plot
    - Add Text
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

plt.plot(t1, y1)
# plt.text(2, 1, 'sin(0)')
plt.text(2, 0.5, r'$ y = \mathcal{A}.sin(2 \omega t)$')
plt.text(2, 0.4, r'$ y = \mathcal{A} = 1 cm, \omega = 1 Hz$')

# 3. Menampilkan plot
plt.show()
