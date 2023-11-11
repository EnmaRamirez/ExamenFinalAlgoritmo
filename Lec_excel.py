import openpyxl

libro = openpyxl.load_workbook("vehiculos.xlsx")
hoja = libro['Listado']

#ejemplo de como obtener los datos
#print(hoja['A2'].value)
def mantenimiento_vehiculos():
    Lista_de_alumnos =[]

    for numero_fila in range(2, hoja.max_row +1):
        mantenimiento_vehiculos.append({
            "Codigo": hoja[f"A{numero_fila}"].value,
            "Marca": hoja[f"B{numero_fila}"].value,
            "Modelo": hoja[f"C{numero_fila}"].value,
            "Precio": hoja[f"D{numero_fila}"].value,
            "Kilometraje": hoja[f"E{numero_fila}"].value,
            "CantidadFotos": hoja[f"E{numero_fila}"].value

           
            

        })

    print(mantenimiento_vehiculos)


mantenimiento_vehiculos()

