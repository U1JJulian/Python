# Herencia

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Email: {self.email}"

class Cliente(Usuario):
    def __init__(self, nombre, email, id_cliente):
        super().__init__(nombre,email)
        self.id_cliente = id_cliente

    def mostrar_info(self): # Sobrescritura
        return f"Cliente: {self.nombre} (ID: {self.id_cliente})"
 
class Administrador(Usuario):
    def __init__(self, nombre, email, nivel_acceso):
        super().__init__(nombre, email)
        self.nivel_acceso = nivel_acceso

# Uso
cliente = Cliente("Juan", "juan.av@nlaredo.tecnm.mx", "D654")
admin = Administrador("Antonio", "joseantonio.el@nlaredo.tecnm.mx", "Total")
print(cliente.mostrar_info())
print(admin.mostrar_info())

# Ejemplos de Herencia
# Super Clase - Vehiculo
# Subclase - Camioneta
# Subclase - Carro

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio
    
    @property
    def precio(self):
        return self.__precio
    
    def calcularCosto(self):
        return self.precio

class ProductoDigital(Producto):    
    def calcularCosto(self): #Polimorfismo
        return self.precio * 0.9

class ProductoFisico(Producto):
    def __init__(self,nombre,precio,costo_envio):
        super().__init__(nombre,precio)
        self.costo_envio = costo_envio
    
    def calcularCosto(self): #Polimorfismo
         return self.precio + self.costo_envio

# Uso polimorfico
productos = [
    Producto("Libro", 20),
    ProductoFisico("Lapiz", 15, 15),
    ProductoDigital("Ebook", 10)
]
for p in productos:
    print(f"{p.nombre}: ${p.calcularCosto()}")


"""
3. Principios SOLID: Introducción a SRP y OCP (40 minutos)
Explicación:
SRP (Single Responsibility Principle): Una clase debe tener una sola razón para cambiar. 
Ejemplo: Producto no debería manejar envíos, solo sus propios datos.

OCP (Open/Closed Principle): Las clases deben estar abiertas a extensión (e.g., nuevas subclases) pero cerradas a modificación (sin alterar el código original).

Relación con herencia y polimorfismo: Puedes extender Producto con ProductoDigital sin modificar la clase base.

Ejemplo:
Sin OCP: Modificar Producto para agregar descuentos rompe el principio.
Con OCP: Usar herencia y polimorfismo como en el ejemplo anterior.

Demostración:
"""

class ProductoMalo:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
    def calcularCosto(self):
        if self.tipo == "Digital":
            return self.precio * 0.9
        elif self.tipo == "Fisico":
            return self.precio + 5
        return self.precio
#########################################
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock
    
    @property
    def precio(self):
        return self.__precio
    
    def disponible(self):
        return self.stock > 0
    
    def calcular_costo(self):
        return self.precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, stock=-1)  # No Aplica
    
    def calcular_costo(self):
        return self.precio * 0.9
    
    def disponible(self):
        return True  # Siempre disponible
    
    def __str__(self):
        return f"{self.nombre} (Digital) - ${self.precio}"

class ProductoFisico(Producto):
    def __init__(self, nombre, precio, stock, costo_envio):
        super().__init__(nombre, precio, stock)
        self.costo_envio = costo_envio
    
    def calcular_costo(self):
        return self.precio + self.costo_envio
    
    def __str__(self):
        return f"{self.nombre} (Físico) - ${self.precio} + ${self.costo_envio} envío"

# Prueba
prod = Producto("Libro", 20, 5)
digital = ProductoDigital("Ebook", 20)
fisico = ProductoFisico("Camisa", 20, 3, 5)
print(prod)              # "Libro - $20 (Stock: 5)"
print(digital)          # "Ebook (Digital) - $20"
print(fisico)           # "Camisa (Físico) - $20 + $5 envío"
print(prod.calcular_costo())    # 20
print(digital.calcular_costo()) # 18.0
print(fisico.calcular_costo())  # 25