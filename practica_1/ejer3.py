import math
def promedio(datos):
    return sum(datos) / len(datos)
def desviacion(datos):
    n = len(datos)
    prom = promedio(datos)
    suma = sum((x - prom) ** 2 for x in datos)
    return math.sqrt(suma / (n - 1))
if __name__ == "__main__":
    numeros = list(map(float, input("Ingrese 10 numeros separados por espacio: ").split()))
    if len(numeros) != 10:
        print("Debe ingresar exactamente 10 numeros.")
    else:
        prom = promedio(numeros)
        desv = desviacion(numeros)
        print(f"El promedio es {prom:.2f}")
        print(f"La desviacion estandar es {desv:.5f}")
