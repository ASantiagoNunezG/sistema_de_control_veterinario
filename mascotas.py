class Mascota:
    def __init__(self, codigo, nombre, especie, raza, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.siguiente = None
        self.anterior = None

class ListaMascotas:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregar_mascota(self, codigo, nombre, especie, raza, edad):
        nueva_mascota = Mascota(codigo, nombre, especie, raza, edad)
        if self.inicio is None:
            self.inicio = self.fin = nueva_mascota
        else:
            nueva_mascota.anterior = self.fin
            self.fin.siguiente = nueva_mascota
            self.fin = nueva_mascota

    def mostrar_mascotas(self):
        actual = self.inicio
        while actual:
            print(f"\nCódigo: {actual.codigo}\nNombre: {actual.nombre}\nEspecie: {actual.especie}\nRaza: {actual.raza}\nEdad: {actual.edad}")
            actual = actual.siguiente

    def buscar_mascota(self,codigo):
        actual = self.inicio
        while actual:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def eliminar_mascota(self, codigo):
        mascota = self.buscar_mascota(codigo)
        if mascota:
            if mascota.anterior:
                mascota.anterior.siguiente = mascota.siguiente
            else:
                self.inicio = mascota.siguiente

            if mascota.siguiente:
                mascota.siguiente.anterior = mascota.anterior
            else:
                self.fin = mascota.anterior

            return True
        return False