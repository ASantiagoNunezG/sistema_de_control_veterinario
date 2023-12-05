class Cola:

    #constructor
    def __init__(self):
        self.elementos = []
        
    def __str__(self):
        return str(self.elementos)
    
    def mostrar(self):
        for i in self.elementos:
            print(i)
    
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

