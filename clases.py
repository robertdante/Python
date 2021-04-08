class Restaurante:

    def agregar_restaurante(self, nombre):
        self.nombre = nombre                          #Crear atributo

    def mostrar_informacion(self):
        print(f'Nombre restaurante: {self.nombre}')
        


restaurante = Restaurante()                           #Crear objeto "restaurante" / instanciar
restaurante.agregar_restaurante('Pizzeria')           #llamada a metodo
restaurante.mostrar_informacion()                     #llamada a metodo  

restaurante2 = Restaurante()                          #crear objeto "restaurante2" / instanciar   
restaurante2.agregar_restaurante('Hamburgueseria')    #llamada a metodo
restaurante2.mostrar_informacion()                    #llamada a metodo

