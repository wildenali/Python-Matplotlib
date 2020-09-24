import numpy as np
import matplotlib.pyplot as plt

"""
Step-step membuat plot
1. Membuat data
2. Membuat plot
    - Label and Title
3. Menampilkan plot
"""

# 1. Membuat data
# Rumus sinusoidal = sin(2wt + theta)


def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t, y


amplitudo = 1
frekuensi = 1
theta = 0
tAkhir = 4
# 2. Membuat Plot
t, y = sinusGenerator(amplitudo, frekuensi, tAkhir, theta)
plt.plot(t, y)

judul = 'Grafik Sinusiodal\n'
rumus = r'$ \mathcal{Y} = A.sin(2 \omega t + \theta) $' + '\n'
parameter1 = r'$ A = $' + str(amplitudo) + ' cm, '
parameter2 = r'$ \omega = $' + str(frekuensi) + r'$ \mathit{Hz}$' + ', '
parameter3 = r'$ \theta = $' + str(theta) + r'$^{o} $'

plt.title(judul + rumus + parameter1 + parameter2 + parameter3)
plt.xlabel('waktu(detik)')
plt.ylabel('magnitude(cm)')

# 3. Menampilkan plot
plt.show()
