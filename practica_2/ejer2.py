import math
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, otra):
        return Vector3D(self.x + otra.x, self.y + otra.y, self.z + otra.z)

    def __sub__(self, otra):
        return Vector3D(self.x - otra.x, self.y - otra.y, self.z - otra.z)

    def __mul__(self, otra):
        if isinstance(otra, (int, float)):   # escalar
            return Vector3D(self.x * otra, self.y * otra, self.z * otra)
        elif isinstance(otra, Vector3D):     # producto escalar
            return self.x*otra.x + self.y*otra.y + self.z*otra.z
        
    def __rmul__(self, otra):
        return self.__mul__(otra)

    def __truediv__(self, otra):
        if otra != 0:
            return Vector3D(self.x / otra, self.y / otra, self.z / otra)

    def __xor__(self, otra):
        
        return Vector3D(
            self.y*otra.z - self.z*otra.y,
            self.z*otra.x - self.x*otra.z,
            self.x*otra.y - self.y*otra.x
        )
a = Vector3D(2, 3, 4)
b = Vector3D(1, 0, -1)

print("Vector a:", a)
print("Vector b:", b)
print("a + b =", a + b)
print("a - b =", a - b)
print("3 * a =", 3 * a)
print("a · b =", a * b)       
print("a × b =", a ^ b)      
