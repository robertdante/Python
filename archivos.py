def app():

#Crear un archivo

    archivo = open('archivo.txt', 'w')

    for i in range(0, 20):
        
        archivo.write(f'Esta es la linea {i}\r\n')

#Cerrar el archivo creado

    archivo.close()

#Ver contenido por consola con la funcion with open. No es necesario cerrar el archivo

    with open('archivo.txt') as apertura:
        for contenido in apertura:
            print(contenido.rstrip())

app()
