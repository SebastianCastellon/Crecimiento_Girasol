import pandas as pd

def cargar_datos():
    datos = pd.read_csv('datos/girasol_motulsky.csv')
    print("Columnas encontradas en el CSV:", datos.columns)
    x = datos['dias'].values   # <- cambia esto si ves otro nombre
    y = datos['altura'].values
    return x, y

def mostrar_datos(x, y):
    print("Días:", x)
    print("Alturas:", y)
