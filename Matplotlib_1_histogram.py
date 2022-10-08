"""
Matplotlib - wykres kolumnowy
"""


import matplotlib.pyplot as plt     # 1
import numpy as np                  # 2


# Ćwiczenie nr _______1 _______ 

def wykres_histogram(x, y , xx, yy):
    plt.hist(x, y,  color='b', rwidth=0.98)
    plt.xlabel(f'{xx}')
    plt.ylabel(f'{yy}')
    plt.title(f'{wykres_histogram.__name__.title()}')
    plt.legend(f'Legenda')
    plt.show()
   
x = list(range(1, 100))
y = [1, 3, 6, 10, 55, 70, 80, 90, 100] # przedziały histogramu

wykres_histogram(x, y, 'x', 'y')