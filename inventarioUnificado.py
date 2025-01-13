# -*- coding: utf-8 -*-
"""
"""
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
    print("2. Editar precio")
    print("3. Editar stock")
    print("4. Editar venta")
    print("5. Editar todo")
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
        # Verificar que el código sea numérico y único
        codigo = inputNumero("Código del producto (numérico): ")
        if codigo in ids:
            print("El código ya existe, por favor ingrese otro.")
            continue
        
        # Verificar que el nombre no esté vacío y sea único
        while True:
            nombre = input("Nombre del producto: ").strip().upper()
            if not nombre:
                print("El nombre del producto no puede estar vacío.")
                continue

            nombres_existentes = [producto['nombre'] for producto in inventario]
            if nombre in nombres_existentes:
                print("El nombre del producto ya existe, favor ingresar otro.")
                continue
            break
        
        # Verificar que el precio sea numérico
        precio = inputNumero("Precio del producto (numérico): ")

        # Verificar que la cantidad sea numérica
        cantidad = inputNumero("Cantidad del producto (numérico): ")

        # Verificar que el número de ventas sea numérico
        nVentas = inputNumero("Número de ventas del producto (numérico): ")

        # Crear el producto y agregarlo al inventario
        producto = {
            "nombre": nombre,
            "codigo": codigo,
            "precio": precio,
            "cantidad": cantidad,
            "nVentas": nVentas
         
        }
        inventario.append(producto)
        ids.append(codigo)
        print(f"\nProducto '{nombre}' agregado correctamente.")
        print("----------------")
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
            cantidad = inputNumero("Stock de producto: ")
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
    if len(inventario) == 0:
        print("No hay productos en el inventario.")
    else:
        listarProductos()  # Mostrar productos disponibles para eliminar
        codigo = inputNumero("Ingrese el código del producto que desea eliminar: ")
        
        if codigo in ids:
            for producto in inventario:
                if producto["codigo"] == codigo:
                    inventario.remove(producto)
                    ids.remove(codigo)
                    print(f"\nProducto eliminado con éxito:")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Código: {producto['codigo']}")
                    print("----------------")
                    break
                else:
                    print("No hay productos en el inventario.")
        print("----------------")

def buscarProducto():
    print("\n***   Buscar Producto  ***")
    criterio = input("¿Desea buscar por [1] Código o [2] Nombre? Ingrese 1 o 2: ").strip()
    
    if criterio == "1":  # Buscar por código
        codigo = inputNumero("Ingrese el código del producto: ")
        encontrado = False
        for producto in inventario:
            if producto["codigo"] == codigo:
                print("\nProducto encontrado:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Código: {producto['codigo']}")
                print(f"Precio: {producto['precio']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Número de ventas: {producto['nVentas']}")
                print("----------------")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró un producto con ese código.")
    
    elif criterio == "2":  # Buscar por nombre
        nombre = input("Ingrese el nombre del producto: ").strip().upper()
        encontrado = False
        for producto in inventario:
            if producto["nombre"] == nombre:
                print("\nProducto encontrado:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Código: {producto['codigo']}")
                print(f"Precio: {producto['precio']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Número de ventas: {producto['nVentas']}")
                print("----------------")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró un producto con ese nombre.")
    
    else:
        print("Opción no válida. Por favor, ingrese 1 o 2.")
    
    
def listarProductos():
    print()
    if len(inventario) == 0:  # Verifica si el inventario está vacío
       print("No hay productos registrados en el inventario.")
       print("***  Listado de Productos  ***")
       print()
    for i, producto in enumerate(inventario, start=1):  # Enumerar productos de manera más clara
            print(f"Producto N° {i}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Código: {producto['codigo']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Número de ventas: {producto['nVentas']}")
            print("----------------\n")
            input("Presiona Enter para continuar...")   
def controlStock():
    print()
    print("***  Control de stock de Productos  ***")
    print("----------------")
    productosCriticos = [] 
     # Identificar productos con stock crítico
    for producto in inventario:
        if int(producto["cantidad"]) <= stockMinimo:
            productosCriticos.append(producto)
# Mostrar resultados
    if productosCriticos:
        print("Productos con stock crítico o bajo:")
        contador = 0
        for producto in productosCriticos:
            print(f"Nombre: {producto['nombre']}")
            print(f"Código: {producto['codigo']}")
            print(f"Cantidad: {producto['cantidad']}")
            contador = contador+1
            print("----------------")
        print(f"Total de productos con stock critico: {contador}")
    else:
        print("Todos los productos tienen niveles de stock adecuados.")
        print("----------------")

def reportes():
    print("\n***  Reportes de Inventario  ***")
    if len(inventario) == 0:  # Verifica si el inventario está vacío
       print("No hay productos registrados en el inventario.")
    else:
        print(f"\nTotal de productos registrados: {len(inventario)}\n")
        
        print("Detalle de productos y su stock:")
        print("-" * 40)
        for i, producto in enumerate(inventario):
            print(f"Producto N° {i + 1}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Código: {producto['codigo']}")
            print(f"Cantidad en stock: {producto['cantidad']}")
            print("-" * 40)

        controlStock()
        print()
        print("***Top 3 Productos Mas vendidos ***")
        topInventario = sorted(inventario, key=lambda producto: producto['nVentas'], reverse=True)[:3]
        for i in range(0, len(topInventario)):
            print(f"Nombre: {topInventario[i]['nombre']}")
            print(f"Código: {topInventario[i]['codigo']}")
            print(f"Cantidad de ventas: {topInventario[i]['nVentas']}")
            print("----------------\n")


    
    print("----------------")
    print("Fin del reporte.")
    
    
    print("----------------")


while True:


    menu()
    opcion = int(inputNumero("Elija una opción: "))

    if(opcion == 0):
        print("Fin de sesión, hasta pronto.")
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
