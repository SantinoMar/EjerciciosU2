class PlanAhorro:
    def __init__(self, codigo_plan, modelo, version, valor_vehiculo, cant_cuotas, cant_cuotas_licitacion):
        self.codigo_plan = codigo_plan
        self.modelo = modelo
        self.version = version
        self.valor_vehiculo = valor_vehiculo
        self.cant_cuotas = cant_cuotas
        self.cant_cuotas_licitacion = cant_cuotas_licitacion
        
    def actualizar_valor_vehiculo(self, nuevo_valor):
        self.valor_vehiculo = nuevo_valor
        
    def calcular_valor_cuota(self):
        valor_cuota = (self.valor_vehiculo/self.cant_cuotas) + self.valor_vehiculo * 0.10
        return valor_cuota
