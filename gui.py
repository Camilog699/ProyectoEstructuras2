import pygame
from Vistas.cursor import Cursor
from Vistas.boton import Boton
from pygame.locals import *
from math import tan, atan2, cos, degrees, pi
from pygame import Rect
from time import sleep
from random import randint

pygame.init()


class Gui:
    def __init__(self, ciudad):
        self.clock = pygame.time.Clock()
        self.obs = False
        self.conexion = False
        self.tanqueo = False
        self.cambio = False
        self.aux = []
        self.cursor = Cursor()
        self.ciudad = ciudad
        self.pintar()

    def without_filter(self, n):
        if n.tanque:
            n.resal = False
            return False

        for barrio in self.ciudad.barrios:
            if barrio.tanque == 0:
                barrio.resal = False
                continue

            if n in barrio.adyacentes:
                n.resal = False
                return False

        return True

    def pintar(self):

        pygame.init()
        imagen = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/boton1.png"
        )
        imagen2 = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/boton2.png"
        )
        imagen = pygame.transform.scale(imagen, (130, 60))
        imagen2 = pygame.transform.scale(imagen2, (130, 60))
        boton = Boton(imagen, imagen2, 20, 650)
        boton2 = Boton(imagen, imagen2, 180, 650)
        boton3 = Boton(imagen, imagen2, 340, 650)
        boton4 = Boton(imagen, imagen2, 500, 650)
        boton5 = Boton(imagen, imagen2, 660, 650)
        ventana = pygame.display.set_mode((1350, 700))
        pygame.display.set_caption("Ciudad")
        fuente = pygame.font.SysFont("Comit Sans Ms", 16)
        fuente2 = pygame.font.SysFont("Arial", 14)
        fuente3 = pygame.font.SysFont("Comit Sans Ms", 20)
        color = pygame.Color(20, 30, 50)
        run = True
        cursor = Cursor()
        agregar = fuente2.render("Agregar Barrio", True, (0, 0, 0))
        agregar2 = fuente2.render("Obstrucción", True, (0, 0, 0))
        agregar3 = fuente2.render("Agregar Tubo", True, (0, 0, 0))
        agregar4 = fuente2.render("Agregar Tanque", True, (0, 0, 0))
        agregar5 = fuente2.render("Cambiar Sentido", True, (0, 0, 0))

        obstruccion = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/tuboRoto.png"
        )
        obstruccion = pygame.transform.scale(obstruccion, (60, 30))

        tanque0 = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/Tanque0.png"
        )
        tanque25 = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/Tanque25.png"
        )
        tanque50 = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/Tanque50.png"
        )
        tanque75 = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/Tanque75.png"
        )
        tanque100 = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/Tanque100.png"
        )
        tanqueDerrame = pygame.image.load("/home/camilogomez/ProyectosVscode/Proyecto/Imgs/TanqueDerrame.png")
        tanque0 = pygame.transform.scale(tanque0, (50, 70))
        tanque25 = pygame.transform.scale(tanque25, (50, 70))
        tanque50 = pygame.transform.scale(tanque50, (50, 70))
        tanque75 = pygame.transform.scale(tanque75, (50, 70))
        tanque100 = pygame.transform.scale(tanque100, (50, 70))
        tanqueDerrame = pygame.transform.scale(tanqueDerrame,(50,70))

        barrioImg = pygame.image.load(
            "/home/camilogomez/ProyectosVscode/Proyecto/Imgs/Barrio1.png"
        )
        barrioImg = pygame.transform.scale(barrioImg, (80, 80))

        while run:

            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if cursor.colliderect(boton.rect):
                        boton.agregar(self.ciudad)

                    elif cursor.colliderect(boton2.rect):
                        self.obs = True
                    elif self.obs:
                        for a in range(len(self.ciudad.tubos)):
                            if (
                                self.ciudad.tubos[a].linea.x
                                < pygame.mouse.get_pos()[0]
                                < self.ciudad.tubos[a].linea.right
                                and self.ciudad.tubos[a].linea.y
                                < pygame.mouse.get_pos()[1]
                                < self.ciudad.tubos[a].linea.bottom
                            ):
                                self.ciudad.tubos[a].obs = True
                                break
                        self.obs = False

                    elif cursor.colliderect(boton3.rect):
                        self.conexion = True
                    elif self.conexion:
                        for barrio in self.ciudad.barrios:
                            if (
                                barrio.linea.x
                                < pygame.mouse.get_pos()[0]
                                < barrio.linea.right
                                and barrio.linea.y
                                < pygame.mouse.get_pos()[1]
                                < barrio.linea.bottom
                            ):
                                self.aux.append(barrio)
                                print(len(self.aux))
                                if len(self.aux) == 2:
                                    self.ciudad.agregarTuberia(
                                        self.aux[0], self.aux[1], randint(1, 5)
                                    )
                                    self.aux = []
                                    self.conexion = False
                                break

                    elif cursor.colliderect(boton4.rect):
                        self.tanqueo = True
                    elif self.tanqueo:
                        for barrio in self.ciudad.barrios:
                            if (
                                barrio.linea.x
                                < pygame.mouse.get_pos()[0]
                                < barrio.linea.right
                                and barrio.linea.y
                                < pygame.mouse.get_pos()[1]
                                < barrio.linea.bottom
                            ):
                                barrio.tanque = 1
                                barrio.monton = 300
                            self.tanqueo = False

                    elif cursor.colliderect(boton5.rect):
                        self.cambio = True
                    elif self.cambio:
                        for tubo in self.ciudad.tubos:
                            if (
                                tubo.linea.x
                                < pygame.mouse.get_pos()[0]
                                < tubo.linea.right
                                and tubo.linea.y
                                < pygame.mouse.get_pos()[1]
                                < tubo.linea.bottom
                            ):
                                new = tubo.origen
                                tubo.origen = tubo.destino
                                tubo.destino = new
                                tubo.origen.adyacentes.append(tubo.destino)
                                tubo.destino.adyacentes.remove(tubo.origen)
                                break
                        self.cambio = False

                if evento.type == pygame.QUIT:
                    run = False

            whithoutsin = list(
                filter(lambda b: self.without_filter(b), self.ciudad.barrios)
            )

            for barrio in whithoutsin:
                barrio.resal = True

            ventana.fill((255, 255, 255))
            cursor.update()
            boton.update(ventana, cursor, agregar)
            boton2.update(ventana, cursor, agregar2)
            boton3.update(ventana, cursor, agregar3)
            boton4.update(ventana, cursor, agregar4)
            boton5.update(ventana, cursor, agregar5)

            for tubo in self.ciudad.tubos:
                desx = tubo.destino.x
                orix = tubo.origen.x
                desy = tubo.destino.y
                oriy = tubo.origen.y
                newrec = Rect(orix, oriy, 80, 80)
                otrorec = Rect(desx, desy, 80, 80)

                tubo.linea = pygame.draw.line(
                    ventana,
                    (0, 0, 0),
                    (newrec.centerx, newrec.centery),
                    (otrorec.centerx, otrorec.centery),
                    35,
                )
                tubo.linea = pygame.draw.line(
                    ventana,
                    (255, 255, 255),
                    (newrec.centerx, newrec.centery),
                    (otrorec.centerx, otrorec.centery),
                    30,
                )
                capacidad = fuente3.render(str(tubo.capacidad), True, (0, 0, 0))
                ventana.blit(capacidad, (tubo.linea.centerx, tubo.linea.centery + 10))

                if tubo.obs:
                    ventana.blit(
                        obstruccion, (tubo.linea.centerx + 10, tubo.linea.centery - 10)
                    )
                    continue

                if (
                    not tubo.origen.tanque
                    or tubo.origen.monton < tubo.capacidad
                    or 0 < tubo.destino.capacidad < tubo.destino.monton
                ):
                    tubo.rect = Rect(orix, oriy, 30, 20)
                    continue

                rads = atan2(desy - oriy, desx - orix)
                dirx = 1
                diry = 1
                if desx - orix < 0:
                    dirx = -1
                if desy - oriy < 0:
                    diry = -1

                movex = dirx
                movey = tan(rads) * movex

                if abs(movey) < 1:
                    movey = diry
                    movex = movey / tan(rads)

                sleep(0.0001)

                tubo.rect.x += movex
                tubo.rect.y += movey

                if dirx == -1:
                    if tubo.rect.x < tubo.destino.x:
                        tubo.rect.x = tubo.destino.x
                else:
                    if tubo.rect.x > tubo.destino.x:
                        tubo.rect.x = tubo.destino.x

                if diry == -1:
                    if tubo.rect.y < tubo.destino.y:
                        tubo.rect.y = tubo.destino.y
                else:
                    if tubo.rect.y > tubo.destino.y:
                        tubo.rect.y = tubo.destino.y

                rect1 = tubo.rect
                rect2 = Rect(desx, desy, 100, 41)

                if rect1.colliderect(rect2):
                    tubo.rect = Rect(orix, oriy, 30, 20)
                    tubo.origen.monton -= tubo.capacidad
                    tubo.destino.monton += tubo.capacidad

                    if tubo.destino.monton > tubo.destino.capacidad:
                        tubo.destino.monton = tubo.destino.capacidad

                ventana.blit(tubo.img, tubo.rect)

            for barrio in self.ciudad.barrios:
                if barrio.tanque == 1:
                    holi = None
                    if barrio.selectImg(barrio.monton) == 0:
                        holi = ventana.blit(tanque0, (barrio.x + 50, barrio.y - 20))
                    if barrio.selectImg(barrio.monton) == 1:
                        holi = ventana.blit(tanque25, (barrio.x + 50, barrio.y - 20))
                    if barrio.selectImg(barrio.monton) == 2:
                        holi = ventana.blit(tanque50, (barrio.x + 50, barrio.y - 20))
                    if barrio.selectImg(barrio.monton) == 3:
                        holi = ventana.blit(tanque75, (barrio.x + 50, barrio.y - 20))
                    if barrio.selectImg(barrio.monton) == 4:
                        holi = ventana.blit(tanque100, (barrio.x + 50, barrio.y - 20))
                    if barrio.selectImg(barrio.monton) == 5:
                        holi = ventana.blit(tanqueDerrame, (barrio.x + 50, barrio.y - 20))

                    texto = fuente.render(str(barrio.monton), True, (0, 0, 0))
                    ventana.blit(texto, (holi.centerx, holi.centery))
                if barrio.resal:
                    pygame.draw.circle(
                        ventana, (0, 0, 250), (barrio.x + 100, barrio.y), 3
                    )

                barrio.linea = ventana.blit(barrioImg, (barrio.x, barrio.y))
                texto = fuente.render(barrio.id, True, (0, 0, 0))
                ventana.blit(texto, (barrio.x + 20, barrio.y + 80))
            self.clock.tick(60)
            pygame.display.update()
