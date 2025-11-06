# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

def clamp(num: int, min: int, max: int, inclusive = True):
    num = int(num)
    if inclusive: return num >= min and num <= max
    return num > min and num < max

def contains_str(string: str, contain: str):
    for char in string:
        if not char in contain:
            return False
    return True

def contains_list(string: str, contain: list):
    return string in contain

def is_int(integer: str):
    try:
        integer = int(integer)
        return True
    except ValueError:
        return False

def leading_zero(num: str):
    return num[0] == "0"

def is_passport_valid(passport: dict):
    iyr = passport.get("iyr")
    eyr = passport.get("eyr")
    hgt = passport.get("hgt")
    hcl = passport.get("hcl")
    ecl = passport.get("ecl")
    pid = passport.get("pid")
    cid = passport.get("cid")

    if (iyr is None or eyr is None or hgt is None or hcl is None or ecl is None or pid is None or cid is None):
        return False

    iyr_b = len(iyr) == 4 and clamp(iyr, 2015, 2025)

    eyr_b = len(eyr) == 4 and clamp(eyr, 2025, 2035) 

    cm = hgt[-2:len(hgt)] == "cm"
    inch = hgt[-2:len(hgt)] == "in"
    hgt_b = cm and clamp(hgt[:-2], 150, 193) or inch and clamp(hgt[:-2], 59, 76)

    hcl_b = len(hcl) == 7 and hcl[0] == "#" and contains_str(hcl[1:], "0123456789abcdef")

    ecl_b = contains_list(ecl, ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

    pid_b = len(pid) == 9 and is_int(pid)

    cid_b = not leading_zero(cid) and len(cid) == 3

    return iyr_b and eyr_b and hgt_b and hcl_b and ecl_b and pid_b and cid_b

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
                # print(passport)
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
valid_passports_path = "valid_passports2.txt"

c = write_valid_passports(passports_path, valid_passports_path)
print(f"There are {c} valid passports")