class Ventana:
    def __init__(self, titulo, x1=0, y1=0, x2=100, y2=100):
        self.titulo = titulo
        self.x1 = max(0, x1) #Vertice superior izquierdo 
        self.y1 = max(0, y1) #Vertice superior izquierdo
        self.x2 = min(500, x2) #Vertice inferior derecho
        self.y2 = min(500, y2) #Vertice inferior derecho

        # Corrección de valores si el usuario ingresó coordenadas invertidas
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1

    def mostrar(self):
        print('Ventana:', self.titulo)
        print('Coordenadas: ({}, {}) - ({}, {})'.format(self.x1, self.y1, self.x2, self.y2))
    
    def ancho(self):
        return self.x2 - self.x1

    def alto(self):
        return self.y2 - self.y1

    def moverDerecha(self, unidades=1):
        self.x1 += unidades
        self.x2 += unidades
        # Verificación de límites
        if self.x2 > 500:
            self.x2 = 500
            self.x1 = self.x2 - self.ancho()

    def moverIzquierda(self, unidades=1):
        self.x1 -= unidades
        self.x2 -= unidades
        # Verificación de límites
        if self.x1 < 0:
            self.x1 = 0
            self.x2 = self.x1 + self.ancho()

    def subir(self, unidades=1):
        self.y1 -= unidades
        self.y2 -= unidades
        # Verificación de límites La razón por la que se restan las unidades a las coordenadas y1 e y2 en el método subir y se suman las unidades en el método bajar es que la dirección positiva del eje y en la pantalla apunta hacia abajo, es decir, los valores más grandes de y corresponden a posiciones más bajas en la pantalla. Por lo tanto, para subir la ventana en la pantalla, se deben restar unidades a las coordenadas y1 e y2 para moverla hacia la parte superior de la pantalla, y para bajarla, se deben sumar unidades a las mismas coordenadas para moverla hacia la parte inferior de la pantalla.
        if self.y1 < 0:
            self.y1 = 0
            self.y2 = self.y1 + self.alto()

    def bajar(self, unidades=1):
        self.y1 += unidades
        self.y2 += unidades
        # Verificación de límites
        if self.y2 > 500:
            self.y2 = 500
            self.y1 = self.y2 - self.alto()

    def getTitulo(self):
        return self.titulo

      
