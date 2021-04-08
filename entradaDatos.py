nombre = input('¿Cuál es tu nombre?: \r\n')
print(f'Hola {nombre}')

#Las entradas siempre son string, para trabajar con numeros hay que convertir la entrada a int

edad = input('¿Cuál es tu edad?: \r\n')

edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aún no puedes votar')    

#Utilización del módulo % que muestra el resto de una división

numero = input('Introduce un número para saber si es par o impar \r\n')
numero = int(numero)

if numero % 2 == 0:
    print('El número es par')
else:
    print('El número es impar')    
