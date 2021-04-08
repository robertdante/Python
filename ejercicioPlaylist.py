playlist = {}
playlist['canciones'] = []


def app():
    agregar_nombre = True

    while agregar_nombre:
        nombre_playlist = input('¿Cómo quieres llamar a la playlist? \r\n')
    
        if nombre_playlist:                          
            playlist['nombre'] = nombre_playlist
            agregar_nombre = False
    

def agregar_canciones():
    agregar_cancion = True
    nombre_cancion = '¿Qué canción deseas agregar? \r\n'
    nombre_cancion+= '(Teclee "salir" para dejar de añadir canciones) \r\n'

    while agregar_cancion:

        nombre_playlist = playlist['nombre']
        nombre_cancion = f'¿Qué canción deseas agregar a {nombre_playlist}? \r\n'
        nombre_cancion+= '(Teclee "salir" para dejar de añadir canciones) \r\n'
        cancion = input(nombre_cancion)
 
        if cancion == 'salir':
            agregar_cancion = False
            mostrar_resumen()
    
        else:
        
            playlist['canciones'].append(cancion)
  
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()
agregar_canciones()                