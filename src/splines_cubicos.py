import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def interpolar_spline(x, y):
    spline = CubicSpline(x, y)
    t_vals = np.linspace(min(x), max(x), 200)
    y_vals = spline(t_vals)

    plt.figure()
    plt.plot(t_vals, y_vals, label='Splines Cúbicos', color='purple')
    plt.plot(x, y, 'ko', label='Datos')
    plt.xlabel('Días')
    plt.ylabel('Altura (cm)')
    plt.title('Interpolación con Splines Cúbicos')
    plt.legend()
    plt.grid(True)
    plt.show()
