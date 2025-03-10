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
    
    def calcular_costo(self):
        return self.precio
    
    def __str__(self):
        return f" \n Nombre del producto: {self.Nombre} \n Precio del producto: {self.__Precio} \n Cantidad de productos disponibles: {self.Stock}"

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

class Usuario:
    def __init__(self,nombre, email, password):
        self.Nombre = nombre
        self.Email = email
        self.__Password = password
    
    @property
    def Password(self):
        return self.__Password
    
    def __str__(self):
        return f"\n Usuario: {self.Nombre} \n Correo: {self.Email}"

class Cliente(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email, password)
    

class Carrito:
    def __init__(self):
        self.lstProductos = []
    
    def agregar_producto(self, Producto):
        if Producto.disponible():
            self.lstProductos.append(Producto)
            if Producto.stock != -1:
                Producto.stock -=1
            print(f"{Producto.nombre} agregado al carrito.")
        else:
            print(f"{Producto.nombre} no esta disponible.")

    def mostrar_productos(self):
        for p in self.lstProductos:
            print (f"{p.Nombre}: ${p.precio}")



