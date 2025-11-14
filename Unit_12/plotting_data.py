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

def data_to_dict(path: str, raw_data = False):
    with open(path, 'r') as f:
        dataset = []
        data = f.readlines()
        for raw in data:
            dataset.append(raw.strip())


        keys = ["Date", "Dew", "Pressure", "Bulb", "Wind", "Precip", "Humid", "AvgTemp", "maxTemp", "minTemp"]
        sorted_data = {k: [] for k in keys}
        for i, data in enumerate(dataset[1:]):
            data = data.split(",") 

            if raw_data:
                for idx, slice in enumerate(data):
                    sorted_data[keys[idx]].append(slice)
                continue

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

rawdata = data_to_dict("Unit_12/WeatherDataCLL.csv", True)
dataset = data_to_dict("Unit_12/WeatherDataCLL.csv")

def plot1():
    fig, ax1 = plt.subplots()

    line1, = ax1.plot(dataset["Date"], dataset["Bulb"], "r", label='Avg Wet Bulb Temp', zorder=1)
    ax1.set_ylabel("Average Wet Bulb Temperature, F")
    ax1.set_xlabel("date")

    ax2 = ax1.twinx()
    line2, = ax2.plot(dataset["Date"], dataset["Pressure"], "b", label='Avg Pressure', zorder=1)
    ax2.set_ylabel("Average Pressure, in Hg")

    lines = [line1, line2]
    labels = [line1.get_label(), line2.get_label()]
    ax2.legend(lines, labels, loc='lower left')

    plt.title("Average Wet Bulb Temperature and Average Pressure")
    plt.figure()

def plot2():
    plt.hist(dataset["Wind"], bins=30, range=(0, 20), color='g', edgecolor='black')
    plt.title("Histogram of Average Wind Speed")
    plt.xlabel("Average Wind Speed, mph")
    plt.ylabel("Number of days")
    plt.figure()

def plot3():
    plt.scatter(dataset["Dew"], dataset["Humid"], sizes=[10], color="black")
    plt.title("Average Relative Humidity vs Average Dew Point")
    plt.xlabel("Average Dew Point (F)")
    plt.ylabel("Average Relative Humidity (%)")

def plot4():
    def get_month_num(date: str):
        return int(date.split('/')[0])

    def get_count(data: list, x: list, find = "avg"):
        months = x
        count = np.zeros(len(x))
        if find == 'min': count = [float('inf') for c in count]

        amounts = np.zeros(12)
        for idx, val in enumerate(rawdata["Date"]):
            for i in range(len(months)):
                if get_month_num(val) == months[i]:

                    value = data[idx]
                    
                    if find == "avg":     
                        if not np.isnan(value):
                            count[i] += value
                            amounts[i] += 1

                    if find == "min":
                        if not np.isnan(value):
                            if value < count[i]: count[i] = value
                    
                    if find == "max":
                        if not np.isnan(value):
                            if value > count[i]: count[i] = value
                    
                    if find == 'sum':
                        if not np.isnan(value):
                            count[i] += value
                    
        if find == "avg":    
            for i in range(len(months)):
               count[i] /= amounts[i]

        return count

    fig, ax = plt.subplots()

    x = np.arange(1, 13)

    avg_temp = get_count(dataset["AvgTemp"], x, 'avg')
    max_temp = get_count(dataset["maxTemp"], x, 'max')
    min_temp = get_count(dataset["minTemp"], x, "min")
    precip = get_count(dataset["Precip"], x, 'sum')
    for i in range(len(precip)):
        precip[i] /= 9

    plt.bar(x, avg_temp, color="#C4B405")
    plt.plot(x, max_temp, color="red", label="High T")
    plt.plot(x, min_temp, color="blue", label="Low T")
    plt.plot(x, precip, color="#03CFC1", label="Precip")
    plt.legend(loc="upper left")
    plt.ylabel("Average Temperature, F\nMonthly Precipitation, in")
    plt.xlabel("Month")
    plt.xticks(x)
    plt.title("Temperature and Precipitation by Month")

def main():
    plot1()
    plot2()
    plot3()
    plot4()
    plt.show()

if __name__ == "__main__":
    main()