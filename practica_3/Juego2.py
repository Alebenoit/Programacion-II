import random
class Juego:
    def __init__(self, numero_de_vidas: int):
        self.numero_de_vidas = numero_de_vidas
        self.record = 0

    def reinicia_partida(self, vidas: int):
        self.numero_de_vidas = vidas

    def actualiza_record(self, vidas_restantes: int):
        if vidas_restantes > self.record:
            self.record = vidas_restantes
            print(f"¡Nuevo récord! Record actual: {self.record}")

    def quita_vida(self) -> bool:
        self.numero_de_vidas -= 1
        return self.numero_de_vidas > 0
    
class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas: int):
        super().__init__(numero_de_vidas)
        self.numero_a_adivinar = None

    def valida_numero(self, num: int) -> bool:
        return 0 <= num <= 10

    def juega(self):
        self.reinicia_partida(self.numero_de_vidas)
        self.numero_a_adivinar = random.randint(0, 10)

        print("Bienvenido al juego Adivina el Número")
        print(f"Tienes {self.numero_de_vidas} vidas.")
        print("Debes adivinar un número entre 0 y 10.")

        while True:
            try:
                intento = int(input("Ingresa tu número: "))
            except ValueError:
                print("Entrada inválida. Ingresa un número entero.")
                continue

            if not self.valida_numero(intento):
                print("Número fuera de rango. Intenta de nuevo (0 a 10).")
                continue

            if intento == self.numero_a_adivinar:
                print("Acertaste!!")
                self.actualiza_record(self.numero_de_vidas)
                break
            else:
                if self.quita_vida():
                    if intento < self.numero_a_adivinar:
                        print(f"El número a adivinar es MAYOR. Te quedan {self.numero_de_vidas} vidas.")
                    else:
                        print(f"El número a adivinar es MENOR. Te quedan {self.numero_de_vidas} vidas.")
                else:
                    print(f"¡Has perdido! El número era: {self.numero_a_adivinar}")
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def valida_numero(self, num: int) -> bool:
        if 0 <= num <= 10:
            if num % 2 == 0:
                return True
            else:
                print("Error: solo se permiten números PARES entre 0 y 10.")
                return False
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def valida_numero(self, num: int) -> bool:
        if 0 <= num <= 10:
            if num % 2 != 0:
                return True
            else:
                print("Error: solo se permiten números IMPARES entre 0 y 10.")
                return False
        return False

class Aplicacion:
    @staticmethod
    def main():
        juegos = [
            JuegoAdivinaNumero(3),
            JuegoAdivinaPar(3),
            JuegoAdivinaImpar(3)
        ]

        for juego in juegos:
            juego.juega()

if __name__ == "__main__":
    Aplicacion.main()
