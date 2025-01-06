inventario = []

def menu_de_opciones_control_de_inventario_tienda_gifty():
    """Menú principal de opciones de control de inventario"""
    print("1. Nuevo Producto")
    print("2. Actualización de producto")
    print("3. Eliminación producto")
    print("4. Mostrar inventario")
    print("5. Buscar por producto")
    print("6. Control de stock")
    print("7. Generar informe de unidades en stock")
    print("8. Salir")

def nuevo_producto():
    """Esta función registra nuevos productos en inventario"""
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto $: "))
    cantidad = int(input("Cantidad disponible: "))
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Registro de nuevo producto éxitoso.")

def actualizacion_producto():
    """Esta función registra las actualizaciones de productos en inventario"""
    nombre = input("Nombre del producto que se actualiza: ")
    for producto in inventario:
       if producto["nombre"] == nombre:
           producto["precio"] = float(input("Nuevo precio del producto $: "))
           producto["cantidad"] = int(input("Nueva cantidad disponible: "))
           print("Actualización de producto exitosa.")
           return
    print("Producto no encontrado.")

def eliminacion_producto():
    """Esta función elimina productos en inventario"""
    nombre = input("Nombre del producto que se elimina ")
    global inventario
    inventario = [producto for producto in inventario if producto["nombre"]]
    print("Eliminación de producto exitosa.")

def mostrar_inventario():
    """Muestra un informe de inventario por nombre de producto, precio y cantidad"""
    for producto in inventario:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def buscar_por_producto():
   """Busca en el inventario por nombre de producto"""
   nombre = input("Nombre del producto que se quiere buscar: ")
   for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"Nombre: {producto['nombre']}, Precio: {profucto['precio']}, Cantidad: {producto['cantidad']}")
            return
        print("Producto no encontrado.")
            
def contro_de_stock():
    """Alerta de stock de cantidad inferior a 10 por producto"""
    for producto in inventario:
        if producto["cantidad"] < 10:
            print(f"Alerta: El producto {producto['nombre']} está bajo en stock ({producto['cantidad']} unidades).")

def reporte_informe_unidades_en_stock():
    total_productos = len(inventario)
    productos_con_baja_cantidad = [producto for producto in inventario if producto["cantidad"] < 10]
    productos_mas_vendidos = sorted(inventario, key=lambda x: x['cantidad'])
    
    print(f"Total de productos:{total_productos}")
    print("Productos con baja cantidad:")
    for producto in productos_con_baja_cantidad:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
    print("Productos más vendidos (basado en cantidad disponible):")
    for producto in productos_mas_vendidos[:10]:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")

        fecha_reporte = datetime.datetime.now().strftime("%Y-%m-%d %H:%S")
        print(f"Informe generado el {fecha_reporte}")

while True:
    menu_de_opciones_control_de_inventario_tienda_gifty()
    opcion = input("Selecciona una opción: ")
    if opcion == '1':
        nuevo_producto()
    elif opcion == '2':
        actualizacion_producto()
    elif opcion == '3':
         eliminacion_producto()
    elif opcion == '4':
        mostrar_inventario()
    elif opcion == '5':
        buscar_por_producto()
    elif opcion == '6':
        contro_de_stock()
    elif opcion == '7':
        reporte_informe_unidades_en_stock()
    elif opcion == '8':
        print("Salir")
        break
    else:
        print("Opción no válida, selecciona una opción nuevamente")
        


    
    
    




                  
    
    

