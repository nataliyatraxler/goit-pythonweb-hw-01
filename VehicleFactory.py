from abc import ABC, abstractmethod

# Абстрактний базовий клас для транспортних засобів
class Vehicle(ABC):
    def __init__(self, make, model, region_spec):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self):
        pass

# Класи для конкретних транспортних засобів
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region_spec} Spec): Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region_spec} Spec): Мотор заведено")

# Абстрактна фабрика
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")

# Фабрика для Європи
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")

# Фабрика для Азії
class AsiaVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "Asia")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "Asia")

# Використання фабрик
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()
asia_factory = AsiaVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()  # Ford Mustang (US Spec): Двигун запущено

vehicle2 = eu_factory.create_motorcycle("BMW", "R1250")
vehicle2.start_engine()  # BMW R1250 (EU Spec): Мотор заведено

vehicle3 = asia_factory.create_car("Toyota", "Camry")
vehicle3.start_engine()  # Toyota Camry (Asia Spec): Двигун запущено
