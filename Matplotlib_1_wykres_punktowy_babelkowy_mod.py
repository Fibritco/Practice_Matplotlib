"""
Matplotlib - wykres punktowy - bąbelkowy mod
colors:  https://matplotlib.org/stable/gallery/color/named_colors.html
"""



from matplotlib import colors as mcolors
import matplotlib.pyplot as plt     # 1
import numpy as np                  # 2
from random import randint          # 3



# Ćwiczenie nr _______1 _______ 

def wykres_punktowy(x, y, z, xx, yy):
    plt.scatter(x, y, s=z,  c=['r', 'b', 'm', 'g', 'y'], marker='o', cmap='Blues', edgecolors="black", alpha=1.0)  # s = size determine bubbles
    plt.xlabel(f'{xx}')
    plt.ylabel(f'{yy}')
    plt.title(f'{wykres_punktowy.__name__}')
    plt.legend(f'Legenda')
    plt.show()
   
x = ['musztarda', 'majonez', 'ziemniaczki', 'sól', 'pomarańcza']
y = [2, 8, 1, 10, 8]
z = [randint(1, 400) for i in range(5)]  #  random bublle size

wykres_punktowy(x, y, z, 'x', 'y')