from datetime import datetime, timedelta
from time import sleep
import numpy as np

class Drink:

    def __init__(self, volume, percent, name=None, price=None, barcode=None):
        self.volume = volume
        self.percent = percent
        self.name = name
        self.price = price
        self.barcode = barcode

class Person:

    def __init__(self, age, weight, height, sex):
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        self.drinks = []
        self.__metabolize_time__ = 40
        self.__time_window__ = timedelta(1)

    def add_drink(self, drink, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        self.drinks.append({"timestamp": timestamp, "drink": drink})

    def generate_graph_data(self):
        tmp_lst = filter(lambda tup: abs((tup["timestamp"] - datetime.now())) < self.__time_window__, self.drinks)
        tmp_lst = sorted(tmp_lst, key=lambda elem: elem["timestamp"])
        time_minutes = self.__time_window__.total_seconds()/60
        np.zeros(time_minutes*2)
        print(time_minutes)
        return tmp_lst

if __name__ == "__main__":
    person = Person(24, 73, 173, True)
    person.add_drink("Test 1")
    person.add_drink("Test 2")
    person.add_drink("Test 3")
    person.add_drink("Test old", datetime.fromisoformat("2023-10-19"))
    print(person.generate_graph_data())
