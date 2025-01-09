import json

#-- Datos del inventario --
inventario = []
#-- Funciones del Sistema ---
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar Producto")
    print("2. Actualizar Producto")
    print("3. Eliminar Producto")
    print("4. Ver Inventario")
    print("5. Buscar Producto")
    print("6. Generar Reportes")
    print("7. Salir")

def agregar_producto():
    print("\n--- Agregar Producto ---")
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad inicial: "))
    inventario.append({"codigo": codigo, "nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Producto agregado exitosamente.")

def actualizar_producto():
    print("\n--- Actualizar Producto ---")
    codigo = input("Ingrese el código del producto a actualizar: ")
    for producto in inventario:
        if producto["codigo"] == codigo:
            producto["nombre"] = input("Nuevo nombre (o presione Enter para mantener el actual): ") or producto["nombre"]
            producto["precio"] = float(input("Nuevo precio (o presione Enter para mantener el actual): ") or producto["precio"])
            producto["cantidad"] = int(input("Nueva cantidad (o presione Enter para mantener la actual): ") or producto["cantidad"])
            print("Producto actualizado.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese el código del producto a eliminar: ")
    global inventario
    inventario = [producto for producto in inventario if producto["codigo"] != codigo]
    print("Producto eliminado exitosamente.")

def ver_inventario():
    print("\n--- Inventario ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def buscar_producto():
    print("\n--- Buscar Producto ---")
    termino = input("Ingrese el nombre o código del producto: ").lower()
    resultados = [p for p in inventario if termino in p["codigo"].lower() or termino in p["nombre"].lower()]
    if resultados:
        for producto in resultados:
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No se encontraron productos.")

def generar_reportes():
    print("\n--- Generar Reportes ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    total_productos = len(inventario)
    productos_bajo_stock = [p for p in inventario if p["cantidad"] < 5]
    print(f"Total de productos: {total_productos}")
    print(f"Productos con stock bajo (<5): {len(productos_bajo_stock)}")
    for p in productos_bajo_stock:
        print(f" - {p['nombre']} (Cantidad: {p['cantidad']})")

# --- Ejecución del Programa ---
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            actualizar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            ver_inventario()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            generar_reportes()
        elif opcion == "7":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

      
