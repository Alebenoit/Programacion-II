import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getDiscriminante(self):
        return self.__b ** 2 - 4 * self.__a * self.__c    
    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return None
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)
    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return None
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)
if __name__ == "__main__":
    a, b, c, = map(float, input("Ingrese a, b, c: ").split())
    ecuacion = EcuacionCuadratica(a, b, c)
    disc = ecuacion.getDiscriminante()
    if disc > 0:
        print(f"La ecuacion tiene dos raices {ecuacion.getRaiz1():.6f} y {ecuacion.getRaiz2():.6f}")
    elif disc == 0:
        print(f"La ecuacion tiene una raiz {ecuacion.getRaiz1():.6f}")
    else:
        print("La ecuacion no tiene raices reales")
