import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def interpolar_lagrange(x, y):
    pol = lagrange(x, y)
    t_vals = np.linspace(min(x), max(x), 200)
    y_vals = pol(t_vals)

    plt.figure()
    plt.plot(t_vals, y_vals, label='Interpolación de Lagrange', color='green')
    plt.plot(x, y, 'ro', label='Datos')
    plt.xlabel('Días')
    plt.ylabel('Altura (cm)')
    plt.title('Interpolación de Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()
