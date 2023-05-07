from materia import Materia

class ManejadorMaterias:
    def __init__(self):
        self.materias = []

    def cargar_materias(self, archivo):
        with open(archivo, 'r') as file:
            for line in file:
                dni, nombre, fecha, nota, aprobacion = line.strip().split(',')
                materia = Materia(int(dni), nombre, fecha, float(nota), aprobacion)
                self.materias.append(materia)

    def estudiantes_aprobados_promocion(self, nombre_materia):
        estudiantes = []
        for materia in self.materias:
            if materia.nombre == nombre_materia and materia.aprobacion == 'P' and materia.nota >= 7:
                estudiantes.append(materia)
        return estudiantes
