class hombrelibre(object):

    def __init__(self, posicion):
        self.posicion = posicion

    def walk_north(self, distancia):
        self.posicion[1] += distancia

    def walk_south(self, distancia):
        self.posicion[0] += distancia


class Prisonero(object):
    prision_locacion= (3, 3)

    def __init__(self):
        self.posicion = self.prision_locacion