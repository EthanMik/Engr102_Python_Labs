import random

sex = ""  # "F" "M"
age = 0   # (20–34, 35–39, …, 70–79)
cho = 0   # <160, 160–199, 200–239, 240–279, ≥280)
smo = ""  # "Y" "N"
hdl = 0   # (≥60, 50–59, 40–49, <40)
sdp = 0   # (<120, 120–129, 130–139, 140–159, ≥160)
med = ""  # "Y" "N"
out = 0.0 # Percentage 

# with open("Unit_5/tyr_test_cases.txt", "r") as file:
#     lines = file.readline()
#     print(lines)

# with open("Unit_5/tyr_test_cases.txt", "w") as file:
#     lines = file.write("e")
#     print(lines)

def get_num_in_bracket(bracket: str) -> int:
    if bracket[0] == "<":
        num = int(bracket[1:len(bracket)])
        return random.randint(num - 10, num - 1)
    if bracket[0] == ">":
        num = int(bracket[1:len(bracket)])
        return random.randint(num, num + 10)
    
    dash_found = False
    min, max = "", ""
    for char in bracket:
        if char == '-':
            dash_found = True
            continue
        if dash_found: max += char
        else: min += char
    return random.randint(int(min), int(max))

def to_bracket():


sex = ["F", "M"]
age = [20, 79]
cho = [150, 290]
smo = ["N", "Y"]
hdl = [70, 30]
med = ["Y", "N"]
sdp = [110, 170]

FRAMINGHAM_LOOKUP = {
    "M": {
        "age": {
            "20-34": -9, "35-39": -4, "40-44": 0, "45-49": 3,
            "50-54": 6, "55-59": 8, "60-64": 10, "65-69": 11,
            "70-74": 12, "75-79": 13
        },
        "cho": {
            "20-39": {"<160": 0, "160-199": 4, "200-239": 7, "240-279": 9, ">280": 11},
            "40-49": {"<160": 0, "160-199": 3, "200-239": 5, "240-279": 6, ">280": 8},
            "50-59": {"<160": 0, "160-199": 2, "200-239": 3, "240-279": 4, ">280": 5},
            "60-69": {"<160": 0, "160-199": 1, "200-239": 1, "240-279": 2, ">280": 3},
            "70-79": {"<160": 0, "160-199": 0, "200-239": 0, "240-279": 1, ">280": 1},
        },
        "smo": {
            "20-39": {"N": 0, "Y": 8},
            "40-49": {"N": 0, "Y": 5},
            "50-59": {"N": 0, "Y": 3},
            "60-69": {"N": 0, "Y": 1},
            "70-79": {"N": 0, "Y": 1},
        },
        "hdl": {">60": -1, "50-59": 0, "40-49": 1, "<40": 2},
        "sbp": {
            "N": {"<120": 0, "120-129": 0, "130-139": 1, "140-159": 1, ">160": 2},
            "Y":   {"<120": 0, "120-129": 1, "130-139": 2, "140-159": 2, ">160": 3},
        },
        "out": {
            "<0": "<1", "0": "1", "1": "1", "2": "1", "3": "1",
            "4": "1", "5": "2", "6": "2", "7": "3", "8": "4",
            "9": "5", "10": "6", "11": "8", "12": "10", "13": "12",
            "14": "16", "15": "20", "16": "25", ">17": ">30"
        },
    },

    "F": {
        "age": {
            "20-34": -7, "35-39": -3, "40-44": 0, "45-49": 3,
            "50-54": 6, "55-59": 8, "60-64": 10, "65-69": 12,
            "70-74": 14, "75-79": 16
        },
        "cho": {
            "20-39": {"<160": 0, "160-199": 4, "200-239": 8, "240-279": 11, ">280": 13},
            "40-49": {"<160": 0, "160-199": 3, "200-239": 6, "240-279": 8, ">280": 10},
            "50-59": {"<160": 0, "160-199": 2, "200-239": 4, "240-279": 5, ">280": 7},
            "60-69": {"<160": 0, "160-199": 1, "200-239": 2, "240-279": 3, ">280": 4},
            "70-79": {"<160": 0, "160-199": 1, "200-239": 1, "240-279": 2, ">280": 2},
        },
        "smo": {
            "20-39": {"N": 0, "Y": 9},
            "40-49": {"N": 0, "Y": 7},
            "50-59": {"N": 0, "Y": 4},
            "60-69": {"N": 0, "Y": 2},
            "70-79": {"N": 0, "Y": 1},
        },
        "hdl": {">60": -1, "50-59": 0, "40-49": 1, "<40": 2},
        "sbp": {
            "N": {"<120": 0, "120-129": 1, "130-139": 2, "140-159": 3, ">160": 4},
            "Y":   {"<120": 0, "120-129": 3, "130-139": 4, "140-159": 5, ">160": 6},
        },
        "out": {
            "<9": "<1", "9": "1", "10": "1", "11": "1", "12": "1",
            "13": "2", "14": "2", "15": "3", "16": "4", "17": "5",
            "18": "6", "19": "8", "20": "11", "21": "14", "22": "17",
            "23": "22", "24": "27", ">25": ">30"
        },
    },
}

# sex:F age:40 cho:105 smo:N hdl:60 sbp:100 med:N out:<1

def iter_framingham_combinations(table):
    for sex, sex_tbl in table.items():
        # Age section
        for age_band, age_pts in sex_tbl["age"].items():
            chol_age_band = get_num_in_bracket(age_band)
            print(chol_age_band)

            # Cholesterol & smoker tables depend on the age band above
            chol_rows   = sex_tbl["cho"][chol_age_band]   # e.g., {'<160':0, ...}
            smoker_rows = sex_tbl["smo"][chol_age_band]        # {'nonsmoker':0, 'smoker':8}

            for chol_range, chol_pts in chol_rows.items():
                for smoker_status, smoke_pts in smoker_rows.items():
                    for hdl_band, hdl_pts in sex_tbl["hdl"].items():
                        for treat_flag, sbp_rows in sex_tbl["sbp"].items():
                            for sbp_range, sbp_pts in sbp_rows.items():
                                total = age_pts + chol_pts + smoke_pts + hdl_pts + sbp_pts
                                risk  = _risk_lookup(sex_tbl["out"], total)

                                yield {
                                    "sex": sex,
                                    "age_band": age_band,
                                    "age_points": age_pts,
                                    "chol_age_band": chol_age_band,
                                    "chol_range": chol_range,
                                    "chol_points": chol_pts,
                                    "smoker": smoker_status,
                                    "smoker_points": smoke_pts,
                                    "hdl_band": hdl_band,
                                    "hdl_points": hdl_pts,
                                    "treated": treat_flag,      # SBP section
                                    "sbp_range": sbp_range,
                                    "sbp_points": sbp_pts,
                                    "total_points": total,
                                    "risk_percent": risk,       # looks like '6', '≥30', etc.
                                }


iter_framingham_combinations(FRAMINGHAM_LOOKUP)
# for sex, table in FRAMINGHAM_LOOKUP.items():
#     for points, risk in table["out"].items():
#         print(sex, points, "->", risk)
