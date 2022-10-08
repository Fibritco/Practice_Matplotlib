"""
Matplotlib - wykres liniowy
"""

import matplotlib.pyplot as plt
import numpy as np


# Ćwiczenie nr _______1 ________
f = np.linspace(-10, 10)
plt.plot(f, f + 5, label='linear')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres')
plt.show()
