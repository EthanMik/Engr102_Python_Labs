# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def is_passport_valid(passport: dict):
    iyr = type(passport.get("byr")) == type("")
    eyr = type(passport.get("eyr")) == type("")
    hgt = type(passport.get("hgt")) == type("")
    hcl = type(passport.get("hcl")) == type("")
    ecl = type(passport.get("ecl")) == type("")
    pid = type(passport.get("pid")) == type("")
    cid = type(passport.get("cid")) == type("")

    return iyr and eyr and hgt and hcl and ecl and pid and cid

def append_passport(path: str, passport: dict):
    if not (passport): return False

    passport_str = ""
    for idx, key in enumerate(passport):
        if idx < len(passport) - 1:
            passport_str += key + ":" + passport[key] + " "
        else:
            passport_str += key + ":" + passport[key] + "\n"
    
    return True

def write_valid_passports(passport_path: str, valid_passports_path: str) -> int:
    passport = {}
    passport_str = ""
    count = 0
    with open(passport_path, "r") as f:
        for line in f:
            if line.strip() != "":
                pairs = line.split()
                pairs = [p.split(":") for p in pairs]
                passport.update(pairs)
            else:
                if is_passport_valid(passport):
                    passport_str += line
                    count += 1
                passport = {}
    print(passport_str)
    with open(valid_passports_path, "w") as f:
        f.write(passport_str) 

    return count

# passports_path = "Unit_11/scanned_passports.txt"
passports_path = input("Enter the name of the file: ")
valid_passports_path = "valid_passports.txt"

c = write_valid_passports(passports_path, valid_passports_path)
print(f"There are {c} valid passports")