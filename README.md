# solid-principios-conocimientos
PRINCIPIOS SOLID 

Sabemos que los POO (Programación Orientada a Objetos), permiten agrupar entidades con funcionalidades parecidas y relacionadas entre sí, no implicando que los programas no se vuelvan confusos o difíciles de mantener. 

De hecho, muchos programas se complican cada vez que se alimentan o agreguen funcionalidades o realiza mantenimiento. 

Por este problema Robert C. Martin estableció cinco principios para facilitar a los desarrolladores la labor de crear programas y mantenibles. 

Estos principios se llamaron S.O.L.I.D. por sus siglas en inglés:

    S: Single responsibility principle o Principio de responsabilidad única
    O: Open/closed principle o Principio de abierto/cerrado
    L: Liskov substitution principle o Principio de sustitución de Liskov
    I: Interface segregation principle o Principio de segregación de la interfaz
    D: Dependency inversion principle o Principio de inversión de dependencia
    
    
S: Principio de responsabilidad única

Como su propio nombre indica, establece que una clase, componente o microservicio debe ser responsable de una sola cosa (el tan aclamado término “decoupled” en inglés). Si por el contrario, una clase tiene varias responsabilidades, esto implica que el cambio en una responsabilidad provocará la modificación en otra responsabilidad.

Ejemplo 1 bad
class Customer(object):

    def __init__(self, name):
        self.name = name

    def store_customer(self, name):
        """ Store into db responsibility. """
        pass

    def generate_customer_report(self, name):
        """ Generate report responsibility. """
        pass


O: Principio abierto/cerrado

Establece que las entidades software (clases, módulos y funciones) deberían estar abiertos para su extensión, pero cerrados para su modificación.


L: Principio de substitución de Liskov

Declara que una subclase debe ser sustituible por su superclase, y si al hacer esto, el programa falla, estaremos violando este principio.

Cumpliendo con este principio se confirmará que nuestro programa tiene una jerarquía de clases fácil de entender y un código reutilizable.


I: Principio de segregación de interfaz

Este principio establece que los clientes no deberían verse forzados a depender de interfaces que no usan.

Dicho de otra manera, cuando un cliente depende de una clase que implementa una interfaz cuya funcionalidad este cliente no usa, pero que otros clientes sí usan, este cliente estará siendo afectado por los cambios que fuercen otros clientes en dicha interfaz.

Imaginemos que queremos definir las clases necesarias para albergar algunos tipos de aves. Por ejemplo, tendríamos loros, tucanes y halcones:
Hasta aquí todo bien. Pero ahora imaginemos que queremos añadir a los pingüinos. Estos son aves, pero además tienen la habilidad de nadar. Podríamos hacer esto:
El problema es que el loro no nada, y el pingüino no vuela, por lo que tendríamos que añadir una excepción o aviso si se intenta llamar a estos métodos. Además, si quisiéramos añadir otro método a la interfaz IAve, tendríamos que recorrer cada una de las clases que la implementa e ir añadiendo la implementación de dicho método en todas ellas. Esto viola el principio de segregación de interfaz, ya que estas clases (los clientes) no tienen por qué depender de métodos que no usan.

Lo más correcto sería segregar más las interfaces, tanto como sea necesario. En este caso podríamos hacer lo siguiente:
Así, cada clase implementa las interfaces de la que realmente necesita implementar sus métodos. A la hora de añadir nuevas funcionalidades, esto nos ahorrará bastante tiempo, y además, cumplimos con el primer principio (Responsabilidad Única).

D: Principio de inversión de dependencias

Establece que las dependencias deben estar en las abstracciones, no en las concreciones. Es decir:

    Los módulos de alto nivel no deberían depender de módulos de bajo nivel. Ambos deberían depender de abstracciones.
    Las abstracciones no deberían depender de detalles. Los detalles deberían depender de abstracciones.

En algún momento nuestro programa o aplicación llegará a estar formado por muchos módulos. Cuando esto pase, es cuando debemos usar inyección de dependencias, lo que nos permitirá controlar las funcionalidades desde un sitio concreto en vez de tenerlas esparcidas por todo el programa. Además, este aislamiento nos permitirá realizar testing mucho más fácilmente.


