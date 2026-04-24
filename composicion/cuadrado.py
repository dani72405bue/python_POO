from coordenadas import coordenadas

class Cuadrado:
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

    def mostrarVertices(self):
        print("el cuadrado esta compuesto por los siguientes vertices:")
        self.v1.mostrarcoordenadas()
        self.v2.mostrarcoordenadas()
        self.v3.mostrarcoordenadas()
        self.v4.mostrarcoordenadas()

def main():
    v1 = coordenadas(1, 1)
    v2 = coordenadas(4, 1)
    v3 = coordenadas(4, 4)
    v4 = coordenadas(1, 4)
    cuadrado = Cuadrado(v1, v2, v3, v4)
    cuadrado.mostrarvertices

    if __name__ == main():
        main()