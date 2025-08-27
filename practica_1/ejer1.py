class EcuacionLineal:
    def __init__(self, a, b, c, d, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__f = f
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0    
    def getX(self):
        if not self.tieneSolucion():
            raise Exception("El sistema no tiene solución única.")
        return (self.__f * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
    def getY(self):
        if not self.tieneSolucion():
            raise Exception("El sistema no tiene solución única.")
        return (self.__a * self.__f - self.__f * self.__c) / (self.__a * self.__d - self.__b * self.__c)
if __name__ == "__main__":
    ecuacion = EcuacionLineal(2, 3, 4, 5, 10)
    if ecuacion.tieneSolucion():
        print("x =", ecuacion.getX())
        print("y =", ecuacion.getY())
    else:
        print("El sistema no tiene solución única.")
