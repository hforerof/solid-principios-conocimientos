"""
Principios Solid
L: Sustitución de Liskov

las clases derivadas deben poder sustituirse por sus clases base
"""
class Vehiculo:

    def __init__(self, nombre):
        self.nombre = nombre

    def num_ruedas(self):
        pass

class Motocicleta(Vehiculo):
    def __init__(self):
        super().__init__('Motocicleta')

    def num_ruedas(self):
        return 2

if __name__ == "__main__":
    moto = Motocicleta()

    print(" * * * S O L O  T R A S P O R T E S * * * ")
    print(" ")
    print("Cantidad de ruedas : ",moto.num_ruedas())

"""
deberíamos poder usar cualquiera de sus subclases sin interferir en la funcionalidad del programa.  
"""