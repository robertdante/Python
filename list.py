lenguajes = ['Python', 'kotlin', 'Java', 'JavaScript']

print(lenguajes)    #Todos los lenguajes
print(lenguajes[3]) #JavaScript

aprendiendo = f'Estoy aprendiendo {lenguajes[0]}'
print(aprendiendo)

#Modificar un elemento por otro en la list
lenguajes[1] = 'HTML'
print(lenguajes)

#Agregar elementos a una list
lenguajes.append('Ruby')
print(lenguajes)

#Eliminar un elemento de una list
del lenguajes[3]
print(lenguajes)

#Eliminar el último elemento de una list
lenguajes.pop()
print(lenguajes)

#Eliminar por nombre
lenguajes.remove('Java')
print(lenguajes)

