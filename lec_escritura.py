
import openpyxl
import sys

libro = openpyxl.load_workbook(sys.argv[1])
hoja = libro['Listado']

#Fila donde encontramos el ID
fila_encontrada = 0
for numero_fila in range(2, hoja.max_row + 1):
    if hoja[f'A{numero_fila}'].value == int(sys.argv[3]):
        fila_encontrada = numero_fila
        break

if fila_encontrada > 0:
    hoja[f'B{fila_encontrada}'].value = sys.argv[4]
    hoja[f'C{fila_encontrada}'].value = sys.argv[5]
    hoja[f'D{fila_encontrada}'].value = sys.argv[6]
    hoja[f'E{fila_encontrada}'].value = sys.argv[7]
    hoja[f'F{fila_encontrada}'].value = sys.argv[8]
else:
    print("ventana no encontrada")

#Guardamos nuestro archivo
libro.save(sys.argv[1])