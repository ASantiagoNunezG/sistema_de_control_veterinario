class Pila:
#Push: Agregar un elemento (push) en la parte superior de la pila.
#Pop: Quitar y recuperar el elemento en la parte superior de la pila.
#Verificación de vacío: Comprobar si la pila está vacía.
#Tamaño: Obtener el número de elementos en la pila.
#Peek: Observar el elemento en la parte superior de la pila sin eliminarlo.
#Limpieza: Vaciar la pila eliminando todos los elementos.''''''

    #constructor
    def __init__(self):
        self.elementos = []
    
    def pila_vacia(self):
        if len(self.elementos) == 0:
            return True
        else:
            return False

    def agregar(self, elemento):
        self.elementos.append(elemento)
    
    def quitar(self):
        pila_vacia = self.pila_vacia()
        if pila_vacia is False:
            self.elementos.pop()
        else:
            print('Ya no hay elementos por desapilar')
        
    
    def mostrar(self):
        pila = self.elementos
        pila_vacia = self.pila_vacia()
        if pila_vacia is False:
            for i in range(len(pila)):
                print(pila[-1 + (-i)])
        else:
            print('Lista vacia')        

    def tamano(self):
        print(len(self.elementos))

    def cima(self):
        print(self.elementos[-1])

    def limpieza(self):
        del(self.elementos[:])