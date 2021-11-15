from abc import ABCMeta, abstractmethod


class forma(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dibujar(self):
        pass


class rectangulo(forma):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def dibujar(self):
        pass