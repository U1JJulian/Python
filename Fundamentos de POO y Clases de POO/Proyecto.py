class Producto:
    def __init__(self, Nombre, Precio, Stock):
        self.Nombre = Nombre
        self.__Precio = Precio
        self.Stock = Stock
    
    @property
    def precio(self):
        return self.__Precio
    
    def disponible(self):
        return self.Stock > 0

    def __str__(self):
        return f" \n Nombre del producto: {self.Nombre} \n Precio del producto: {self.__Precio} \n Cantidad de productos disponibles: {self.Stock}"

class Cliente:
    def __init__(self, Nombre, Email):
        self.Nombre = Nombre
        self.Email = Email
    def __str__(self):
        return f"\n Usuario: {self.Nombre} \n Correo: {self.Email}"

class Carrito:
    def __init__(self, Producto):
        self.Producto = Producto
        self.lstProductos = []
    
    def agregar_producto(self,Producto):
        self.lstProductos.append(Producto)


miProducto = Producto("Samsung s18", 5000, 15)
print(miProducto)

