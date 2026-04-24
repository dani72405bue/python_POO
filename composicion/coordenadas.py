class Coordenada:
    # Metodo constructor
    def __init__(self, X, Y):
        self.__X = X
        self.__Y = Y

    # metodos de acceso
    def getX(self):
        return self.__X
    
    def setX(self, X):
        self.__X = X

    def getY(self):
        return self.__Y

    def setY(self, Y):
        self.__Y = Y
        # metodo para mostrar la coordenda 
    def mostrarcoordenda(self):
        print("(", self.__x,"," ,self.__y,")")