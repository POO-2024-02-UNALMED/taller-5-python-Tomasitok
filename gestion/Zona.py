
class Zona:
    def __init__(self, nombre=None, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self.__nombre

    def getZoo(self):
        return self.__zoo

    def getAnimales(self):
        return self.__animales

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setZoo(self, zoo):
        self.__zoo = zoo