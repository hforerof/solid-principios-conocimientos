"""
Principios Solid
D:Inversión de Dependencias
Las entidades deben depender de abstracciones no de concreciones.
"""
class A:
    def print_a(self):
        print('a')
class B:
    def print_b(self):
        print('b')
class C(A, B):
    def print_c(self):
        print('c')


c = C()
print("****************")
c.print_a()
c.print_b()
c.print_c()
print("****************")
