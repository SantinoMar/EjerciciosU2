from plan_ahorro import PlanAhorro
from lectura_datos import leer_datos


def mostrar_menu():
    print("----- MENÚ DE OPCIONES -----")
    print("1. Actualizar valor del vehículo")
    print("2. Mostrar planes cuya cuota sea inferior a un valor dado")
    print("3. Mostrar monto que se debe haber pagado para licitar el vehículo")
    print("4. Modificar cantidad de cuotas para licitar")
    print("5. Salir")

def actualizar_valor_vehiculo(lista_planes):
    for plan in lista_planes:
        print(f"Codigo plan: {plan.codigo_plan}")
        print(f"Modelo: {plan.modelo}")
        print(f"Version: {plan.version}")
        nuevo_valor = float(input("Ingrese el nuevo valor del vehículo: "))
        plan.actualizar_valor_vehiculo(nuevo_valor)
        print("Valor del vehículo actualizado correctamente.")
    
    
def mostrar_planes_cuota_inferior(lista_planes):
    valor_cuota = float(input("Ingrese el valor máximo de la cuota: "))
    print("Planes con cuota inferior a", valor_cuota, ":")
    for plan in lista_planes:
        if plan.calcular_valor_cuota() < valor_cuota:
            print("Código de plan:", plan.codigo_plan, "- Modelo:", plan.modelo, "- Versión:", plan.version)

def mostrar_monto_cuotas_licitacion(lista_planes):
    codigo_plan = input("Ingrese el código del plan: ")
    encontrado = False
    for plan in lista_planes:
        if plan.codigo_plan == codigo_plan:
            encontrado = True
            monto_cuotas_licitacion = plan.cant_cuotas_licitacion * plan.calcular_valor_cuota()
            print("Monto que se debe haber pagado para licitar:", monto_cuotas_licitacion)
            break
    if not encontrado:
        print("No se encontró un plan con el código ingresado.")

def modificar_cuotas_licitacion(lista_planes):
    codigo_plan = input("Ingrese el código del plan: ")
    encontrado = False
    for plan in lista_planes:
        if plan.codigo_plan == codigo_plan:
            encontrado = True
            nueva_cant_cuotas_licitacion = int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
            plan.cant_cuotas_licitacion = nueva_cant_cuotas_licitacion
            print("Cantidad de cuotas para licitar actualizada correctamente.")
            break
    if not encontrado:
        print("No se encontró un plan con el código ingresado.")

if __name__ == '__main__':
    lista_planes = leer_datos()
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            actualizar_valor_vehiculo(lista_planes)
        elif opcion == "2":
            mostrar_planes_cuota_inferior(lista_planes)
        elif opcion == "3":
            mostrar_monto_cuotas_licitacion(lista_planes)
        elif opcion == "4":
            modificar_cuotas_licitacion(lista_planes)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
