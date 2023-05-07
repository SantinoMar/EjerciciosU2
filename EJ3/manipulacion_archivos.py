import numpy as np
from registro import Registro
import os

def leer_archivo(nombre_archivo):
    datos = np.genfromtxt(nombre_archivo, delimiter=',')
    num_dias = int(max(datos[:,0]))
    registros = [[None]*24 for _ in range(num_dias)]
    for fila in datos:
        dia = int(fila[0]-1)
        hora = int(fila[1])
        temperatura = fila[2]
        humedad = fila[3]
        presion = fila[4]
        if registros[dia][hora] is None:
            registros[dia][hora] = Registro(temperatura, humedad, presion)
    return registros

def escribir_archivo(nombre_archivo, registros):
    with open(nombre_archivo, 'w') as f:
        for dia, registro_dia in enumerate(registros):
            for hora, registro_hora in enumerate(registro_dia):
                if registro_hora is not None:
                    temperatura = registro_hora.temperatura
                    humedad = registro_hora.humedad
                    presion = registro_hora.presion
                    f.write(f"{dia+1},{hora},{temperatura},{humedad},{presion}\n")
