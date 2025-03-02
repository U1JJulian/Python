class Gato:
    def __init__(self, Nombre, Color):
        self.Nombre = Nombre
        self.Color = Color
    def maullar(self):
        return f"{self.Nombre} dice: miauu!"

miGatoObeso = Gato("Garfild","Naranja")
print(miGatoObeso.maullar())