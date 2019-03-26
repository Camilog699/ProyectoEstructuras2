class Barrio:
    def selectImg(self, monton):
        imagen = 4
        if monton < 75:
            imagen = 0
        elif monton < 150:
            imagen = 1
        elif monton < 225:
            imagen = 2
        elif monton < 300:
            imagen = 3

        return imagen

    def __init__(self, id, x, y, tanque, monton):
        self.adyacentes = []
        self.tanque = tanque
        self.id = id
        self.x = x
        self.y = y
        self.monton = monton
        self.linea = None
        self.selectImg(monton)
        self.capacidad = 300
