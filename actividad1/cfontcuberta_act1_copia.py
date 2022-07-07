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
import os
from csv import reader
#import matplotlib.pyplot as plt
# definicion de la ruta del archivo
MEDIA_ROOT = os.path.expanduser("~/Desktop/Buenas/actividad1/finanzas2020.csv")
# lectura dek archivo en caso de error ejecuta la excepcion
ingreso = []
egreso = []
try:
    with open(MEDIA_ROOT, "r") as file:
    # pass the file object to reader()
        datos = reader(file)
except IOError:
        print("error al abrir el archivo")
else:
    print("Lectura exitosa del Archivo")
print(datos)
try:
    for i in datos:
        # Separo ingresos de egresos
            if datos(i) > 0:
                ingreso.append(i)
            else:
                egreso.append(i)
except ValueError:
    print

