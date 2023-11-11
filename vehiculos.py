print("WELCOME TO MY SALES TRANSACTION PROGRAM".center(80,'_'))
   
Codigo = []
Marca = []
Modelo = []
Precio = []
Kilometraje= []
CantidadFotos= []

while True:
        print("""

        1. Crear vehiculos
        2. Editar vehiculo
        3. Eliminar vehiculo        
        4. Listar vehiculos     
     
        """)

        respuesta = int(input('Ingrese su opcion: '))
        if respuesta == 1:
           
            Añadir_Codigo = int(input('Ingrese el codigo de su producto: '))
            Añadir_Marca = input('Ingrese el Marca de su producto')
            Añadir_Modelo =  int(input('Ingrese modelo de su vehiculo: '))
            Añadir_Precio = input('Ingrese el precio de su vehiculo')
            Añadir_kilometraje =  int(input('Ingrese el kilometraje: '))
            Añadir_CantidadFotos =  int(input('Ingrese cantidad fotos '))

            Codigo.append(Añadir_Codigo)
            Marca.append(Añadir_Marca)
            Modelo.append(Añadir_Modelo)
            Precio.append(Añadir_kilometraje)
            Kilometraje.append(Añadir_Precio)
            CantidadFotos.append(Añadir_CantidadFotos)
        


        elif respuesta == 2:
            crear = input('Ingrese datos que decea crear: ')
            posición = Codigo .index(crear)
              
            print('El codigo del producto es: ', Codigo[posición])
            print('El Marca del producto es: ', Marca[posición])
            print('El modelo del producto es: ', Modelo[posición])
            print('El precio de su hehiculo es: ', Precio[posición])
            print('El kilometraje es: ', Kilometraje[posición])
            print('La cantidad de fotos  es: ', CantidadFotos[posición])
            

     