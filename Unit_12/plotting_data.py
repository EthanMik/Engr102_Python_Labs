# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

import matplotlib.pyplot as plt
import numpy as np

def data_to_dict(path: str):
    with open(path, 'r') as f:
        dataset = []
        data = f.readlines()
        for raw in data:
            dataset.append(raw.strip())


        keys = ["Date", "Dew", "Pressure", "Bulb", "Wind", "Precip", "Humid", "AvgTemp", "maxTemp", "minTemp"]
        sorted_data = {k: [] for k in keys}
        for i, data in enumerate(dataset[1:]):
            data = data.split(",")
            data[0] = i + 1

            cleaned = []
            for v in data:
                if v == "": cleaned.append(np.nan)
                else:
                    try: cleaned.append(float(v))
                    except ValueError: cleaned.append(v)

            for idx, slice in enumerate(cleaned):
                sorted_data[keys[idx]].append(slice)

    return sorted_data


dataset = data_to_dict("Unit_12/WeatherDataCLL.csv")

def plot1():
    fig, ax1 = plt.subplots()

    line1, = ax1.plot(dataset["Date"], dataset["Bulb"], "r", label='Avg Wet Bulb Temp')
    ax1.set_ylabel("Average Wet Bulb Temperature, F")
    ax1.set_xlabel("date")

    ax2 = ax1.twinx()
    line2, = ax2.plot(dataset["Date"], dataset["Pressure"], "b", label='Avg Pressure')
    ax2.set_ylabel("Average Pressure, in Hg")

    lines = [line1, line2]
    labels = [line1.get_label(), line2.get_label()]
    l = ax1.legend(lines, labels, loc="best", zorder=10)
    l.set_zorder(2.5)

    plt.title("Average Wet Bulb Temperature and Average Pressure")

    plt.show()


plot1()