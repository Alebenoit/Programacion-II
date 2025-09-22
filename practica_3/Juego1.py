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
            print(f" Record actual: {self.record}")

    def quita_vida(self) -> bool:
        self.numero_de_vidas -= 1
        return self.numero_de_vidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas: int):
        super().__init__(numero_de_vidas)
        self.numero_a_adivinar = None

    def juega(self):
        self.reinicia_partida(self.numero_de_vidas)
        self.numero_a_adivinar = random.randint(0, 10)

        print("Bienvenido al juego Adivina el Número")
        print(f"Tienes {self.numero_de_vidas} vidas.")
        print("Debes adivinar un número entre 0 y 10.")

        while True:
            try:
                intento = int(input("Ingresa tu número:"))
            except ValueError:
                print("Entrada inválida. Ingresa un número entero.")
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

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(5) 
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()





