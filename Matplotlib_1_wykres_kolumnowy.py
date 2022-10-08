"""
Matplotlib - wykres kolumnowy
"""


import matplotlib.pyplot as plt     # 1
import numpy as np                  # 2


# Ćwiczenie nr _______1 _______ 

def wykres_kolumnowy(x, y , xx, yy):
    plt.bar(x, y,  color='r', )
    plt.xlabel(f'{xx}')
    plt.ylabel(f'{yy}')
    plt.title(f'{wykres_kolumnowy.__name__}')
    plt.legend(f'Legenda')
    plt.show()
   
x = list(range(1, 10))
y = list(range(2, 20, 2))

wykres_kolumnowy(x, y, 'x', 'y')
