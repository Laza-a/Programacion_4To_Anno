
from turtle import delay


class character:
    def __init__(self, name, resistance, strength):
        self.name = name
        self.resistance = resistance
        self.strength = strength

    def run(self):
        print(f"{self.name} is running.")
        self.resistance -= 1
        print(f"{self.name}'s resistance is now {self.resistance}.")
        delay(1)
    def recover_resistance(self):
        print(f"{self.name} is recovering resistance.")
        self.resistance += 1
        print(f"{self.name}'s resistance is now {self.resistance}.")
        delay(1)
class superhero(character):
    def __init__(self, name, resistance, strength, superpower):
        super().__init__(name, resistance, strength)
        self.superpower = superpower

    def use_superpower(self):
        print(f"{self.name} is using their superpower: {self.superpower}.")
        self.strength += 5
        print(f"{self.name}'s strength is now {self.strength}.")
        delay(1)
class villain(character):
    def __init__(self, name, resistance, strength, evil_plan):
        super().__init__(name, resistance, strength)
        self.evil_plan = evil_plan

    def execute_evil_plan(self):
        print(f"{self.name} is executing their evil plan: {self.evil_plan}.")
        self.strength += 5
        print(f"{self.name}'s strength is now {self.strength}.")
        delay(1)
