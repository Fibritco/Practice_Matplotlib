"""
Matplotlib - wykres kolowy
https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
"""



import matplotlib.pyplot as plt     # 1
import numpy as np                  # 2


# Ćwiczenie nr _______1 _______  


x = [10, 10, 80]
y = ['Chemia', 'Biologia', 'Python']
explode = (0.2, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

def wykres_kolowy(x, y):
    plt.pie(x, explode=explode, labels=y, autopct='%1.3f%%',
        shadow=True, startangle=90)
    plt.title(f'{wykres_kolowy.__name__.title()}')
    plt.show()
   
wykres_kolowy(x, y)