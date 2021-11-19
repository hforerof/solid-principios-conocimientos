# coding: utf-8
# Your code here!
"""
Principios Solid
O:Abierto/Cerrado.
Las entidades deben estar abiertas para su extensión y cerradas para su modificación.
"""
class Calculadora:
    """
    CALCULADORA MATEMATICA
    """
    def __init__(self, Numero1, Numero2):
        self.Numero1 = Numero1
        self.Numero2 = Numero2

class Boton_suma(Calculadora):

    def suma(self):
        return self.Numero1 + self.Numero2

class Boton_resta(Calculadora):

    def resta(self):
        return self.Numero1 - self.Numero2

"""
las clases que usas deberían estar abiertas para poder extenderse y cerradas para modificarse
"""
class Boton_multiplicacion(Calculadora):

    def multiplicacion(self):
        return self.Numero1 * self.Numero2

Boton_suma = Boton_suma(4, 5)
Boton_resta = Boton_resta(2021, 1976)
Boton_multiplicacion = Boton_multiplicacion(15, 5)

print(" * * * CALCULADORA MATEMATICA * * * ")
print(" ")
print("El resultado de la suma es : ", Boton_suma.suma())
print("El resultado de la resta es :", Boton_resta.resta())
print("El resultado de la multiplicacion es : ", Boton_multiplicacion.multiplicacion())
