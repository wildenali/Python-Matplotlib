import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

# Inisialisai plot
plt.plot(x, y)

# tampilkan
plt.show()

# Membuat lingkaran
PI = np.pi
sudut = np.linspace(0, 2*PI, 100)
radius = 5
x = radius * np.cos(sudut)
y = radius * np.sin(sudut)
# inisialisasi plot
plt.plot(x, y)
# tampilkan
plt.show()
