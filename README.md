# Análisis de Crecimiento de Helianthus annuus (Girasol)

**Autor:**  
- Castellon Gutierrez Sebastian Dennis

---

## Descripción

Este repositorio contiene el código completo en Python para:

1. **Interpolación de Newton**  
2. **Interpolación de Lagrange**  
3. **Splines cúbicos naturales**  
4. **Regresión no lineal** (modelo logístico)

sobre el conjunto de datos de crecimiento de un girasol (_Helianthus annuus_) obtenido de:

> Motulsky, H. (2003). *Intuitive Biostatistics: A Nonmathematical Guide to Statistical Thinking*. Capítulo “Growth curves in biology”, Oxford University Press.

---

## Estructura del proyecto

PLANTA_CRECIIMIENTO/
│
├── datos/
│ └── girasol_motulsky.csv # Datos de crecimiento (días vs altura)
│
├── reporte/
│ └── reporte_final.pdf # Informe en PDF con resultados
│
├── src/
│ ├── main.py # Script principal (ejecutar este)
│ ├── utils.py # Carga y visualización de datos
│ ├── interpolacion_lagrange.py # Interpolación por Lagrange
│ ├── interpolacion_newton.py # Interpolación de Newton
│ ├── splines_cubicos.py # Interpolación con Splines cúbicos
│ ├── regresion_logistica.py # Ajuste con modelo logístico
│ └── comparativa_graficos.py # Muestra todos los gráficos

- **`datos/girasol_motulsky.csv`**: Archivo CSV con los datos de días (`t`) y altura en cm (`h`).  
- **`src/utils.py`**: Funciones auxiliares para cargar datos, diferencias divididas y polinomio de Lagrange.  
- **`src/interpolacion_newton.py`**: Script que construye y grafica el polinomio de Newton.  
- **`src/interpolacion_lagrange.py`**: Script que construye y grafica el polinomio de Lagrange.  
- **`src/splines_cubicos.py`**: Script que construye y grafica la interpolación con splines cúbicos naturales.  
- **`src/regresion_logistica.py`**: Script que ajusta un modelo logístico a los datos y grafica el ajuste.  
- **`src/comparativa_graficos.py`**: Script que genera un solo gráfico comparando los cuatro métodos.  
- **`reporte/reporte_final.pdf`**: Documento PDF con resumen de resultados y conclusiones (tú lo generarás y colocarás aquí).

---

## Instrucciones paso a paso para ejecutar el código


---

## ▶️ ¿Cómo ejecutar el programa?

1. Asegúrate de tener **Python instalado (3.9+ recomendado)**.
2. Instala las librerías necesarias con:

pip install -r "numpy
pandas
matplotlib
scipy"
Corre el archivo principal:

bash
Copiar
Editar
python src/main.py
Esto abrirá automáticamente todos los gráficos comparando métodos de interpolación y la regresión logística.

📈 Métodos aplicados
Interpolación de Newton

Interpolación de Lagrange

Interpolación con Splines cúbicos

Regresión logística (modelo de crecimiento biológico)

Comparativa gráfica de todos los métodos


