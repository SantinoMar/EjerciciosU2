def validar_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print('El valor debe estar entre {} y {}'.format(minimo, maximo))
        except ValueError:
            print('Ingrese un valor entero válido')
