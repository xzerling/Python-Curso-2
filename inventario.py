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
* Alvaro Daniel Elgueda Labra                                                *
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
* Descripcion de Aplicación INVENTARIO :
* La aplicación inventario tiene el siguiente menú:
*	- Registrar producto.
*	- Listar productos.
*   - Buscar producto.
*	- Modificar producto.
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
inventario=[]
"""
Se inicia un ciclo while infinito, el bucle no termina hasta que el usuario
seleccione la opcion salir
"""
while True:

    """
    Con este ciclo while y try and except se controla que los errores cometidos por el usuario
    no terminen el programa
    """
    while True:
        try:
            print("Seleccione la opcion deseada", "1)Registrar Producto","2)Listar Productos", "3)Buscar Productos", "4)Modificar Productos", "5)Eliminar Productos", "6)Salir", sep="\n")
            select=int(input())
        except ValueError as error:
            print("Error:",error)
        else:
            break
    """
    Segun sea la seleccion del usuario en el menú anterior, se realiza cierta acción
    """
    if select ==1:
        """
        Si la opción es 1, se ingresan los productos, los datos que se van a ingresar
        estan "protegidos" contra entradas invalidas mediante ciclos while y
        sentencias try-except, estas caracteristicas se repiten a lo largo del codigo.
        """
        while True:
            while True:
                try:
                    ID=int(input("Ingrese el id-->"))
                    if ID == -1:
                        break
                except ValueError as error:
                    print("Error:",error)
                else:
                    if ID in ids: #comprobamos que el id ingresado no se encuentre dentro de la lista ids
                        print("Este ID ya existe intente de nuevo")
                        continue
                    else:
                        ids.append(ID)#si el id no existe en la lista ids, lo agregamos
                        while True:
                            cat=input("Ingrese la categoria-->")
                            if cat.isnumeric() == True or cat.isalpha() == False: 
                                """Se verifica que las entradas del usuario sean validas, solo pueden ser palabras
                                """
                                print("Valor invalido")
                            else:
                                if cat not in categorias:#comprobamos si la categoria ya existe 
                                    categorias.append(cat)#si no existe la agregamos a lista categorias
                                break
                        while True:
                            nombre=input("Ingrese el nombre-->")
                            if nombre.isnumeric() == True or nombre.isalpha() == False:
                                """Se verifica que las entradas del usuario sean validas, solo pueden ser palabras
                                """
                                print("Valor invalido")
                            else:
                                break   
                        while True: 
                            try:
                                cantidad=int(input("Ingrese la cantidad-->"))
                                costo=float(input("Ingrese el costo-->"))
                            except ValueError as error:
                                print("Error:",error)
                            else:
                                fecha=input("Ingrese la fecha de registro-->")
                                comentarios=input("Comentarios-->")
                                inventario.append({"ID": ID, "categoria" : cat, "nombre" : nombre, "cantidad" : cantidad, "costo" : costo, 
                                "fecha_registro" : fecha, "comentarios" : comentarios}) 
                                """
                                Se Agrega los datos a nuestra lista inventario
                                la cual contiene diccionarios que almacenan en pares
                                clave:valor lo ingresado por el usuario
                                """
                                break
                        break
            break
    
    #Si la opcion es 2, listamos los productos
    elif select==2:
        """
        se comprueba que la lista inventario no este vacia
        """
        if inventario != []:
            """
            se itera sobre cada elemento de la lista categoria, despues se itera sobre la
            lista inventario y los pares clave_valor que coincidan con la iteración
            de la lista categorias, las mostramos en pantalla
            """
            for i in categorias:
                print("\n\n****************{}**************\n\n".format(i))
                for j in inventario:
                    if i == j["categoria"]:
                        print("********************************")
                        print("ID:", j["ID"])
                        print("categoria", j["categoria"])
                        print("Nombre:", j["nombre"])
                        print("Cantidad:", j["cantidad"])
                        print("Costo:", j["costo"])
                        print("Fecha_registro:", j["fecha_registro"])
                        print("Comentarios:", j["comentarios"])
                        print("\n\n")
        else:
            """
            Si la lista está vacia se muestra este mensaje
            """
            print("NO HAY PRODUCTOS REGISTRADOS")
    
    #Si la opcion es 3, se busca el producto que quiere el usuario
    
    elif select==3:
        """
        Las busquedas del usuario solo deben ser a traves de un id, por ello
        protegemos las entradas en sentencias try,except
        """
        while True:
            try:
                buscar=int(input("Ingrese el ID-->"))
            except ValueError as error:
                print("Valor invalido", error)
            else:
                if buscar not in ids:
                    """
                    Si el id que busca el usuario no existe se muestra este mensaje
                    """
                    print("********************************")
                    print("ESTE PRODUCTO NO EXISTE")
                    print("********************************")
                else:
                    """
                    Si el id de busqueda existe, iteramos sobre los elementos de la lista
                    inventario y comparamos el id de busqueda del usario con el id
                    registrado dentro del diccionario dentro de la lista, si los ids
                    coinciden se muestra la informacion relevante al producto
                    """
                    for i in inventario:
                        if buscar == i["ID"]:
                            print("********************************")
                            print("ID:", i["ID"])
                            print("Nombre:", i["nombre"])
                            print("Categoria:", i["categoria"])
                            print("Cantidad:", i["cantidad"])
                            print("Costo:", i["costo"])
                            print("Fecha_registro:", i["fecha_registro"])
                            print("Comentarios:", i["comentarios"])
                            print("********************************")
                            print("\n\n")
                            break
                break
    
    #Si la opcion es 4, se modifica un producto con base en un id existente
    
    elif select==4:
        """
            Si el id de busqueda existe, iteramos sobre los elementos de la lista
            inventario y comparamos el id de busqueda del usario con el id
            registrado dentro del diccionario dentro de la lista, si los ids
            coinciden se le pide al usuario ingresar los nuevos datos
            del producto, la entrada de estos datos se realiza de la misma
            manera que en la opcion 1 y solo se modifican los datos permitidos
         """
        while True:
            try:
                buscar=int(input("Ingrese el ID-->"))
            except ValueError as error:
                print("Valor invalido", error)
            else:
                if buscar not in ids:
                    print("********************************")
                    print("ESTE PRODUCTO NO EXISTE")
                    print("********************************")
                    break
                else:
                    for i in inventario:
                        if buscar == i["ID"]:
                            while True:
                                cat_m=input("categoria-->")
                                if cat.isnumeric() == True or cat.isalpha() == False:
                                    print("Valor invalido")
                                else:
                                    if cat_m not in categorias:
                                        categorias.append(cat_m)
                                        i["categoria"]=cat_m
                                        break
                                    else:
                                        i["categoria"]=cat_m
                                    break
                            while True:
                                nombre_m=input("Ingrese el nombre-->")
                                if nombre_m.isnumeric() == True or nombre_m.isalpha() == False:
                                    print("Valor invalido")
                                else:
                                    i["nombre"]=nombre_m
                                    break   
                            while True:
                                try:
                                    cantidad_m=int(input("Ingrese la cantidad-->"))
                                    costo_m=float(input("Ingrese el costo-->"))
                                except ValueError as error:
                                    print("Error:",error)
                                else:
                                    i["cantidad"]=cantidad_m
                                    i["costo"]=costo_m
                                    break
                    break
    
    #Si la opcion es 5, se elimina el producto siempre y cuando el id exista
                       
    elif select==5:
        """
        Se realiza una busqueda al igual que en la opcion 3, si el id existe
        se devuelve en que numero de indice esta contenido el diccionario que contiene
        el id de busqueda para eliminar, posteriormete se elimina con el metodo .pop
        """
        while True:
            try:
                buscar=int(input("Ingrese el ID-->"))
            except ValueError as error:
                print("Valor invalido", error)
            else:
                if buscar not in ids:
                    print("********************************")
                    print("ESTE PRODUCTO NO EXISTE")
                    print("********************************")
                else:
                    for i in inventario:
                        if buscar == i["ID"]:
                            print("********************************")
                            indice=inventario.index(i) #Se devuelve el indice correspondiente
                            eliminar=inventario.pop(indice)
                            print("SE ELIMINÓ EL PRODUCTO")
                            print("********************************")
                            break
                break
    
    #Si la opcion es 6, se finaliza el programa
    
    elif select==6:
        print("LA EJECUCIÓN TERMINÓ")
        break
        
    