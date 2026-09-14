#ejemplo de cómo crear una clase

#class NombreDeLaClase:
    # codigo de la clase
    # la función especial __init__ es el constructor de la clase, se ejecuta al crear un objeto de la clase
    # para crear un objeto de la clase se utiliza el nombre de la clase seguido entre parentesis de los valores de los atributos
    # para llamar a la clase Rectangulo sería Rectangulo (base, altura), PE: rectangulo = Rectangulo (5, 10)
    # para acceder a las propiedades y metodos se usa (.)
    # por ejemplo print (rectangulo.base) o print (rectangulo.area())

class Rectangulo:

    num_rectangulos = 0  # variable de clase, se puede acceder a ella con Rectangulo.num_rectangulos

    def __init__(self, base, altura):  
        self.base = base
        self.altura = altura
        Rectangulo.num_rectangulos += 1 #definimos un contador de objetos de la clase Rectangulo, que se incrementa cada vez que se crea un objeto de la clase Rectangulo.

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


#Para crear una clase heredada, llamamos a una nueva clase y entre parentesis ponemos el nombre de la clase padre, por ejemplo: class Cuadrado(Rectangulo):

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)  # función super() llama al constructor de la clase padre, en este caso Rectangulo, y le pasa los valores de los atributos base y altura, que en este caso son iguales al valor del lado del cuadrado.
        # También se puede llamar al constructor de la clase padre con Rectangulo.__init__(self, lado, lado) para inicializar los atributos de la clase padre.
        
# para crear un objeto de la clase Cuadraro se hará de la misma forma que Rectangulo.
# se puede añadir una variable de clase a la clase Rectangulo, que será compartida por todos los objetos de la clase.