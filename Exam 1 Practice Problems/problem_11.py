for i in range(2, 6):
    sum = 0
    print(f"{i}", end="    ")
    for j in range(1, 11):
        sum += i
        print(f"{sum}, ", end="")
    print()