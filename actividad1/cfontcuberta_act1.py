""" Implemente un programa que lea el contenido del fichero y realice los
    siguientes cálculos:
● ¿Qué mes se ha gastado más?
● ¿Qué mes se ha ahorrado más?
● ¿Cuál es la media de gastos al año?
● ¿Cuál ha sido el gasto total a lo largo del año?
● ¿Cuáles han sido los ingresos totales a lo largo del año?
● Opcional: Realice una gráfica de la evolución de ingresos a lo largo del año
"""
# Importacion de las librerias

from msilib import type_string, type_valid
from numpy import dtype
import pandas as pd
import os

#import matplotlib.pyplot as plt

# definicion de la ruta del archivo
MEDIA_ROOT = os.path.expanduser("~/Desktop/Buenas/actividad1/finanzas2020.csv")

# lectura dek archivo en caso de error ejecuta la excepcion
try:    
    datos = pd.read_csv(MEDIA_ROOT, sep='\s+', engine='python',header=0)
except IOError:
        print("error al abrir el archivo")
else:
    print("Lectura exitosa del Archivo")
# si todo salio bien se muestra el datafrae
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(datos)

#  definicion de la variable total donde se  almacenan los ingresos y egreso


# rutina para Validar los datos

try:
    for c in range(11):
        for f in  range(98):
            celda = datos.iloc[f,c]             
            type(celda)           
            if type(celda) == "str":
                celda = 0
            datos.iloc[f,c] = float(celda)                     
except ValueError:
         print(f"dato invalido {datos.iloc[f,c]}")


Total1 = datos{"Enero"].sum()





        



