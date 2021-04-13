import os

CARPETA = 'contactos/'
EXTENSION = '.txt'

class Contacto():

    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria



def app():

    crear_directorio()

    mostrar_menu()

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False

        elif opcion == 2:
            editar_contacto()
            preguntar = False

        elif opcion == 3:
            mostrar_contactos()
            preguntar = False

        elif opcion == 4:
            buscar_contacto()
            preguntar = False

        elif opcion == 5:
            eliminar_contacto()
            preguntar = False

        else:
            print('Elija una opción válida')                    



def agregar_contacto():
    print('Escribe los datos para agregar un nuevo contacto')
    nombre_contacto = input('Nombre del contacto:\r\n')
    existe = existe_contacto(nombre_contacto)


    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            telefono_contacto = input('Introduce el número de teléfono:\r\n')
            categoria_contacto = input('Agrega categoría:\r\n')

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)


            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono+ '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            print('Contacto creado correctamente')

    else:
            print('El contacto ya existe. Utilice otro nombre')    

    app()
         
def editar_contacto():
    
    nombre_anterior = input('Introduce el nombre que desea editar \r\n')
    existe = existe_contacto(nombre_anterior)

    if existe:
        
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Introduce el nuevo nombre:\r\n')
            telefono_contacto = input('Introduce el nuevo telefono:\r\n')
            categoria_contacto = input('Introduce la nueva categoría:\r\n')

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            print('Contacto editado correctamente')
    else:
        print('El contacto no existe')

    app()        

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            
            print('\r\n')

def buscar_contacto():

    nombre = input('Introduce el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

    app()                

def eliminar_contacto():
    nombre = input('Introduce el contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado correctamente')
    except IOError:
        print('No existe el contacto')  

    app()    

def mostrar_menu():
    print('Seleccione del menú lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):      #Revisa si existe la carpeta
        os.makedirs(CARPETA)             #Crea una carpeta
  
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()
