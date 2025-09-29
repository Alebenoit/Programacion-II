from abc import ABC, abstractmethod
import random
import math
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color: str = "sin color"):
        self.color = color
    def setColor(self, color: str):
        self.color = color
    def getColor(self) -> str:
        return self.color
    def __str__(self):
        return f"Figura de color {self.color}"
    @abstractmethod
    def area(self) -> float:
        pass
    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str = "sin color"):
        super().__init__(color)
        self.lado = lado
    def area(self) -> float:
        return self.lado * self.lado
    def perimetro(self) -> float:
        return 4 * self.lado
    def comoColorear(self) -> str:
        return "Colorear los cuatro lados"
    def __str__(self):
        return (f"Cuadrado de lado {self.lado}, color {self.color}, "
                f"Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}")

class Circulo(Figura):
    def __init__(self, radio: float, color: str = "sin color"):
        super().__init__(color)
        self.radio = radio
    def area(self) -> float:
        return math.pi * self.radio ** 2
    def perimetro(self) -> float:
        return 2 * math.pi * self.radio
    def __str__(self):
        return (f"Círculo de radio {self.radio}, color {self.color}, "
                f"Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}")

if __name__ == "__main__":
    figuras = []
    colores = ["rojo", "azul", "verde", "amarillo", "negro"]

    for _ in range(5):
        tipo = random.randint(1, 2)
        color = random.choice(colores)

        if tipo == 1:
            lado = random.uniform(1, 10)
            figuras.append(Cuadrado(lado, color))
        else:
            radio = random.uniform(1, 10) 
            figuras.append(Circulo(radio, color))
    print("\n=== Figuras Generadas ===")
    for f in figuras:
        print(f)
        print(f"Área: {f.area():.2f}, Perímetro: {f.perimetro():.2f}")
        if isinstance(f, Coloreado):
            print("→", f.comoColorear())
        print("-" * 40)
