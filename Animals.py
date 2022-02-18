class animal:
    def __init__(self,nombre,edad,vacunado):
        self.nombre = nombre
        self.edad = edad
        self._vacunado = vacunado
        
        def __str__(self):
            return "[{}, nombre: {}, edad: {} años]".format(type(self).__name__,self.nombre,self.edad)

        def comer(self,alimento):
            print("yo como"+alimento)
            pass

            def dormir(self):
             print("yo duermo")
             pass 
    
        def jugar(self):
             print("yo juego")
             pass 
    
        def morder(self):
            print ("yo muerdo")
            pass

class Mamifero(animal):
    def caminar(self):
        print("yo camino")    

class Perro(Mamifero):
    def __init__(self, nombre, edad, vacunado, raza, color, tamaño):
        super().__init__(nombre, edad, vacunado)
        self.raza = raza
        self.color = color
        self.tamaño = tamaño



