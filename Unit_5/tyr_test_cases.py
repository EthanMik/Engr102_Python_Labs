sex = ""  # "F" "M"
age = 0   # (20–34, 35–39, …, 70–79)
cho = 0   # <160, 160–199, 200–239, 240–279, ≥280)
smo = ""  # "Y" "N"
hdl = 0   # (≥60, 50–59, 40–49, <40)
sdp = 0   # (<120, 120–129, 130–139, 140–159, ≥160)
med = ""  # "Y" "N"
out = 0.0 # Percentage 

with open("Unit_5/tyr_test_cases.txt", "r") as file:
    lines = file.readline()
    print(lines)

with open("Unit_5/tyr_test_cases.txt", "w") as file:
    lines = file.write("e")
    print(lines)
