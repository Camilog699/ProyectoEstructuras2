import json


class JSON:
    def leer(self, ciudad):
        if self != ciudad:
            pass
        with open(
            "/home/camilogomez/ProyectosVscode/Proyecto/Json/ciudad.json"
        ) as file:
            data = json.load(file)
            for ciud in data["Ciudad"]:
                for barrio in ciud["Barrio"]:
                    if barrio["tanque"] == 0:
                        t = False
                    else:
                        t = True
                    ciudad.agregarBarrio(
                        barrio["id"], barrio["x"], barrio["y"], t, barrio["monton"]
                    )
                for tuberia in ciud["Tuberia"]:
                    ciudad.agregarTuberia(
                        ciudad.buscarBarrio(tuberia["origen"]),
                        ciudad.buscarBarrio(tuberia["destino"]),
                        tuberia["capacidad"],
                    )
        return ciudad
