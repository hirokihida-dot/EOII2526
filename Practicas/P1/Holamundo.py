# Programa hola mundo

# Definicion de la función que imprime

def print_hola(cadena):
    print(f'Hola{cadena}')

if __name__ == '__main__':
    print_hola(' mundo')

# La funcion print permite imprimir una cadena en pantalla
# también se puede escribir números convirtiendolos antes a cadena

    num = 5
    print('El número es: ' + str(num))

# La función open() permite abrir un archivo en modo escritura y escribir en el

    with open("archivo.txt", "w") as f:
        f.write("Hola mundo\n")

    numeros = [1, 2, 3, 4, 5]
    with open("numeros.txt", "w") as f: 
        for numero in numeros:
            f.write(str(numero) + "\n")

# La función input() permite leer una cadena desde teclado

    nombre = input("Escriba su nombre: ")
    print("Hola, " + nombre + "!")

# si la cadena es un número, se puede convertir a entero

    num = int(input("Escriba un número: "))
    print("El número que escribiste es: " + str(num))

# La función open() también permite abrir un archivo en modo lectura y leer su contenido con read() o readlines()

    with open ( "archivo.txt", "r") as f:
        contenido = f.read()
        print("Contenido del archivo: ")
        print(contenido)

# las f-strings permiten formatear cadenas de manera más sencilla y legible e interpolarlas

    name = "Juan"
    print(f"Hola {name}, !") # Output: Hola Juan, !

    x,y = 4, 5
    print(f"La suma de {x} y {y} es {x+y}") # Output: La suma de 4 y 5 es 9

# las f-strings también permiten cálculos y expresiones dentro de las llaves

def to_uppercase (text):
    return text.upper()

    message =  "hello, world"
    print(f"The message is: {to_uppercase(message)}") # Output: The message is: HELLO, WORLD

# Algo a tener en cuenta es que permiten un control más fino sobre la forma en que se formatean los valores.

    pi = 3.14159265
    print(f"El valor de pi con 2 decimales es: {pi:.2f}") # Output: El valor de pi con 2 decimales es: 3.14

# El modulo threading proporciona una interfaz para trabajar con hilos en un programa. Se puede utilizar la funcion threading.Thread o crear una clase que herede Thread.

import threading

def print_message():
    print(f"Hola , soy el thread({threading.current_thread().name})")

# Crear Threads
thread1 = threading.Thread(target=print_message, name="Hilo-1")
thread2 = threading.Thread(target=print_message, name="Hilo-2")

# Iniciar Threads
thread1.start()
thread2.start()

# Esperar a que los threads terminen
thread1.join()
thread2.join()


# Si se quiere tener un mayor control sobre el hilo y se necesitan metodos personalizados es mejor crear una clase que herede de Thread.

import threading

class MiHilo(threading.Thread):
    def run(self):
        print(f"Hola, soy el thread {self.name}")

# Crear instancias de la clase MiHilo
hilo1 = MiHilo(name="Hilo-1")
hilo2 = MiHilo(name="Hilo-2")

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()


# Un ejemplo de como utilizar el módulo threading para crear dos hilos que impriman un mensaje con delay

import threading
import time

def print_message(message, delay):
    time.sleep(delay)
    print(message)

if __name__ == "main":
    # Crear hilos
    t1 = threading.Thread(target=print_message, args=("Hola desde el hilo 1", 5 ))
    t2 = threading.Thread(target=print_message, args=("Hola desde el hilo 2", 7 ))

    # Iniciar hilos
    t1.start()
    t2.start()

# Ejemplo de procesos en Python propociona una interfaz similar.

import multiprocessing
import time

def print_message(message, delay):
    time.sleep(delay)
    print(message)  

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=print_message, args=("Hola desde el proceso 1", 5))
    process2 = multiprocessing.Process(target=print_message, args=("Hola desde el proceso 2", 7))

    # Iniciar procesos
    process1.start()
    process2.start()