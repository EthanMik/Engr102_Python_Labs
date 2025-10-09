flights = ["12A23B45F", "01F03C23D"]

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def print_flights(flights: list):
    p = 0
    a = 0
    w = 0

    for i, ticket in enumerate(flights):
        a_t = 0
        w_t = 0

        for t in ticket:
            if t == "A" or t == "F":
                a_t += 1
                a += 1
            elif t == "D" or t == "C":
                w_t += 1
                w += 1
            if t in LETTERS: p += 1
        print(f"Group {i + 1} has {w_t} window seats and {a_t} aisle seats")

    print(f"There are {p} passengers, {a} aisle seats and {w} window seats")

print_flights(flights)