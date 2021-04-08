#Acceder a un valor con get.

uncharted = {}

uncharted['jugador'] = 'Rober'
uncharted['personaje'] = 'Nathan Drake'
print(uncharted)

print(uncharted.get('jugador'))

#Acceder a un valor inexistente y generar mensaje de error

print(uncharted.get('consola', 'No existe ese valor'))

#Iterar por un diccionario sin retornar valor. Accediento solo a las llaves

for juego in uncharted:
    
    personaje = uncharted['personaje']
    if juego == 'personaje':
        print(f'Estas jugando con {personaje}')
    else:
    
         print('Selecciona un personaje')


print(uncharted)  

#Iterar por un diccionario accediendo a llaves y valores

for llave, valor in uncharted.items():
    print(llave)
    print(valor)

