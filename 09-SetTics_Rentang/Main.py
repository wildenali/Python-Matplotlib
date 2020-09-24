import numpy as np
import matplotlib.pyplot as plt

"""
Step-step membuat plot
1. Membuat data
2. Membuat plot
    - Set Ticks
3. Menampilkan plot
"""

# 1. Membuat data
sudut = np.arange(0, 360, 1)
y = np.sin(np.deg2rad(sudut))

# 2. Membuat Plot
plt.plot(sudut, y)
plt.ylabel("magnituda")
plt.xlabel("sudut")

# set ticks
plt.yticks([-1, 0, 0.5, 1])
# plt.xticks([0, 90, 180, 270, 360])
plt.xticks(
    [0, 90, 180, 270, 360],
    [r'${0}^o$', r'${90}^o$', r'${18}^o$', r'${270}^o$', r'${260}^o$']
)

# 3. Menampilkan plot
plt.show()
