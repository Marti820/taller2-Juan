var = 12
nuevo_cambio = 12
aaa=1e12

# Modificación del sagrado rostro

import numpy as np

lamb = 22

n = 1000

vals = np.random.exponential(scale = 1/lamb, size =n)

import matplotlib.pyplot as plt

count, bins, ignored = plt.hist(x=vals, bin = 30)
plt.title("Histograma Distribución Exponencial de Martin")
plt.xlabel("Tiempos Entre Arribos")
plt.ylabel("Frecuencia")
plt.show()