# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def month_to_int(month: str) -> int:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months.index(month) + 1

def data_to_float(dataset: list):
    new_dataset = []
    for data in dataset:
        try:
            new_dataset.append(float(data))
        except ValueError:
            pass
    return new_dataset

def pull_data_slice(path: str, data_index: int):
    data = []
    with open(path, "r") as f:
        for line in f:

            data.append(line.strip().split(",")[data_index])
    return data

def pull_data_month_year(path: str, month: str, year: int) -> list:
    date = str(month_to_int(month)) + str(year)

    def convert_date_int(date: str):
        date = line.strip().split(",")[0]
        date = date.split("/")
        if len(date) < 3: return None

        del date[1]
        return "".join(date)

    dataset = []
    with open(path, "r") as f:
        for line in f:
            _date = convert_date_int(line)
            if _date == date:
                dataset.append(line.strip())

    return dataset

def data_to_dict(dataset: list[str]):
    keys = ["Date", "Dew", "Pressure", "Bulb", "Wind", "Precip", "Humid", "AvgTemp", "maxTemp", "minTemp"]
    sorted_data = {k: [] for k in keys}
    for data in dataset:
        data = data.split(",")
        for idx, slice in enumerate(data):
            sorted_data[keys[idx]].append(slice)

    return sorted_data

def mean(list: list[int]):
    try:
        list = [float(v) for v in list]
        return sum(list) / len(list)
    except ValueError: 
        return None 

def percent(list: list[int]):
    try:
        list = [float(v) for v in list]
        above_zero = [val for val in list if val > 0]
        return len(above_zero) / len(list)
    except ValueError: 
        return None 

csv = "WeatherDataCLL.csv"

max_temps = pull_data_slice(csv, 8)
min_temps = pull_data_slice(csv, 9)

print(f"10-year maximum temperature: {max(data_to_float(max_temps)):.0f} F")
print(f"10-year minimum temperature: {min(data_to_float(min_temps)):.0f} F")

month = input("Please enter a month: ")
year = input ("Please enter a year: ")

# month = "July"
# year = 2024

data = pull_data_month_year(csv, month, year)
dataset = data_to_dict(data)

print(f"For {month} {year}:")
print(f"Mean average daily pressure: {mean(dataset['Pressure']):.2f} in Hg")
print(f"Mean average daily temperature: {mean(dataset['AvgTemp']):.1f} F")
print(f"Mean average daily wet bulb temperature: {mean(dataset['Bulb']):.1f} F")
print(f"Mean average daily dew point: {mean(dataset['Dew']):.1f} F")
print(f"Mean average daily relative humidity: {mean(dataset['Humid']):.1f}%")
print(f"Mean average daily wind speed: {mean(dataset['Wind']):.2f} mph")
print(f"Percentage of days with precipitation: {percent(dataset['Precip']) * 100:.1f}%")