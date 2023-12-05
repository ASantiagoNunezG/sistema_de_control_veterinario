class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return str(self.dato)

class ListaEnlazadaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def esta_vacia(self):
        return self.inicio is None

    def agregar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.inicio
            self.inicio.anterior = nuevo_nodo
            self.inicio = nuevo_nodo

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def mostrar(self):
        actual = self.inicio
        while actual:
            print(actual.dato, end=" ------------------------------")
            actual = actual.siguiente
        print("\nNo hay mas datos")

    def buscar(self, dato):
        actual = self.inicio
        while actual:
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None

    def eliminar(self, dato):
        nodo_a_eliminar = self.buscar(dato)
        if nodo_a_eliminar:
            if nodo_a_eliminar.anterior:
                nodo_a_eliminar.anterior.siguiente = nodo_a_eliminar.siguiente
            else:
                self.inicio = nodo_a_eliminar.siguiente

            if nodo_a_eliminar.siguiente:
                nodo_a_eliminar.siguiente.anterior = nodo_a_eliminar.anterior
            else:
                self.fin = nodo_a_eliminar.anterior

    def actualizar(self, dato_antiguo, dato_nuevo):
        nodo_a_actualizar = self.buscar(dato_antiguo)
        if nodo_a_actualizar:
            nodo_a_actualizar.dato = dato_nuevo
