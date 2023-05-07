class ViajeroFrecuente:
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.num_viajero = num_viajero
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.millas_acum = millas_acum

    def cantidadTotalMillas(self):
        return self.millas_acum

    def acumularMillas(self, millas_recorridas):
        self.millas_acum += millas_recorridas
        return self.millas_acum

    def canjearMillas(self, cantidad_millas_canje):
        if cantidad_millas_canje <= self.millas_acum:
            self.millas_acum -= cantidad_millas_canje
            return self.millas_acum
        else:
            print('Error en la operacion "La cantidad de millas a canjear es mayor a las millas acumuladas"')
            return self.millas_acum

    def __gt__(self, other):
        return self.millas_acum > other.millas_acum

    def __add__(self, millas_recorridas):
        self.millas_acum += millas_recorridas
        return self

    def __sub__(self, cantidad_millas_canje):
        if cantidad_millas_canje <= self.millas_acum:
            self.millas_acum -= cantidad_millas_canje
        else:
            print('Error en la operacion "La cantidad de millas a canjear es mayor a las millas acumuladas"')
        return self
    
    def __eq__(self, other):
        if isinstance(other, int):
          return self.millas_acum == other
        else:
            return False
        
    def __radd__(self, other):
        if isinstance(other, int):
            self.millas_acum += other
            return self
        else:
            raise TypeError("Unsupported operand type: {} + ViajeroFrecuente".format(type(other)))
        
    def __rsub__(self, other):
        if isinstance(other, int):
            if other <= self.millas_acum:
                self.millas_acum -= other
            else:
                raise ValueError("La cantidad de millas a canjear es mayor a las millas acumuladas")
            return self
        else:
            raise TypeError("Unsupported operand type: {} - ViajeroFrecuente".format(type(other)))


