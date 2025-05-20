import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def modelo_logistico(t, a, b, H=102):
    return H / (1 + np.exp(-(a + b * t)))

def ajustar_regresion_logistica(x, y):
    popt, _ = curve_fit(lambda t, a, b: modelo_logistico(t, a, b), x, y)
    a, b = popt
    print(f"Parámetros de regresión logística: a = {a:.4f}, b = {b:.4f}")

    t_vals = np.linspace(min(x), max(x), 200)
    y_vals = modelo_logistico(t_vals, a, b)

    plt.figure()
    plt.plot(t_vals, y_vals, label='Regresión Logística', color='blue')
    plt.plot(x, y, 'mo', label='Datos')
    plt.xlabel('Días')
    plt.ylabel('Altura (cm)')
    plt.title('Ajuste de Regresión Logística')
    plt.legend()
    plt.grid(True)
    plt.show()
