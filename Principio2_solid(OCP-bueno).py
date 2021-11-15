from abc import ABCMeta, abstractmethod


class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        # Override Shape draw method
        pass