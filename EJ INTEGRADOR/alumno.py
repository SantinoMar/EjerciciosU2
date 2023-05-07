class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, anio):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.anio = anio

    def __lt__(self, other):
        if self.anio == other.anio:
            return (self.apellido, self.nombre) < (other.apellido, other.nombre)
        return self.anio < other.anio
