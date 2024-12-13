


class Animal:
    _totalAnimales = 0  

    def __init__(self, nombre=None, edad=0, habitat=None, genero=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        Animal._totalAnimales += 1

        @staticmethod
        def totalPorTipo():
            from zooAnimales.mamifero import Mamifero
            from zooAnimales.ave import Ave
            from zooAnimales.reptil import Reptil
            from zooAnimales.pez import Pez
            from zooAnimales.anfibio import Anfibio
            return f"Mamíferos: {Mamifero.getListado().size()}\n"
            f"Aves: {Ave.getListado().size()}\n"
            f"Reptiles: {Reptil.getListado().size()}\n"
            f"Peces: {Pez.getListado().size()}\n"
            f"Anfibios: {Anfibio.getListado().size()}"

        def movimiento(self):
            return "desplazarse";

        def __str__(self):
            if self.__zona is None:
                return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} "
                        f"y mi genero es {self._genero}.")
            else:
                return (f"Mi nombre es {self._nombre}, tengo una edad de {self.__edad}, habito en {self._habitat} "
                        f"y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.get_nombre()}, "
                        f"en el {self._zona.get_zoo().get_nombre()}.")

    @staticmethod
    def getTotalAnimales():
        return Animal._totalAnimales

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def getZona(self):
        return self._zona

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def setGenero(self, genero):
        self._genero = genero

    def setZona(self, zona):
        self._zona = zona

