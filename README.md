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

plant-growth-analysis/
│
├── README.md
├── datos/
│ └── girasol_motulsky.csv
├── src/
│ ├── utils.py
│ ├── interpolacion_newton.py
│ ├── interpolacion_lagrange.py
│ ├── splines_cubicos.py
│ ├── regresion_logistica.py
│ └── comparativa_graficos.py
└── reporte/
└── reporte_final.pdf


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

1. **Entrar a la carpeta del proyecto**  
   ```bash
   cd /ruta/a/plant-growth-analysis
