class animal(object):
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


class Gato(Mamifero):
    def __init__(self,nombre,edad,vacunado,color,raza):
        super().__init__(nombre, edad, vacunado)
        self.color = color
        self.raza = raza
    
    def __str__(self):
        return super().__str__()[:-1]+", raza: {}, color: {}]".format(self.raza,self.color)
    
    def maullar():
        print("miau")
        
    def comer(self,alimento):
        print ("ñam *estoy comiendo {}*".format(alimento))
    
    def arañar(self,objeto):
        print ("purr ñiau *estoy arañando {}*".format(objeto))

Perro1=Perro("Odie",8,True,"Pastor Aleman","Negro con Naranja","Grande")


Gato1 = Gato("Garfield",6,False,"Naranja","Persa")

Listaanimal=[Perro1,Gato1]
print()

print(Listaanimal)


def ordenaranimal(Listaanimal,criterio,invertido):
    if criterio.lower=="nombre":
        Listaanimal.sort(key=lambda animal:animal.nombre,reverse=invertido)
        return Listaanimal
    
    elif criterio.lower()=="edad":
       Listaanimal.sort(key=lambda animal:animal.edad,reverse=invertido)
       return Listaanimal
    
    elif criterio.lower()=="especie":
       Listaanimal.sort(key=lambda animal:type(animal).__name__,reverse=invertido)
       return Listaanimal
    
    else:
        return Listaanimal
        pass

ListaMascotas=ordenaranimal(ordenaranimal, "nombre",True)
print(ListaMascotas)
print()
ListaMascotas=ordenaranimal(ListaMascotas, "edad",False)
print(ListaMascotas)
print()
ListaMascotas=ordenaranimal(ListaMascotas, "especie",False)
print(ListaMascotas)


        