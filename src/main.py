from utils import cargar_datos, mostrar_datos
from interpolacion_newton import interpolar_newton
from interpolacion_lagrange import interpolar_lagrange
from splines_cubicos import interpolar_spline
from regresion_logistica import ajustar_regresion_logistica
from comparativa_graficos import graficar_comparativa

if __name__ == "__main__":
    x, y = cargar_datos()
    mostrar_datos(x, y)

    print("\n--- Interpolación de Newton ---")
    interpolar_newton(x, y)

    print("\n--- Interpolación de Lagrange ---")
    interpolar_lagrange(x, y)

    print("\n--- Interpolación con Splines ---")
    interpolar_spline(x, y)

    print("\n--- Regresión Logística ---")
    ajustar_regresion_logistica(x, y)

    print("\n--- Comparativa ---")
    graficar_comparativa(x, y)
