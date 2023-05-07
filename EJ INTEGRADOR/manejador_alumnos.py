import numpy as np
from alumno import Alumno

class ManejadorAlumnos:
    def __init__(self):
        self.alumnos = np.array([], dtype=Alumno)

    def cargar_alumnos(self, archivo):
        with open(archivo, 'r') as file:
            for line in file:
                dni, apellido, nombre, carrera, anio = line.strip().split(',')
                alumno = Alumno(int(dni), apellido, nombre, carrera, int(anio))
                self.alumnos = np.append(self.alumnos, alumno)

    def calcular_promedio(self, dni, manejador_materias):
        notas = []
        for alumno in self.alumnos:
            if alumno.dni == dni:
                for materia in manejador_materias.materias:
                    if materia.dni == dni:
                        notas.append(materia.nota)
                break
        if len(notas) > 0:
            promedio_con_aplazos = np.mean(notas)
            promedio_sin_aplazos = np.mean([nota for nota in notas if nota >= 4])
            return promedio_con_aplazos, promedio_sin_aplazos
        return None, None
