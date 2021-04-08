def informacion(nombre, puesto = 'desconocido'):
    print(f'Soy {nombre} y soy {puesto}')

informacion('Paco', 'programador')
informacion('Pedro', 'albañil')
informacion('Lola')   

def info(nickname):
    return nickname

apodo = info('El chino')
print(apodo)    