from datetime import datetime

class Person:

    def __init__(self, age, weight, height, sex):
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        self.drinks = []

    def add_drink(self, drink, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        self.drinks.append({"timestamp": timestamp, "drink": drink})
