from viajeroFrecuente import ViajeroFrecuente

## Determinar el/los viajero/s con mayor cantidad de millas acumuladas:

viajero1 = ViajeroFrecuente(1, '12345678', 'John', 'Doe', 5000)
viajero2 = ViajeroFrecuente(2, '87654321', 'Jane', 'Smith', 7000)

if viajero1.__gt__(viajero2) > viajero2:
    print("El viajero 1 tiene más millas acumuladas.")
else:
    print("El viajero 2 tiene más millas acumuladas.")



##Acumular millas usando la sobrecarga del operador binario suma (+):

viajero3 = ViajeroFrecuente(1, '12345678', 'John', 'Doe', 5000)
viajero3.__add__(100)
print(viajero3.cantidadTotalMillas())  # Imprime 5100



##Canjear millas usando la sobrecarga del operador binario resta (-):

viajero4 = ViajeroFrecuente(1, '12345678', 'John', 'Doe', 5000)
viajero4.__sub__(2000)
print(viajero4.cantidadTotalMillas())  # Imprime 3000