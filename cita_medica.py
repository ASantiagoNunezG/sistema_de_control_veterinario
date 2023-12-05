class CitaMedica:
    def __init__(self,ID, fecha, hora, medico, asistente, recepcionista, cliente, mascota, diagnostico = 'En proceso', condicion_final = 'En proceso'):
        self.ID = ID
        self.fecha = fecha
        self.hora = hora
        self.medico = medico
        self.asistente = asistente
        self.recepcionista = recepcionista
        self.cliente = cliente
        self.diagnostico = diagnostico
        self.mascota = mascota
        self.condicion_final = condicion_final

    def __str__(self):
        return f'''

            -----------Cita Médica---------------
            ID:                             {self.ID}
            Fecha:                          {self.fecha}
            Hora:                           {self.hora}
            Nombre del médico veterinario:  {self.medico}
            Nombre del asistente:           {self.asistente}
            Nombre del recepcionista(tú):   {self.recepcionista}\n
            Cliente:                        {self.cliente}
            Mascota:                        {self.mascota}
            Diagnostico:                    {self.diagnostico}
            Condición final:                {self.condicion_final}
            '''