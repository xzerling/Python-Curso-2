# --- Datos del inventario ---
inventario = []

# --- Funciones del Sistema ---
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar Producto")
    print("2. Ver Inventario")
    print("3. Buscar Producto")
    print("4. Salir")

def agregar_producto():
    print("\n--- Agregar Producto ---")
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    producto = {"codigo": codigo, "nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Producto agregado con éxito.")

def ver_inventario():
    print("\n--- Inventario ---")
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def buscar_producto():
    print("\n--- Buscar Producto ---")
    busqueda = input("Ingrese el código o nombre del producto: ").lower()
    encontrado = False
    for producto in inventario:
        if busqueda in producto["codigo"].lower() or busqueda in producto["nombre"].lower():
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.")

# --- Ejecución Principal ---
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
