from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre
    @abstractmethod
    def CalcularSalarioMensual(self) -> float:
        pass
    def __str__(self):
        return f"Empleado: {self.nombre}"
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_anual: float):
        super().__init__(nombre)
        self.salario_anual = salario_anual
    def CalcularSalarioMensual(self) -> float:
        return self.salario_anual / 12
    def __str__(self):
        return (f"[Tiempo Completo] Nombre: {self.nombre}, "
                f"Salario Anual: {self.salario_anual}, "
                f"Salario Mensual: {self.CalcularSalarioMensual():.2f}")
    
class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre: str, horas_trabajadas: float, tarifa_hora: float):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
    def CalcularSalarioMensual(self) -> float:
        return self.horas_trabajadas * self.tarifa_hora
    def __str__(self):
        return (f"[Tiempo Horario] Nombre: {self.nombre}, "
                f"Horas: {self.horas_trabajadas}, Tarifa: {self.tarifa_hora}, "
                f"Salario Mensual: {self.CalcularSalarioMensual():.2f}")
if __name__ == "__main__":
    empleados = []

    print("=== Registro Empleados a Tiempo Completo ===")
    for i in range(3):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        salario_anual = float(input("Ingrese el salario anual: "))
        empleados.append(EmpleadoTiempoCompleto(nombre, salario_anual))

    print("\n=== Registro Empleados a Tiempo Horario ===")
    for i in range(2):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        horas = float(input("Ingrese las horas trabajadas: "))
        tarifa = float(input("Ingrese la tarifa por hora: "))
        empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))

    print("\n=== Lista de Empleados ===")
    for emp in empleados:
        print(f"{emp.nombre} -> Salario Mensual: {emp.CalcularSalarioMensual():.2f}")
