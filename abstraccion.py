class Materia:
    def __init__(self, dicc):
        self.nombre = dicc["nombre"]
        self.codigo = dicc["codigo"]
        self.horas = dicc["horas"]

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Horas: {self.horas}")


class Student:
    def __init__(self, dicc):
        self.name = dicc["name"]
        self.codigo = dicc["codigo"]
        self.carnet = dicc["carnet"]
        self.materias = dicc["materias"]

    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Código: {self.codigo}")
        print(f"Carnet: {self.carnet}")
        print("Materias:")
        for materia in self.materias:
            print(f"- {materia.nombre}")


programacion = Materia({
    "nombre": "Programación",
    "codigo": "M1",
    "horas": 80
})
redes = Materia({
    "nombre": "Redes",
    "codigo": "M2",
    "horas": 60
})

ariel = Student({
    "name": "Ariel",
    "codigo": "202110038",
    "carnet": "CT19003",
    "materias": [programacion, redes]
})

pablo = Student({
    "name": "Pablo",
    "codigo": "202110038",
    "carnet": "CT19003",
    "materias": [programacion]
})

ariel.mostrar()
pablo.mostrar()
