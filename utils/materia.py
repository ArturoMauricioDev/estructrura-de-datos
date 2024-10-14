class Materia:

    def __init__(self, dicc):
        self.__nombre = dicc["nombre"]
        self.codigo = dicc["codigo"]
        self.horas = dicc["horas"]
        self.estudiantes = dicc["estudiantes"]

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Código: {self.codigo}")
        print(f"Horas: {self.horas}")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.name}")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
