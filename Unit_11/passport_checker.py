# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def is_passport_valid(passport: dict):
    iyr = type(passport.get("iyr")) == type("")
    eyr = type(passport.get("eyr")) == type("")
    hgt = type(passport.get("hgt")) == type("")
    hcl = type(passport.get("hcl")) == type("")
    ecl = type(passport.get("ecl")) == type("")
    pid = type(passport.get("pid")) == type("")
    cid = type(passport.get("cid")) == type("")

    return iyr and eyr and hgt and hcl and ecl and pid and cid

def write_valid_passports(passport_path: str, valid_passports_path: str) -> int:
    passport = {}
    passports = ""
    passport_str = ""
    count = 0

    with open(passport_path, "r") as f:
        lines = f.readlines()
        lines.append("\n")
        for idx, line in enumerate(lines[:-1]):

            if line.strip() != "":
                pairs = line.strip().split()
                pairs = [p.split(":") for p in pairs]
                passport.update(pairs)
                passport_str += line

            if lines[idx + 1].strip() == "":
                if is_passport_valid(passport):
                    passports += passport_str + "\n"
                    count += 1

                passport_str = ""
                passport = {}


    with open(valid_passports_path, "w") as f:
        f.write(passports.strip()) 

    return count

passports_path = input("Enter the name of the file: ")
# passports_path = "scanned_passports.txt"
valid_passports_path = "valid_passports.txt"

c = write_valid_passports(passports_path, valid_passports_path)
print(f"There are {c} valid passports")