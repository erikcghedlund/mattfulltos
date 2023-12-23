#!/bin/env python3

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

from person import Person, Drink

if __name__ == "__main__":
    #person = Person(24, 73, 173, True)
    #person.add_drink(Drink(500, 10.2, "Test 1"), datetime.now()-timedelta(hours=3))
    #person.add_drink(Drink(500, 10.2, "Test 2"), datetime.now()-timedelta(hours=2))
    #person.add_drink(Drink(500, 10.2, "Test 3"), datetime.now()-timedelta(hours=1))
    #person.add_drink(Drink(500, 10.2, "Test 4"))
    #person.add_drink(Drink(30, 5.2, "Test old"), datetime.fromisoformat("2023-10-19"))
    person = Person.load_person("profile.json")
    data = person.generate_graph_data()
    data = list(filter(lambda x: x != 0, data))
    x = range(len(data))
    y = savgol_filter(data, 21, 3)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
    person.save_person("profile.json")
