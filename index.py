class animal:
    def __init__(self,nombre,edad,vacunado):
        self.nombre = nombre
        self.edad = edad
        self._vacunado = vacunado
        
        def __str__(self):
            return "[{}, nombre: {}, edad: {} años]".format(type(self).__name__,self.nombre,self.edad)

        def comer(self,alimento):
            print("yo como"+alimento)
        



