from plan_ahorro import PlanAhorro

def leer_datos():
    lista_planes = []
    with open("planes.csv", "r+") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.strip().split(";")
            codigo_plan = datos[0]
            modelo = datos[1]
            version = datos[2]
            valor_vehiculo = float(datos[3])
            cant_cuotas = int(datos[4])
            cant_cuotas_licitacion = int(datos[5])
            plan = PlanAhorro(codigo_plan, modelo, version, valor_vehiculo, cant_cuotas, cant_cuotas_licitacion)
            lista_planes.append(plan)
    return lista_planes
