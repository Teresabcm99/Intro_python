import array


class registro:
    alumnos = []
    asignaturas = {}

    def anadirAlumno(self, nombre:str):
        return self.alumnos.append(nombre)
    def getListAlumno(self) -> array:
        self.alumnos

class asignatura:
    nombre = ""
    nota = 0

    def setnombre(self, nombre:str):
        self.nombre = nombre
    