from cliente import *
from mascota import *
from cita_medica import *
from lista_enlazada_doble import *
from cola import *
from pila import *

def menu():
    print('''
    |         -----Sistema de Control-----            |
    |1. Registrar cliente                             |
    |2. Registrar mascota                             |
    |3. Registrar cita médica                         |
    |4. Registrar diagnóstico y condición final       |
    |5. Salir                                         |
    ''')

def opciones(opcion, nuevo_cliente, nueva_mascota):
    cola = Cola()
    pila = Pila()
    while True:
        if opcion == 1:
            print('Ingresando datos del cliente...')
            nombres = input('Nombres: ')
            apellidos = input('Apellidos: ')
            correo = input('Correo: ')
            celular = input('Celular: ')
            print('----------------------------------')
            try:
                nuevo_cliente = Cliente(nombres, apellidos, correo, celular)
                print('Registro exitoso')
                print('----------------------------------')
                menu()
            except ValueError:
                print('Error al registrar el nuevo cliente')
                print('----------------------------------')
                menu()
        elif opcion == 2:
            print('Ingresando datos de la mascota...')
            nombre = input('Nombre: ')
            especie = input('Especie: ')
            raza = input('Raza: ')
            edad = input('Edad: ')
            print('----------------------------------')
            try:
                nueva_mascota = Mascota(nombre, especie, raza, edad)
                print('Registro exitoso')
                print('----------------------------------')
                menu()
            except ValueError:
                print('Error al registrar la nueva mascota')
                print('----------------------------------')
                menu()
        elif opcion == 3:
            print('Agendando la cita médica...')
            ID = input('Establezca un identificador para la cita: ')
            fecha = input('Establecer fecha: ')
            hora = input('Establecer hora: ')
            medico = input('Nombre del médico: ')
            asistente = input('Nombre de asistente: ')
            recepcionista = input('Ingrese su nombre (ud.): ')
            print('----------------------------------')
            cliente = nuevo_cliente
            mascota = nueva_mascota
            try:
                nueva_cita = CitaMedica(ID, fecha, hora, medico, asistente, recepcionista, cliente, mascota)
                cola.encolar(nueva_cita)
                print('Cita agendada')
                print('----------------------------------') 
                cola.frente()
                menu()
            except ValueError:
                print('Error al agendar la cita')
                print('----------------------------------')
                menu()
        elif opcion == 4:
            print('\nLuego de la cita')
            diagnostico = input('Diagnóstico final: ')
            condicion_final = input('Describa la condición final de la mascota: ')
            print('----------------------------------')
            if cola.fila_vacia() is False:
                cita_actual = nueva_cita
                cita_actual.diagnostico = diagnostico
                cita_actual.condicion_final = condicion_final
                print('Diagnóstico y condición actualizados')
                print('----------------------------------')
                cola.frente()
                #Agregando cita actual al historial(pila)
                pila.agregar(cita_actual)
                menu()
            else:
                print('No hay citas agendadas')
                print('----------------------------------')
                menu()
        elif opcion == 5:
            print('Hasta luego.')
            pila.mostrar()
            break
        else:
            print('Seleccione nuevamente')
        opcion = int(input('Elija una opcion: '))

def menu_interactivo():
    nuevo_cliente = None
    nueva_mascota = None

    menu()
    opcion = input('Elija una opcion: ')
    try:
        opcion_entero = int(opcion)
        if 1 <= opcion_entero <= 5:
            opciones(opcion_entero, nuevo_cliente, nueva_mascota)
        else:
            print('Por favor, ingrese un valor válido (entre 1 y 5).')
    except ValueError:
        print('Por favor, ingrese un valor numérico.')

if __name__ == "__main__":
    menu_interactivo()
    
