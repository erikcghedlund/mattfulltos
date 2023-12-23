from datetime import datetime, timedelta
import json
from boozelib import get_blood_alcohol_content as get_alc_content, get_blood_alcohol_degradation as get_alc_degrad
import numpy as np

class Drink:

    def __init__(self, volume, percent, name=None, price=None, barcode=None):
        self.volume = volume
        self.percent = percent
        self.name = name
        self.price = price
        self.barcode = barcode

    def __repr__(self):
        return "drink({}, {}, {}, {}, {})".format(self.volume, self.percent, self.name, self.price, self.barcode)

    def __dict__(self):
        return {
                "volume": self.volume,
                "percent": self.percent,
                "name": self.name,
                "price": self.price,
                "barcode": self.barcode
                }

    @classmethod
    def fromdict(self, dictionary):
        return Drink(dictionary["volume"], dictionary["percent"], dictionary["name"], dictionary["price"], dictionary["barcode"])

class Person:

    def __init__(self, age, weight, height, sex):
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        self.degradation = get_alc_degrad(age=age, weight=weight, height=height, sex=sex)
        self.drinks = []
        self.__metabolize_time__ = 40
        self.__time_window__ = timedelta(1)

    def add_drink(self, drink, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        self.drinks.append({"timestamp": timestamp, "drink": drink})

    def generate_graph_data(self):

        now = datetime.now()

        def add_drink_to_data(tup, data):
            drink_time = tup["timestamp"]
            drink = tup["drink"]
            peak = get_alc_content(age=self.age, weight=self.weight, height=self.height, sex=self.sex, volume=drink.volume, percent=drink.percent)
            start_index = abs(round((drink_time - now).total_seconds()/60))
            add_curve = np.append(np.zeros(start_index), np.append(np.linspace(0, peak, self.__metabolize_time__), np.full((len(data)-self.__metabolize_time__-start_index), peak)))
            return np.add(data, add_curve)

        def apply_degradation(data):
            for i in range(len(data)):
                if data[i] <= 0:
                    factor = 1
                    continue
                else:
                    data[i] -= self.degradation*factor
                    factor += 1
            return data

        def zero_negative_data(data):
            return [max(0, d) for d in data]

        tmp_lst = filter(lambda tup: abs((tup["timestamp"] - now)) < self.__time_window__, self.drinks)
        tmp_lst = sorted(tmp_lst, key=lambda elem: elem["timestamp"])
        time_minutes = round(self.__time_window__.total_seconds()/60)
        data = np.zeros(time_minutes*2)
        for tup in tmp_lst:
            data = add_drink_to_data(tup, data)
        data = apply_degradation(data)
        data = zero_negative_data(data)
        return data

    def __dict__(self):
        return {
                "age": self.age,
                "weight": self.weight,
                "height": self.height,
                "sex": self.sex,
                "drinks": [{"timestamp": mapping["timestamp"].timestamp(), "drink":mapping["drink"].__dict__()} for mapping in self.drinks]
                }

    def save_person(self, file):
        dic = self.__dict__()
        dump_str = json.dumps(dic, sort_keys=False, indent=4)
        with open(file, "w") as f:
            f.write(dump_str)

    @classmethod
    def load_person(self, file):
        with open(file, "r") as f:
            j_obj = json.loads(f.read())
        print(j_obj)
        person = Person(j_obj["age"], j_obj["weight"], j_obj["height"], j_obj["sex"])
        person.drinks = [{"timestamp": datetime.fromtimestamp(entry["timestamp"]), "drink":Drink.fromdict(entry["drink"])} for entry in j_obj["drinks"]]
        return person
