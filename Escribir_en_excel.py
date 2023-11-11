import openpyxl
from openpyxl.styles import Border,Side

#Cargamos documento
libro = openpyxl.load_workbook("Vehiculos.xlsx")

#Abrimos la hoja de excel
hoja = libro['Listado']

#Encabezados de la hoja de excel
hoja ['A1'].value = "Codigo"
hoja ['B1'].value = "Marca"
hoja ['C1'].value = "Modelo"
hoja ['D1'].value = "Precio"
hoja ['E1'].value = "Kilometraje"
hoja ['F1'].value = "CantidadFotos"




datos_de_entrada = [
  {  
        "Codigo": "CITY01",
        "Marca": "HONDA",
        "Modelo": "2020",
        "Precio": "80000",
        "Kilometraje": "600",
        "CantidadFotos": "5",
    },
    
    { 
        "Codigo": "CIVIC01",
        "Marca": "HONDA",
        "Modelo": "2021",
        "Precio": "2021",
        "Kilometraje": "0",
        "CantidadFotos": "3",


    }


]
#Nos posicionamos en la fila 2 de excel:
proxima_fila = hoja.max_row + 1

for mantenimiento_vehiculos in  datos_de_entrada:
    hoja[f'A{proxima_fila}'].value = mantenimiento_vehiculos["Codigo"]
    hoja[f'B{proxima_fila}'].value = mantenimiento_vehiculos["Marca"]
    hoja[f'C{proxima_fila}'].value = mantenimiento_vehiculos["Modelo"]
    hoja[f'D{proxima_fila}'].value = mantenimiento_vehiculos["Precio"]
    hoja[f'E{proxima_fila}'].value = mantenimiento_vehiculos["Kilometraje"]
    hoja[f'F{proxima_fila}'].value = mantenimiento_vehiculos["CantidadFotos"]
    proxima_fila +=1

#guardamos el archivo
libro.save("vehiculos.xlsx")