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
    def __str__(self):
        return super().__str__()[:-1]+", raza: {}, color: {}, tamaño: {}]".format(self.raza,self.color, self.tamaño)
    
    def ladrar(self):
        print("guau")

        
    def comer(self,alimento):
        print("woof guau *estoy comiendo {}*".format(alimento))
        
    def cuidar(self,objeto):
        print("woof *estoy vigilando {}*".format(objeto))

