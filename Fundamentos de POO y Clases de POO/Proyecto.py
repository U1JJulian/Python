class Producto():
    def __init__(self, Nombre, Precio, Stock):
        self.Nombre = Nombre
        self.Precio = Precio
        self.Stock = Stock
    def __str__(self):
        return f" \n Nombre del producto: {self.Nombre} \n Precio del producto: {self.Precio} \n Cantidad de productos disponibles: {self.Stock}"

miProducto = Producto("Samsung s18", 5000, 15)
print(miProducto)

