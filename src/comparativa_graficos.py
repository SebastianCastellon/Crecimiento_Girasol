import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline
from regresion_logistica import modelo_logistico
from scipy.optimize import curve_fit

def graficar_comparativa(x, y):
    t_vals = np.linspace(min(x), max(x), 200)

    # Lagrange
    pol_lagrange = lagrange(x, y)
    y_lagrange = pol_lagrange(t_vals)

    # Splines
    spline = CubicSpline(x, y)
    y_spline = spline(t_vals)

    # Regresión logística
    from scipy.optimize import curve_fit
    popt, _ = curve_fit(lambda t, a, b: modelo_logistico(t, a, b), x, y)
    y_logistica = modelo_logistico(t_vals, *popt)

    # Gráfico
    plt.figure()
    plt.plot(t_vals, y_lagrange, label='Lagrange', linestyle='--')
    plt.plot(t_vals, y_spline, label='Splines', linestyle='-.')
    plt.plot(t_vals, y_logistica, label='Logística', linestyle='-')
    plt.plot(x, y, 'ko', label='Datos')
    plt.xlabel('Días')
    plt.ylabel('Altura (cm)')
    plt.title('Comparativa de Métodos')
    plt.legend()
    plt.grid(True)
    plt.show()
