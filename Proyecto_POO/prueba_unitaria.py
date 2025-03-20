import unittest
from index import Carrito, Producto

class TestCarrito(unittest.TestCase):
    def test_calcular_total_carrito_vacio(self):
        carrito = Carrito()  # Crear carrito vacío
        self.assertEqual(carrito.calcular_total(), 0)  # Debe ser 0

    def test_calcular_total_con_productos(self):
        carrito = Carrito()
        producto1 = Producto("Laptop", 1000, 5)  # Precio 1000, stock 5
        producto2 = Producto("Mouse", 50, 10)  # Precio 50, stock 10

        carrito.agregar_producto(producto1)
        carrito.agregar_producto(producto2)

        total_esperado = 1000 + 50  # 1050
        self.assertEqual(carrito.calcular_total(), total_esperado) 

unittest.main()
