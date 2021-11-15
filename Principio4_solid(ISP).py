from abc import ABCMeta, abstractmethod


class Carro(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def accelerar(self):
        pass


class maquina_del_tiempo(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def de_vuelta_al_pasado(self):
        pass

    @abstractmethod
    def regreso_al_futuro(self):
        pass


class Mustang(Carro):

    def encender(self): pass

    def accelerar(self): pass


class DeloRean(Carro, maquina_del_tiempo):
    def encender(self): pass

    def accelerar(self): pass

    def de_vuelta_al_pasado(self): pass

    def regreso_al_futuro(self): pass