import index as POO

#Creamos una lista de clientes que puedan tener acceso a la tienda
lstUsuarios = {
    "JJulian":"03JJulianU1@gmail.com"
}

#Metodo para que el usuario pueda iniciar sesion
def iniciar_sesion():
    print("------------------------")
    print("-----Iniciar Sesion-----")
    print("------------------------","\n")
    while True:
        print("---Ingresar tu nombre---")
        usuario = input("Usuario: ")
        print("---Ingresa tu correo---")
        correo = input("Correo: ")

        if usuario in lstUsuarios and lstUsuarios[usuario] == correo:
            print("\n","Inicio de sesion correcta!")
            return usuario
        else:

            print("\n","Favor de ingresar correctamente tus datos","\n")

#metodo para mostrar el menu de la tienda
def menu_tienda(cliente, carrito, tienda):
    while True:
        print("\n--- Menú de la Tienda ---")
        print("1. Ver productos disponibles")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Salir \n")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n Productos disponibles:")
            for producto in tienda.catalogo:
                print(f"- {producto}")

        elif opcion == "2":
            nombre_producto = input("Escribe el nombre del producto: ")
            producto = tienda.buscar_producto(nombre_producto)

            if producto:
                if carrito.agregar_producto(producto):
                    print(f" {producto.nombre} agregado al carrito.")
                else:
                    print("No hay suficiente stock.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            print("\n Carrito de compras:")
            print(carrito)

        elif opcion == "4":
            print("\n Finalizando compra...")
            print(tienda.realizar_compra(cliente, carrito))
            return  # Sale del menú tras la compra

        elif opcion == "5":
            print("\n Saliendo de la tienda...")
            return  # Sale del menú

        else:
            print("Opción no válida. Intenta de nuevo.")

     

#Creamos una lista de clientes que puedan tener acceso a la tienda
lstUsuarios = {"JJulian":"03JJulianU1@gmail.com"}
# Iniciar sesión
usuario = iniciar_sesion()

# Crear cliente (según el usuario autenticado)
cliente = POO.Cliente(usuario, f"{lstUsuarios[usuario]}")

# Crear productos
p1 = POO.Producto("Laptop", 1000, 5)
p2 = POO.ProductoDigital("Curso de Python", 200)
p3 = POO.Producto("Mouse", 40, 12)

# Crear tienda y agregar productos
tienda = POO.Tienda()
tienda.agregar_al_catalogo(p1)
tienda.agregar_al_catalogo(p2)
tienda.agregar_al_catalogo(p3)

# Crear carrito (vacío al inicio)
carrito = POO.Carrito()

# Mostrar menú de la tienda
menu_tienda(cliente, carrito, tienda)