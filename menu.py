from mascotas import *
from pila import *
def menu_lista():
    print('''
    |         -----Menú-----            |
    |1. Cliente                         |
    |2. Mascota                         |
    |3. Cita médica                     |
    |4. Historial de atención           |
    |5. Otros                           |
    |6. Salir                           |
    ''')

def cliente_opcion():
    print('Seleccionaste la opción Cliente')

def mascota_opcion():
    print('Seleccionaste la opción Mascota')
    lista = ListaMascotas()
    codigo = input('Codigo de la mascota: ')
    nombre = input('Nombre de la mascota: ')
    especie = input('Especie de la mascota: ')
    raza = input('Raza de la mascota: ')
    edad = input('Edad de la mascota: ')
    nuevo = lista.agregar_mascota(codigo, nombre, especie, raza, edad)
    pila_mascota = Pila()
    pila_mascota.agregar(nuevo)
    pila_mascota.mostrar()
    
def cita_medica_opcion():
    print('Seleccionaste la opción Cita Médica')

def historial_atencion_opcion():
    print('Seleccionaste la opción Historial de Atención')

def otros_opcion():
    print('Seleccionaste la opción Otros')

def salir_opcion():
    print('Seleccionaste la opción Salir')

def opciones(opcion):
    while True:
        if opcion == 1:
            cliente_opcion()
        elif opcion == 2:
            mascota_opcion()
        elif opcion == 3:
            cita_medica_opcion()
        elif opcion == 4:
            historial_atencion_opcion()
        elif opcion == 5:
            otros_opcion()
        elif opcion == 6:
            salir_opcion()
            break
        else:
            print('Seleccione nuevamente')
        opcion = int(input('Elija una opcion: '))

def menu_interactivo():
    menu_lista()
    opcion = input('Elija una opcion: ')
    try:
        opcion_entero = int(opcion)
        if 1 <= opcion_entero <= 6:
            opciones(opcion_entero)
        else:
            print('Por favor, ingrese un valor válido (entre 1 y 6).')
            menu_interactivo()
    except ValueError:
        print('Por favor, ingrese un valor numérico.')
        menu_interactivo()

