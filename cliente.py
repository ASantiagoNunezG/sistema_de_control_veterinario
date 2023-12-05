class Cliente:
    def __init__(self, nombres, apellidos, correo, celular):
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.celular = celular

    def __str__(self):
        return f'''
            Información del cliente
            Nombres:                       {self.nombres}
            Apellidos:                     {self.apellidos}
            Correo:                        {self.correo}
            Celular:                       {self.celular}
            '''
