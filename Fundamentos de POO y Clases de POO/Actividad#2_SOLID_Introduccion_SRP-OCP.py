#Como aplicar herencia en python

class Usuario:
    def __init__(self, nombre, email):
        self.Nombre = nombre
        self.Email = email
    
    def mostrar_info(self):
        return f"Nombre: {self.Nombre}, Email: {self.Email}"
    
class Cliente(Usuario):
    def __init__(self, nombre, email,id_cliente):
        super().__init__(nombre, email) #Ejecute el contructor base
        self.ID_Cliente = id_cliente

    def mostrar_info(self):#Sobrescritura al metodo de la clase Usuario (mostrar_info)
        return f"Cliente: {self.Nombre}, ID: {self.ID_Cliente}"

class Administrador(Usuario):
    def __init__(self, nombre, email, nivel_acceso):
        super().__init__(nombre, email)
        self.Nivel_Acceso = nivel_acceso

#Uso
cliente = Cliente("Jose Julia","uijjulian@gmail.com","21100215")
admin = Administrador("Pablito","joseantonio.el@nlaredo.tecnm.mx","Total")
print(cliente.mostrar_info())
print(admin.mostrar_info())

#Ejemplos de Herencia
#Super Clase - Vehiculo
#Subclase - Camioneta
#Subclase - Carro

class Producto:
    def __init__(self, nombre, precio, stock):
        self.Nombre = nombre
        self.__Precio = precio
        self.Stock = stock
    
    @property
    def precio(self):
        return self.__Precio
    
    def calculador_costo(self):
        return self.precio

class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio,stock=-1)
    
    def calculador_costo(self): #Polimorfismo
        return self.precio * 0.9

class ProductoFisico(Producto):
    def __init__(self, nombre, precio, costo_envio):
        super().__init__(nombre, precio)
        self.Costo_Envio = costo_envio
    
    def calculador_costo(self):
        return self.precio + self.Costo_Envio
    
#Uso de polimorfismo
#crear una clase llamada producto fisica y producto digital
class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, stock = -1)
    def calculador_costo(self):
        return self.precio * 0.9
    def disponible(self):
        return True #Siempre disponible
    def __str__(self):
        return f"{self.Nombre} (Digital) - ${self.precio}"
    
class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock, costo_envio):
        super().__init__(nombre, precio, stock)
        self.Costo_Envio = costo_envio

    def calculador_costo(self):
        return self.precio + self.Costo_Envio
    def __str__(self):
        return f"{self.Nombre} (Fisico) - ${self.precio} + ${self.Costo_Envio}"
    
#prueba 
prod_q = Producto("Libro", 20,5)
prod_d = ProductoDigital("Ebook",50)
prod_f = ProductoFisico("Lapiz",20,5,10)

print(prod_q)
print(prod_d)
print(prod_f)

#XDDDDDDDDDDDDDDDDDDDDDDDD

productos = [
    Producto("Libro",20),
    ProductoFisico("Lapiz",5,2),
    ProductoDigital("Pluma",10,25)
]

for p in productos:
    print(f"Nombre: {p.Nombre}, Precio: ${p.calculador_costo()}")

#Ejemplo de un mal practica en una clase POO sin Polimorfismo
class ProductoMalo:
    def __init__(self, nombre, precio, tipo):
        self.Nombre = nombre
        self.Precio = precio
        self.Tipo = tipo
    def calcular_costo(self):
        if self.Tipo =="Digital":
            return self.Precio * 0.9
        elif self.Tipo == "Fisico":
            return self.Precio + 5
        return self.Precio



