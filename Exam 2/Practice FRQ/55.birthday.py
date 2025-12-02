dict = {
    "January":[],
    "Febuary":[],
    "March":[],
    "April":[],
    "May":[],
    "June":[],
    "July":[],
    "August":[],
    "September":[],
    "October":[],
    "November":[],
    "December":[],
}

for i in range(5):
    bday = input("Enter bday")
    inp = bday.split(" ")
    dict[inp[0]].append(inp[1])

for key in dict:
    if len(dict[key]) > 0:
        dict[key] = sorted(dict[key])
        for date in dict[key]:
            print(f"{key} {date}")
