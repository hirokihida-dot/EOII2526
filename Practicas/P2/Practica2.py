import threading
import time
import random
import matplotlib.pyplot as plt


class Contenedor:   # Se crea la clase Contenerdor 
    MAX_VALOR = 20  # Se establece como variable global el Valor Máximo
    MIN_VALOR = 0   # Se establece como variable global el Valor Mínimo

    def __init__(self, var_compartida = 10):  # Constructor
        self.var_compartida = var_compartida    # variable compartida
        self.monitor = threading.Condition()    # variable tipo Monitor con Condition para iniciar los métodos
        
    def incrementar(self):    # Método incrementar
        with self.monitor:    # Avisa que va a entrar en una sección de código protegida, solo 1 hilo a la vez
            while self.var_compartida >= self.MAX_VALOR: # Comprueba la condición
                print("Esperando a que cumpla la condición")
                self.monitor.wait()
            self.var_compartida += 1 # Suma uno a la variable
            print("Incrementando en 1")
            self.monitor.notify_all() # Notifica al resto de hilos

    def decrementar(self): # Método decrementar
        with self.monitor:
            while self.var_compartida <= self.MIN_VALOR:
                print("Esperando a que cumpla la condición")
                self.monitor.wait()
            print("Decrementando en 1")
            self.var_compartida -= 1
            self.monitor.notify_all()

    def leer_valor(self):
        with self.monitor:
            return self.var_compartida

def hilo_productor(contenedor, iteraciones, intervalo):
    for _ in range(iteraciones):
        contenedor.incrementar() # incremento
        time.sleep(0.2)


def hilo_consumidor(contenedor, iteraciones, intervalo):
    for _ in range(iteraciones):
        contenedor.decrementar()
        time.sleep(0.2)


def hilo_visualizador(contenedor, valores, finalizar):
    while not finalizar.wait(0.1):
        valores.append(contenedor.leer_valor())


class Grafica:
    def __init__(self, valores):
        self.datos_grafica = valores
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.hl, = self.ax.plot(self.datos_grafica)
        plt.ylim(contenedor.MIN_VALOR-1, contenedor.MAX_VALOR+1)
        plt.xlim(0, len(valores))
        plt.show()


if __name__ == "__main__":
    contenedor = Contenedor() # Generamos un objeto de la clase contenedor
    valores = [] # Creamos un vector para guardar los datos
    finalizar = threading.Event() # Crea un evento de finalización para avisar a los hilos

    visualizador = threading.Thread(target=hilo_visualizador, args=(contenedor, valores, finalizar))
    hilos = [] # Creamos una lita de hilos para guardar los hilos que creamos

    for _ in range(15):   # Bucle para hacer las iteraciones
        iteraciones = random.randint(10, 20) # genera un número aleatorio entre 10 y 20
        productor = threading.Thread(target=hilo_productor,args=(contenedor, iteraciones, random.uniform(0.01,0.1))) # Crea los hilos productores con las iteraciones designadas
        consumidor = threading.Thread(target=hilo_consumidor,args=(contenedor, iteraciones, random.uniform(0.01,0.1))) # Crea los hilos consumidores con las iteraciones designadas
        hilos.extend((productor, consumidor)) # Añadimos los hilos a la lista de hilos 

    visualizador.start() # Lanzamos el hilo visualizador
    for hilo in hilos: # bucle para lanzar todos los hilos creados en la lista
        hilo.start()

    for hilo in hilos: # bucle para Esperar a todos los hilos 
        hilo.join()
    finalizar.set() # seteamos finalizar como condicion para visualizar
    visualizador.join() #Espera a que termine visualizar
    Grafica(valores) # lanza gráfica
    

