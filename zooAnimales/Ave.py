from Animal import Animal

class Ave(Animal):
    alcones = 0
    aguilas = 0
    _listado = []

    def __init__(self):
        Ave._listado.append(self)

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def cantidadAves():
        return len(Ave._listado)
    
    def movimiento():
        return "volar"
    
    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montañas", genero, "café glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
    
    @staticmethod
    def getListado():
        return Ave.listado

    @staticmethod
    def setListado(nuevoListado):
        Ave.listado = nuevoListado

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    