class Conjunto:
    def __init__(self, elementos=None):
        if elementos is None:
            elementos = []
        self.elementos = elementos

    def __str__(self):
        return "{" + ", ".join(str(elemento) for elemento in self.elementos) + "}"

    def __add__(self, otro_conjunto):
        elementos_union = self.elementos.copy()
        for elemento in otro_conjunto.elementos:
            if elemento not in elementos_union:
                elementos_union.append(elemento)
        return Conjunto(elementos_union)

    def __sub__(self, otro_conjunto):
        elementos_diferencia = [elemento for elemento in self.elementos if elemento not in otro_conjunto.elementos]
        return Conjunto(elementos_diferencia)

    def __eq__(self, otro_conjunto):
        return sorted(self.elementos) == sorted(otro_conjunto.elementos)
