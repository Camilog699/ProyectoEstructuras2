from Estructura.barrio import Barrio
from Estructura.tubo import Tubo


class Ciudad:
    def __init__(self):
        self.barrios = []
        self.tubos = []

    def agregarBarrio(self, dato, x, y, tanque, monton):
        barrio = Barrio(dato, x, y, tanque, monton)
        if barrio in self.barrios:
            return
        self.barrios.append(barrio)
        return barrio

    def agregarTuberia(self, origen, destino, capacidad):
        tubo = Tubo(origen, destino, capacidad)
        tuboAux = Tubo(origen, destino, capacidad)
        if tubo in self.tubos or tuboAux in self.tubos:
            return
        self.tubos.append(tubo)
        origen.adyacentes.append(destino)
        destino.adyacentes.append(origen)

    def buscarBarrio(self, id):
        for barrio in self.barrios:
            if barrio.id == id:
                return barrio
        return None

    def verificarBarrio(self, estructura, nombre):
        for i in estructura:
            if i.id == nombre:
                return True
        return False
