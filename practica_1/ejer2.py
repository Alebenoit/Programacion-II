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
            return 0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)
    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)
if __name__ == "__main__":
    a, b, c = map(float, input("Ingrese a, b y c: ").split())
    ecuacion = EcuacionCuadratica(a, b, c)

    disc = ecuacion.getDiscriminante()
    if disc < 0:
        print("La ecuacion no tiene soluciones reales.")
    elif disc == 0:
        print(f"La ecuacion tiene una unica raiz: x = {ecuacion.getRaiz1()}")
    else:
        print(f"Raiz 1 = {ecuacion.getRaiz1()}, Raiz 2 = {ecuacion.getRaiz2()}")
