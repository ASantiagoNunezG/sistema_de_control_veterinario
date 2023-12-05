class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
    
    def __str__(self):
        return f'''
            Información de la mascota
            Nombre:                       {self.nombre}
            Especie:                      {self.especie}
            Raza:                         {self.raza}
            Edad:                         {self.edad}
            '''