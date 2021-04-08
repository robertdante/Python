print('Bienvenido al examen online de Historia del cine')
nombre = input('Escriba su nombre: \r\n')
print(f'Hola {nombre}, comencemos')

puntuacion = 0
pregunta1 = input('¿Paul Thomas Anderson ha ganado algún oscar a mejor director?: \r\n')

if pregunta1 == 'no':
    puntuacion += 1

pregunta2 = input('¿Akira Kurosawa era un director japonés?: \r\n')

if pregunta2 == 'si':
    puntuacion += 1

pregunta3 = input('¿Alguna mujer ha ganado el oscar a mejor dirección?: \r\n')

if pregunta3 == 'si':
    puntuacion += 1

pregunta4 = input('¿Ha dirigido alguna película Tim Robins?: \r\n')

if pregunta4 == 'si':
    puntuacion += 1

pregunta5 = input('¿Aún funcionan los estudios Zoetrope de Coppola?: \r\n')

if pregunta5 == 'no':
    puntuacion += 1

if puntuacion > 2:
    print(f'Enhorabuena has aprobado el examen. Tu puntuacion es {puntuacion}')
else:
    print(f'Lo siento, has suspendido el examen. Tu puntuacion es {puntuacion}')        
