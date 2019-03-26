from pygame import Rect
import pygame


class Tubo:
    def __init__(self, origen, destino, capacidad):
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.obs = False
        self.rect = Rect(origen.x, origen.y, 60, 40)
        self.linea = None
        self.img = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/bolita.png"
        )
        self.img = pygame.transform.scale(self.img, (30, 20))
