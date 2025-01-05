
#Variables globales

inventario = []
stockMinimo = 15


def menu():
    print()
    print("***  Menu principal  ***")
    print("1. Registrar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Listar productos")
    print("5. Control de stock")
    print("6. Reportes")
    print("0. Salir")
    print()

def menuEditar():
    print()
    print("***  Menu edición  ***")
    print("1. Editar nombre")
    print("2. Editar código")
    print("3. Editar precio")
    print("4. Editar cantidad")
    print("5. Editar stock")
    print("6. Editar todo")
    print()


def inputNumero(texto):
    while True:
        valor = input(texto)
        if valor == "" or valor.isdigit() == False:
            print("Debe ser un valor numerico valido")
        else:
            return valor


def agregarProducto():
    print()
    print("***  Agregar Producto  ***")
    nombre = input("Nombre del producto: ")
    codigo = input("Código del producto: ")
    precio = inputNumero("Precio del producto: ")
    cantidad = inputNumero("Cantidad de producto: ")
    nVentas = inputNumero("Número de ventas del producto: ")

    producto = {
        "nombre": nombre,
        "codigo": codigo,
        "precio": precio,
        "cantidad": cantidad,
        "nVentas": nVentas
    }
    inventario.append(producto)
    print("----------------")

def editarProducto():
    print()
    print("***  Editar Producto  ***")
    if len(inventario) != 0:
        print("Elige el N° de producto que se va a editar")
        listarProductos()
        indice = inputNumero("Seleccionar numero: ")
 
        indice = int(indice)
        paraEditar = inventario[indice-1]

        menuEditar()
        opcion = int(input("Elija una opción: "))

        if(opcion == 1):
            nombre = input("Nombre del producto: ")
            paraEditar["nombre"] = nombre
        elif(opcion == 2):
            codigo = input("Código del producto: ")
            paraEditar["codigo"] = codigo
        elif(opcion == 3):
            precio = inputNumero("Precio del producto: ")
            paraEditar["precio"] = precio
        elif(opcion == 4):
            cantidad = inputNumero("Cantidad de producto: ")
            paraEditar["cantidad"] = cantidad
        elif(opcion == 5):
            nVentas = inputNumero("Número de ventas del producto: ")
            paraEditar["nVentas"] = nVentas
        elif(opcion == 6):
            nombre = input("Nombre del producto: ")
            codigo = input("Código del producto: ")
            precio = inputNumero("Precio del producto: ")
            cantidad = inputNumero("Cantidad de producto: ")
            nVentas = inputNumero("Número de ventas del producto: ")
            paraEditar["nombre"] = nombre
            paraEditar["codigo"] = codigo
            paraEditar["precio"] = precio
            paraEditar["cantidad"] = cantidad
            paraEditar["nVentas"] = nVentas

        print()
        print("Editado correctamente.")
    else:
        print("No hay productos en el inventario.")
    print("----------------")

def eliminarProducto():
    print()
    print("***  Eliminar Producto  ***")
    if len(inventario) != 0:
        print("Elige el N° de producto que se va a eliminar")
        listarProductos()
        while True:
            indice = input("Seleccionar numero: ")
            if indice == "" or indice.isdigit() == False:
                print("La opción debe ser un numero valido.")
            else:
                break
        indice = int(indice)
        eliminado = inventario.pop(indice+1)
        print("Producto eliminado: ")
        print("Nombre: ", eliminado["nombre"])    
        print("Codigo: ", eliminado["codigo"])    
    else:
        print("No hay productos en el inventario.")
    print("----------------")

def listarProductos():
    print()
    print("***  Listado de Productos  ***")
    print()
    for i in range(0, len(inventario)):
        print("Producto N°", i+1)
        print()
        print("Nombre: ", inventario[i]["nombre"])
        print("Codigo: ", inventario[i]["codigo"])
        print("Precio: ", inventario[i]["precio"])
        print("Cantidad: ", inventario[i]["cantidad"])
        print("Numero de ventas: ", inventario[i]["nVentas"])
        print("----------------")
        print()

def controlStock():
    print()
    print("***  Control de stock de Productos  ***")
    print("----------------")

def reportes():
    print()
    print("***  Reportes  ***")
    print("----------------")


while True:


    menu()
    opcion = int(input("Elija una opción: "))

    if(opcion == 0):
        print("Hasta pronto.")
        break
    elif(opcion == 1):
        agregarProducto()
    elif(opcion == 2):
        editarProducto()
    elif(opcion == 3):
        eliminarProducto()
    elif(opcion == 4):
        listarProductos()
    elif(opcion == 5):
        controlStock()
    elif(opcion == 6):
        reportes()
