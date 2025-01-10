"""
******************************************************************************
*       U N I V E R S I D A D   A U T O N O M A   D E   C H I L E            *
*                                                                            *
* DIPLOMADO DE BID DATA  AND MACHINE LEARNING                                *
*                                                                            *
* APLICACION: Inventario                                                     *
* INTEGRANTES GRUPO N°39                                                     *
* Veronica Patricia Alvarez Diaz                                             *
* Christian Francisco Astete Seguel                                          *
* Álvaro Daniel Elgueda Labra                                                *
* Jorge Fernando Fornés Pavez                                                *
* Daniela Soledad Pinto Castro                                               *
*                                                                            *
******************************************************************************
* Descripción Tarea:
* La tienda de venta de artículos de regalo “gifty”, lleva su control de
* inventario a través de hojas de Excel, registrando las entradas de artículos
* y salidas de cada uno cada vez que se vende un artículo. Ustedes como equipo
* de desarrolladores de software en Python deben desarrollar un sistema sencillo
* de gestión de inventario. El sistema permitirá a los usuarios administrar el
* inventario de la tienda, utilizando los conceptos aprendidos en las cuatro
* unidades del diplomado en Python, incluyendo el uso de variables, estructuras
* de control de flujo, funciones y módulos, y estructuras de datos.
*
* Descripción de Aplicación INVENTARIO :
* La aplicación inventario tiene el siguiente menú:
*   - Registrar producto.
*   - Listar productos.
*   - Buscar producto.
*   - Modificar producto.
*   - Eliminar producto.
*   - Salir.
*
* Explicación de Funciones:
*
REGISTRAR: La opción de registrar producto deberá solicitar al usuario un ID del producto a registrar, 
este valor debe ser único e irrepetible. Adicionalmente, se solicitarán los siguientes datos: 
Categoría del producto
Nombre del producto
Cantidad
Costo unitario
Fecha de registro
Comentarios.

LISTAR: La opción de listar deberá mostrar en pantalla los datos de todos los productos registrados. 
Esta información deberá mostrarse de forma ordenada por categoría (ej., lácteos, cereales, 
farmacia, etc.)

BUSCAR: La opción de buscar producto solicitará al usuario el ID del producto y una vez localizado deberá 
mostrar la información de dicho producto.

MODIFICAR: La opción de modificar producto solicitará al usuario el ID del producto, si el producto existe, 
los únicos datos que se pueden modificar son nombre del producto, categoría, precio unitario y 
la cantidad en existencia.

ELIMINAR: La opción de eliminar producto solicitará al usuario el ID del producto a eliminar, 
en caso de existir dicho producto deberá ser eliminado del sistema.

SALIR: El programa debe terminar sólo cuando el usuario elija la opción de salir.
"""

"""
********* SUPUESTOS ************
- El codigo del producto debe ser un numero entero positivo.
- Se considera stock critico menor o igual a 10 unidades.
- El codigo no puede ser editado.

"""

"""
Declaramos un diccionario, el cual será la plantilla
para guardar los datos ingresados
"""
productos = {
    "ID" : None,
    "categoria" : None,
    "nombre" : None,
    "cantidad" : None,
    "costo" : None,
    "fecha_registro" :None,
    "comentarios" : None
}

"""
Se Declaran varias listas vacias, la lista "ids" almacena los id ingresados
y posteriormente se intera sobre ella para verificar que ningun id se repita.
La lista categoria almacena las categorias ingresadas para definir categorias por defecto
La lista inventario almacena todos los datos ingresados, esta información se almacena
en diccionarios anidados
"""
ids=[]
categorias=[]
inventario = []
stockMinimo = 15


def menu():
    print()
    print("***  Menu principal  ***")
    print("1. Registrar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Listar productos")
    print("5. Buscar producto")
    print("6. Control de stock")
    print("7. Reportes")
    print("0. Salir")
    print()

def menuEditar():
    print()
    print("***  Menu edición  ***")
    print("1. Editar nombre")
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
    while True: 
        codigo = inputNumero("Código del producto: ")
        if codigo in ids:
            print("el codigo ya existe, escribe otro")
        else:
            nombre = input("Nombre del producto: ")
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
            ids.append(codigo)
            break
            
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
            precio = inputNumero("Precio del producto: ")
            paraEditar["precio"] = precio
        elif(opcion == 3):
            cantidad = inputNumero("Cantidad de producto: ")
            paraEditar["cantidad"] = cantidad
        elif(opcion == 4):
            nVentas = inputNumero("Número de ventas del producto: ")
            paraEditar["nVentas"] = nVentas
        elif(opcion == 5):
            nombre = input("Nombre del producto: ")
            precio = inputNumero("Precio del producto: ")
            cantidad = inputNumero("Cantidad de producto: ")
            nVentas = inputNumero("Número de ventas del producto: ")
            paraEditar["nombre"] = nombre
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
        indice = inputNumero("Seleccionar numero: ")
        indice = int(indice)
        if(indice >= len(inventario)):
            eliminado = inventario.pop(indice+1)
            print("Producto eliminado: ")
            print("Nombre: ", eliminado["nombre"])    
            print("Codigo: ", eliminado["codigo"])
        else:
            print()
    else:
        print("No hay productos en el inventario.")
    print("----------------")

def buscarProducto():
    print("\n***   Buscar Producto  ***")
    codigo = inputNumero("Ingrese código del producto: ")
    if(codigo in ids):
        for i in range(0, len(inventario)):
            if(inventario[i]["codigo"] == codigo):
                print()
                print("Producto encontrado: ")
                print("Nombre: ", inventario[i]["nombre"])
                print("Precio: ", inventario[i]["precio"])
                print("Cantidad: ", inventario[i]["cantidad"])
                print("Numero de ventas: ", inventario[i]["nVentas"])
                print("----------------")
                print()
    else:
        print("No hay un producto con ese codigo asociado")

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
    print("Total de productos: ", len(inventario))
    contador = 0
    for i in range(0, len(inventario)):
        if int(inventario[i]["cantidad"]) <= stockMinimo:
            print("producto "+inventario[i]["nombre"]+" tiene stock de "+inventario[i]["cantidad"] )
            contador = contador+1
    print("Productos con stock menor o igual a "+stockMinimo+": "+contador)
    
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
        buscarProducto()
    elif(opcion == 6):
        controlStock()
    elif(opcion == 7):
        reportes()