from conjunto import Conjunto

def mostrar_menu():
    print("1. Unión de conjuntos")
    print("2. Diferencia de conjuntos")
    print("3. Verificar igualdad de conjuntos")
    print("4. Salir")

def leer_conjunto():
    elementos = input("Ingrese los elementos del conjunto separados por comas: ")
    elementos = [int(elemento) for elemento in elementos.split(",")]
    return Conjunto(elementos)

if __name__ == '__main__':
    conjunto_a = None
    conjunto_b = None

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            conjunto_a = leer_conjunto()
            conjunto_b = leer_conjunto()
            union = conjunto_a.__add__(conjunto_b)
            print("Unión:", union)
        elif opcion == "2":
            conjunto_a = leer_conjunto()
            conjunto_b = leer_conjunto()
            diferencia = conjunto_a.__sub__(conjunto_b)
            print("Diferencia:", diferencia)
        elif opcion == "3":
            conjunto_a = leer_conjunto()
            conjunto_b = leer_conjunto()
            if conjunto_a.__eq__(conjunto_b):
                print("Los conjuntos son iguales")
            else:
                print("Los conjuntos no son iguales")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
