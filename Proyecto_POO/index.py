class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio  # Precio es privado (no accesible directamente)
        self.stock = stock  # Cantidad disponible en stock

    @property
    def precio(self):
        return self.__precio  # Devuelve el precio (getter)
    
    def disponible(self):
        return self.Stock > 0

    def calcular_costo(self):
        return self.precio  # Retorna el precio del producto

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, -1)  # Stock en -1 (infinito)

    def calcular_costo(self):
        return self.precio * 0.9  # Descuento del 10%

    def __str__(self):
        return f"{self.nombre} (Digital) - ${self.precio}"

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre} ({self.email})"

class Carrito:
    def __init__(self):
        self.productos = []  # Lista de productos en el carrito

    def agregar_producto(self, producto):
        if producto.stock > 0 or producto.stock == -1:  # Stock infinito para digitales
            self.productos.append(producto)
            if producto.stock != -1:
                producto.stock -= 1  # Reduce el stock si es físico
            return True
        return False

    def calcular_total(self):
        return sum(p.calcular_costo() for p in self.productos) if self.productos else 0

    def __str__(self):
        return "\n".join(str(p) for p in self.productos) or "Carrito vacío"

class Tienda:
    def __init__(self):
        self.catalogo = []  # Lista de productos en la tienda

    def agregar_al_catalogo(self, producto):
        self.catalogo.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.catalogo:
            if producto.nombre == nombre:
                return producto
        return None

    def realizar_compra(self, cliente, carrito):
        if not carrito.productos:
            return "Compra cancelada: carrito vacío."
        total = carrito.calcular_total()
        return f"Compra de {cliente}:\n{carrito}\nTotal: ${total}"
