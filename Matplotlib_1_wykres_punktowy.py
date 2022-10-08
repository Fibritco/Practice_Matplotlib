"""
Matplotlib - wykres punktowy
"""


import matplotlib.pyplot as plt     # 1
import numpy as np                  # 2


# Ćwiczenie nr _______1 _______ dekorator 

def wykres_punktowy(x, y , xx, yy):
    plt.scatter(x, y,  c='r', marker='o', alpha=1.0)
    plt.xlabel(f'{xx}')
    plt.ylabel(f'{yy}')
    plt.title(f'{wykres_punktowy.__name__}')
    plt.legend(f'Legenda')
    plt.show()
   
x = list(range(1, 10))
y = list(range(2, 20, 2))

wykres_punktowy(x, y, 'x', 'y')







