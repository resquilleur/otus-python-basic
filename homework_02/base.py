from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 1350
    started: bool = False
    fuel: int = 45
    fuel_consumption: int = 8

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low fuel", self.fuel)

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        fuel = self.fuel - required_fuel
        if fuel >= 0:
            self.fuel = fuel
        else:
            raise NotEnoughFuel("Not enough fuel", self.fuel)
