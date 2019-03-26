from Estructura.ciudad import Ciudad
from gui import Gui
from random import randint
from Json.json import JSON


def main():
    ciudad = Ciudad()
    json = JSON()
    ciudad = json.leer(ciudad)
    Gui(ciudad)


main()
