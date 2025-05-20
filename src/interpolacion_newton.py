import numpy as np
import matplotlib.pyplot as plt

def diferencias_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1]) / (x[j:n] - x[j - 1])
    return coef

def evaluar_newton(x, coef, t):
    n = len(coef)
    p = coef[n - 1]
    for k in range(1, n):
        p = coef[n - k - 1] + (t - x[n - k - 1]) * p
    return p

def interpolar_newton(x, y):
    coef = diferencias_divididas(x, y)
    t_vals = np.linspace(min(x), max(x), 200)
    y_vals = [evaluar_newton(x, coef, t) for t in t_vals]

    plt.figure()
    plt.plot(t_vals, y_vals, label='Interpolación de Newton', color='orange')
    plt.plot(x, y, 'bo', label='Datos')
    plt.xlabel('Días')
    plt.ylabel('Altura (cm)')
    plt.title('Interpolación de Newton')
    plt.legend()
    plt.grid(True)
    plt.show()
