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

# Ubah warna
t2, y2 = sinusGenerator(1, 1, 4, 30)
plt.plot(t2, y2, 'r')

#  Pakai Marker
t3, y3 = sinusGenerator(1, 1, 4, 60)
plt.plot(t3, y3, 'b--')

#  Pakai Marker
t4, y4 = sinusGenerator(1, 1, 4, 90)
plt.plot(t4, y4, 'c-o')

# 3. Menampilkan plot
plt.show()


# Untuk marker sama warna yg tersedia cek di github atau link lainnya
