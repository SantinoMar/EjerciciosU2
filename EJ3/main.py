import numpy as np
import os
from registro import Registro
from manipulacion_archivos import leer_archivo

registros = leer_archivo("datos.txt")

def menu():
    print("1. Mostrar máximos y mínimos")
    print("2. Temperatura promedio mensual por hora")
    print("3. Listar valores de variables para un día")
    print("4. Salir")

if __name__ == '__main__':
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        temp_max = np.max([np.max([registro.temperatura for registro in registro_dia if registro is not None]) for registro_dia in registros])
        temp_min = np.min([np.min([registro.temperatura for registro in registro_dia if registro is not None]) for registro_dia in registros])
        hum_max = np.max([np.max([registro.humedad for registro in registro_dia if registro is not None]) for registro_dia in registros])
        hum_min = np.min([np.min([registro.humedad for registro in registro_dia if registro is not None]) for registro_dia in registros])
        pres_max = np.max([np.max([registro.presion for registro in registro_dia if registro is not None]) for registro_dia in registros])
        pres_min = np.min([np.min([registro.presion for registro in registro_dia if registro is not None]) for registro_dia in registros])
        print(f"Temperatura máxima: {temp_max}")
        print(f"Temperatura mínima: {temp_min}")
        print(f"Humedad máxima: {hum_max}")
        print(f"Humedad mínima: {hum_min}")
        print(f"Presión máxima: {pres_max}")
        print(f"Presión mínima: {pres_min}")
    elif opcion == "2":
        for hora in range(24):
            temperatura_promedio = np.mean([registro.temperatura for registro in registros if registro[hora] is not None])
            print(f"Hora {hora}: {temperatura_promedio}")
    elif opcion == "3":
        dia = int(input("Ingrese el número de día: ")) - 1
        print("Hora\tTemperatura\tHumedad\tPresión")
        for hora, registro in enumerate(registros[dia]):
            if registro is not None:
                temperatura = registro.temperatura
                humedad = registro.humedad
                presion = registro.presion
                print(f"{hora}\t{temperatura}\t{humedad}\t{presion}")
    elif opcion == "4":
        print("Terminado")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
