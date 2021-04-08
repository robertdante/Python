balance = 500
if balance > 550:
    print('Puedes pagar')
else:
    print('No puedes pagar')  


 #Para establecer una igualdad se utiliza ==

likes = 200
if likes == 200:
    print('Excelente, 200 likes')


#Para establcer una diferencia con if se utiliza la expresión if not

lenguaje = 'Python'
if not lenguaje == 'Java':
    print('Cool, Java no mola')
else:
    print('¿Seriously?')


#Para evaluar una condición con Boolean no es necesario añadir en la condicion la igualdad

usuario_identificado = True
if usuario_identificado:         #NO es necesario la expresión usuario_identificado == True
    print('Acceso al sistema')
else:
    print('Inicie sesión')   


#Utilización de if con el iterador para saber si un elemento está en la lista

lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

if 'PHP' in lenguajes:
    print('El lenguaje indicado está en la lista')
else:
    print('Oops, ese lenguaje no está en la lista') 


lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

for lenguaje in lenguajes:
    if lenguaje == 'Python':
        print('Excelente, Python')
    else:
        print(lenguaje)            


#if anidados

usuario_identificado = True
usuario_admin = False

if usuario_identificado:
    if usuario_admin:
        print('Acesso total')
    else:
        print('Acceso al sistema')
else:
    print('Inicie sesión')  


#elif

usuario_identificado = True
usuario_admin = True

if usuario_admin:
    print('Acceso total')
elif usuario_identificado:
    print('Acceso al sistema')
else:
    print('Inicie sesión')  


ocupacion = 'Jubilado'
if ocupacion == 'Estudiante':
    print('Tienes 50% de descuento')
elif ocupacion == 'Jubilado':
    print('Tienes el 75% de descuento')
else:
    print('Debes pagar el 100%')  


# condicionales con and y or

ocupacion = 'Estudiante'
edad = 19
if ocupacion == 'Estudiante' and edad <= 18:
    print('Tienes 50% de descuento')
elif ocupacion == 'Jubilado' or ocupacion == 'Desempleado':
    print('Tienes el 75% de descuento')
else:
    print('Debes pagar el 100%')  
                    
