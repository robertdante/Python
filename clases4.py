class Restaurante:

#Constructor

    def __init__(self, nombre, categoria, precio):           
        self.nombre = nombre               #Atributo con categoria PUBLIC
        self._categoria = categoria        #Atributo con categoria PROTECTED
        self.__precio = precio             #Atributo con categoria PRIVATE

#Métodos

    def mostrar_informacion(self):                  
        print(f'Nombre: {self.nombre}, Categoria: {self._categoria}, Precio: {self.__precio}')

    def get_precio(self):                 #Método Getter
        return self.__precio

    def set_precio(self, precio):         #Método Setter
        self.__precio = precio


#Instancias

restaurante1 = Restaurante('Pizzeria', 'Comida italiana', 50)
precio = restaurante1.get_precio()                              #Utilizar metodo get para visualizar el precio PRIVATE
print(f'El precio del restaurante1 es {precio} euros')
restaurante1.mostrar_informacion()

restaurante2 = Restaurante('Hamburgueseria', 'Fast Food', 30)
restaurante2.set_precio(40)                                     #Utilizar metodo set para modificar el precio PRIVATE
restaurante2.mostrar_informacion()



class Hotel(Restaurante):                               #Subclase Hotel que hereda de la clase Restaurante

    def __init__(self, nombre, categoria, precio):      #Constructor subclase
        super().__init__(nombre, categoria, precio)     #Sintaxis para heredar los atributos de la clase Restaurante

hotel = Hotel('Hotel PTA', '5 Estrellas', 200)
hotel.mostrar_informacion()                             #Utilización del método mostrar_informacion de la clase Restaurante
precio = hotel.get_precio()                             #Utilización del método get de la clase Restaurante
print(f'El precio del Hotel PTA es {precio}')        