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
    def __init__(self, nombre, precio):
        self.Nombre = nombre
        self.__Precio = precio
    
    @property
    def precio(self):
        return self.__Precio
    
    def calculador_costo(self):
        return self.precio

class ProductoDigital(Producto):
    def __init__(self, nombre, precio, costo_envio):
        super().__init__(nombre, precio)
        self.Costo_Envio = costo_envio
    
    def calculador_costo(self): #Polimorfismo
        return self.precio * 0.9

class ProductoFisico(Producto):
    def __init__(self, nombre, precio, costo_envio):
        super().__init__(nombre, precio)
        self.Costo_Envio = costo_envio
    
    def calculador_costo(self):
        return self.precio + self.Costo_Envio