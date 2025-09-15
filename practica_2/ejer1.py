import math

class AlgebraVectorial:
    def __init__(self, vectorA=None, vectorB=None):
        if vectorA is None and vectorB is None:
            self.vectorA = [0, 0, 0]
            self.vectorB = [0, 0, 0]
        elif vectorB is None:
            self.vectorA = vectorA
            self.vectorB = [0, 0, 0]
        else:
            self.vectorA = vectorA
            self.vectorB = vectorB

    def modulo(self, v):
        return math.sqrt(sum([x**2 for x in v]))

    def producto_punto(self, a, b):
        return sum([a[i] * b[i] for i in range(len(a))])

    def producto_cruz(self, a, b):
        return [
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

    def perpendicular(self, tipo=1):
        a, b = self.vectorA, self.vectorB
        if tipo == 1:  # |a+b| = |a-b|
            return math.isclose(self.modulo([a[i]+b[i] for i in range(len(a))]),
                                self.modulo([a[i]-b[i] for i in range(len(a))]))
        elif tipo == 2:  # |a-b| = |b-a|
            return math.isclose(self.modulo([a[i]-b[i] for i in range(len(a))]),
                                self.modulo([b[i]-a[i] for i in range(len(a))]))
        elif tipo == 3:  # a · b = 0
            return math.isclose(self.producto_punto(a, b), 0.0)
        elif tipo == 4:  # |a+b|^2 = |a|^2 + |b|^2
            return math.isclose(self.modulo([a[i]+b[i] for i in range(len(a))])**2,
                                self.modulo(a)**2 + self.modulo(b)**2)

    def paralelo(self, tipo=1):
        a, b = self.vectorA, self.vectorB
        if tipo == 1:
            try:
                r = a[0] / b[0]
                return all(math.isclose(a[i], r*b[i]) for i in range(len(a)))
            except 10 / 0:
                return False
        elif tipo == 2: 
            return self.producto_cruz(a, b) == [0, 0, 0]

    def proyeccion(self):
        a, b = self.vectorA, self.vectorB
        escalar = self.producto_punto(a, b) / (self.modulo(b)**2)
        return [escalar * bi for bi in b]

    def componente(self):
        a, b = self.vectorA, self.vectorB
        return self.producto_punto(a, b) / self.modulo(b)


v1 = [2, 3, 4]
v2 = [4, 6, 8]
algebra= AlgebraVectorial(v1, v2)

print("Perpendiculares:", algebra.perpendicular(3))
print("Paralelos:", algebra.paralelo(2))
print("Proyección:", algebra.proyeccion())
print("Componente:", algebra.componente())
