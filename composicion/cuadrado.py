from coordenadas import Coordenada

class Cuadrado:
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

    def mostrarVertices(self):
        print("el cuadrado esta compuesto por los siguientes vertices:")
        self.v1.mostrarcoordenada()
        self.v2.mostrarcoordenada()
        self.v3.mostrarcoordenada()
        self.v4.mostrarcoordenada()

def main():
    v1 = Coordenada(1, 1)
    v2 = Coordenada(4, 1)
    v3 = Coordenada(4, 4)
    v4 = Coordenada(1, 4)
    cuadrado = Cuadrado(v1, v2, v3, v4)
    cuadrado.mostrarvertices

    if __name__ == main():
        main()