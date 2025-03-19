import unittest
from index import Carrito, Producto

class TestCarrito(unittest.TestCase):
    def test_calcular_total(self):
        carrito = Carrito()

        # Productos de prueba
        producto1 = Producto("Laptop", 1000, 5)  # $1000
        producto2 = Producto("Mouse", 50, 10)     # $50
        producto3 = Producto("Ebook", 15, -1)     # $15 (digital, stock infinito)

        # Agregamos productos al carrito
        carrito.agregar_producto(producto1)  # +1000
        carrito.agregar_producto(producto2)  # +50
        carrito.agregar_producto(producto3)  # +15

        # Calculamos el total esperado
        total_esperado = 1000 + 50 + 15

        # Aseguramos que calcular_total devuelve el total esperado
        self.assertEqual(carrito.calcular_total(), total_esperado)

# Ejecutar las pruebas si este archivo se ejecuta directamente
if __name__ == "__main__":
    unittest.main()
