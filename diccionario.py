#Crear un diccionerio

cancion = {

    'artista' : 'metallica',   #llave y valor
    'cancion' : 'enter sandman', 
    'lanzamiento' : 1992, 
    'likes' : 3000
}

print(cancion)

#Acceder a un elemento concreto del diccionario

print(cancion['artista'])
print(cancion['cancion'])

#Utilizar un valor del diccionario como variable

grupo = cancion['artista']

print(f'Estoy escuchando a {grupo}')

#Agregar nuevos valores

cancion['genero'] = 'Heavy Metal'
print(cancion)

#Reemplazar valor existente

cancion['lanzamiento'] = 1993
print(cancion)

#Eliminar un valor

del cancion['lanzamiento']
print(cancion)