" Creación de mi primera Clase"

class Coche:
    def __init__(self, marca:str, color: str) -> None:
        self.marca = marca
        self.color = color

    def imprimir_color(self):
        print(f"El color del coche es {self.color}")

    def imprimir_marca(self):
        print(f"La marca del coche es {self.marca}")

    def confirmar_datos(self, color, marca):
        if self.color == color and self.marca == marca:
            print("Datos Correctos")
        else:
            print("Datos Incorrectos")

mi_coche = Coche("Toyota", "Blanco")
mi_coche.imprimir_color()
mi_coche.marca = "Seat"
mi_coche.imprimir_marca()
mi_coche.confirmar_datos("Blanco", "Toyota")
