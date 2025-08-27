class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f    
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0
    def getX(self):
        if not self.tieneSolucion():
            raise Exception("La ecuación no tiene solución.")
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
    def getY(self):
        if not self.tieneSolucion():
            raise Exception("La ecuación no tiene solución.")
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
if __name__ == "__main__":
    a, b, c, d, e, f = map(float, input("Ingrese a, b, c, d, e, f: ").split())
    ecuacion = EcuacionLineal(a, b, c, d, e, f)
    if ecuacion.tieneSolucion():
        print(f"x = {ecuacion.getX()}, y = {ecuacion.getY()}")
    else:
        print("La ecuacion no tiene solucion")
