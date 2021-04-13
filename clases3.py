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
print(precio)
restaurante1.mostrar_informacion()

restaurante2 = Restaurante('Hamburgueseria', 'Fast Food', 30)
restaurante2.set_precio(40)                                     #Utilizar metodo set para modificar el precio PRIVATE
restaurante2.mostrar_informacion()