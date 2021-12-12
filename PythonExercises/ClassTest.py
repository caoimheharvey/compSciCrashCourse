class Vehicle:
    def __init__(self, brand, wheels, doors, convertible):
        self.brand = brand
        self.wheels = wheels
        self.doors = doors
        self.isConvertible = convertible

    def introduce(self):
        print(f"Hello, I am a vehicle, my brand is {self.brand} and I have {self.wheels} wheels")


class Motorbike(Vehicle):
    def __init__(self, brand, wheels, doors, convertible, vtype):
        self.vtype = vtype
        super().__init__(brand, wheels, doors, convertible)

    def introduce(self):
        print(f"Hello, I am a {self.vtype}, my brand is {self.brand} and I have {self.wheels} wheels")

def main():
    v1 = Vehicle("Ford", 4, 3, True)
    v1.introduce()

    v2 = Motorbike("HD", 2, 0, False, "Motor Bike")
    v2.introduce()

    v2.brand = "Honda"
    v2.introduce()

main()