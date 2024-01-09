from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 100

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        new_cargo = self.cargo + weight
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload(f"cargo overload new cargo = {self.cargo}, max cargo = {self.max_cargo}")

    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo
