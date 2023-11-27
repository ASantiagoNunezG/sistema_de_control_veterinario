'''
Encolar: Agregar un elemento al final de la cola.
Desencolar: Quitar y recuperar el elemento en la parte delantera de la cola.
Verificación de vacío: Comprobar si la cola está vacía.
Tamaño: Obtener el número de elementos en la cola.
Frente: Observar el elemento en la parte delantera de la cola sin eliminarlo.
Limpieza: Vaciar la cola eliminando todos los elementos.
'''
class Fila:

    #constructor
    def __init__(self):
        self.elementos = []
    
    def mostrar(self):
        print(self.elementos)
    
    def fila_vacia(self):
        if len(self.elementos) == 0:
            return True
        else:
            return False
    
    def encolar(self, elemento):
        self.elementos.append(elemento)
    
    def desencolar(self):
        if self.fila_vacia() is False:
            del(self.elementos[0])     
        else:
            print('La fila esta vacia')
            
    def tamano(self):
        print(f'La longitud de la fila es de: {len(self.elementos)}')
    
    def frente(self):
        print(self.elementos[0])

    def limpieza(self):
        del(self.elementos[:])