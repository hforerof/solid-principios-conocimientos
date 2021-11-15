from abc import ABCMeta, abstractmethod


class servicio_de_entrega(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def entregar_producto(self, producto):
        pass


class entrega_conductor(servicio_de_entrega):

    def entregar_producto(self, producto):

        pass


class compañia_de_entrega(object):

    def __init__(self, servicio_de_entrega):
        self.servicio_de_entrega = servicio_de_entrega

    def enviar_producto(self, producto):
        self.servicio_de_entrega.entregar_producto(producto)