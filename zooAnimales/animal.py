
from gestion.zona import Zona

class Animal:
    _totalAnimales = 0  
    _zona = None

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1

    @staticmethod
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio

        return (f"Mamiferos : {len(Mamifero.getListado())}\n"
                f"Aves : {len(Ave.getListado())}\n"
                f"Reptiles : {len(Reptil.getListado())}\n"
                f"Peces : {len(Pez.getListado())}\n"
                f"Anfibios : {len(Anfibio.getListado())}")

    def movimiento(self):
        return "desplazarse";

    def toString(self):
        if self._zona is None:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} "
                    f"y mi genero es {self._genero}")
        else:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} "
                    f"y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.get_nombre()}, "
                    f"en el {self._zona.get_zoo().get_nombre()}")

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales

    @classmethod
    def getZona(cls):
        return cls._zona
    
    @classmethod
    def setZona(cls, zona):
        cls._zona = zona

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat
    
    def setEdad(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero
