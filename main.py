class Person:
    def __init__(self, name):
        self.name = name
        self.car = None

    def buy_car(self, car):
        self.car = car
        car.driver = self
        print(f"{self.name} придбав(ла) автомобіль {car.brand}")

    def drive_car(self):
        if self.car is not None:
            print(f"{self.name} водить автомобіль {self.car.brand}")
        else:
            print(f"{self.name} не має автомобіля")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.driver = None

    def start(self):
        if self.driver is not None:
            print(f"Автомобіль {self.brand} запущено. Водій: {self.driver.name}")
        else:
            print(f"Автомобіль {self.brand} не має водія")