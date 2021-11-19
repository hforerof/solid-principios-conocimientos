"""
Principios Solid
S: Responsabilidad única.
"""
class Poligono:
    """
    Define un polígono según su base y su altura.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Rectangulo(Poligono):

    def area(self):
        return self.base * self.altura
"""
Es el principio más fácil de romper y también de detectar.
"""
class Triangulo(Poligono):

    def area(self):
        return (self.base * self.altura) / 2

rectangulo = Rectangulo(20, 10)
triangulo = Triangulo(20, 12)

print(" * * * P O L I G O N O S * * * ")
print(" ")
print("Área del rectángulo: ", rectangulo.area())
print("Área del triángulo:", triangulo.area())
"""
Nuestro programa será mucho más cohesivo y estará más encapsulado aplicando este principio.
"""
