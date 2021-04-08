
pregunta = 'Introduce un número para saber si es par o impar \r\n'
pregunta += '(Teclee "cerrar" para finalizar la aplicación) \r\n'

preguntar = True


while preguntar:
    numero = input(pregunta)
    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print('El número es par')
        else:
            print('El número es impar')        