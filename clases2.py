class Restaurante:

#Constructor

    def __init__(self, nombre, categoria):           
        self.nombre = nombre
        self.categoria = categoria

#Método

    def mostrar_informacion(self):                  
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}')

#Instancias

restaurante1 = Restaurante('Pizzeria', 'Comida italiana')
restaurante1.mostrar_informacion()

restaurante2 = Restaurante('Hamburgueseria', 'Fast Food')
restaurante2.mostrar_informacion()