"""
Principios Solid
I: Segregación de la Interfaz

Una clase nunca debe ser forzada a implementar una interface que no usa, empleando métodos que no tiene por qué usar.
"""
class Operaciones:
    """
    * * * OPERACIONES CON MAS DE 2 NUMEROS * * *
    """
    def __init__(self, NumeroUno, NumeroDos, NumeroTres):
        self.NumeroUno = NumeroUno
        self.NumeroDos = NumeroDos
        self.NumeroTres = NumeroTres

class Sumatoria(Operaciones):

    def suma_total(self):
        return self.NumeroUno + self.NumeroDos + self.NumeroTres

class Multiplicacion(Operaciones):

    def multi(self):
        return self.NumeroUno * self.NumeroDos * self.NumeroTres

"""
Haz interfaces que sean específicas para un tipo de proceso 
"""
Sumatoria = Sumatoria(6, 8, 5)
Multiplicacion = Multiplicacion(5, 5, 10)

print(" * * * OPERACIONES * * * ")
print(" ")
print("El resultado de la multiplicacion : ", Multiplicacion.multi())
print("El resultado de la suma total es : ", Sumatoria.suma_total())

