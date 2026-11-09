"Ejercico Extra"

class EmpleadoGeneral:

    Etica = "respetar a los compañeros"

    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def fichar(self, hora: str, accion: str):
        print(f"{self.nombre} : {self.id} {accion} registrada a las {hora}")

    def condcuta_obligatoria(self):
        print(f"Como empleado {self.nombre} debe {EmpleadoGeneral.Etica}")

class Trabajador(EmpleadoGeneral):

    def __init__(self, id: int, nombre: str, puesto: str):
        super().__init__(id, nombre)
        self.puesto = puesto

    def trabajar(self):
        print(f"La funcion de {self.nombre} {self.id} es realizar sus labores de {self.puesto}")

class Coordinador(EmpleadoGeneral):

    def __init__(self, id: int, nombre: str, subordinados: list):
        super().__init__(id, nombre)
        self.subordinados = subordinados

    def coordinar(self):
        print(f"La funcion de {self.nombre} {self.id} es coordinar a los trabajadores")

    def personal(self):
        print(f"{self.nombre} {self.id} tiene a su cargo:")
        for empleado in self.subordinados:
            print(empleado.nombre)
            print(empleado.id)

class Director(EmpleadoGeneral):

    def __init__(self, id: int, nombre: str, subordinados: list):
        super().__init__(id, nombre)
        self.subordinados = subordinados

    def dirigir(self):
        print(f"La funcion de {self.nombre} {self.id} es dirigir a los coordinadores")

    def personal(self):
        print(f"{self.nombre} {self.id} tiene a su cargo:")
        for empleado in self.subordinados:
            print(empleado.nombre)
            print(empleado.id)

Empleado1 = Trabajador(1, "Angel", "Ingeniero")
Empleado2 = Trabajador(2, "Ana", "Psicóloga")
Empleado3 = Trabajador(3, "Marina", "Logopeda")
Empleado4 = Trabajador(4, "Josué", "Electricista")


Empleado1.trabajar()
Empleado2.trabajar()
Empleado3.trabajar()
Empleado4.trabajar()

Empleado5 = Coordinador(5, "Juan",[Empleado1, Empleado2])
Empleado6 = Coordinador(6, "Joaquín",[Empleado3, Empleado4])

Empleado5.coordinar()
Empleado5.personal()
Empleado6.coordinar()
Empleado6.personal()

Empleado7 = Director(7,"Luis", [Empleado5, Empleado6])

Empleado7.dirigir()
Empleado7.personal()