def sec_max(l):
    max = float(l[0])
    s_max = float(l[0])

    for n in l:
        n = float(n)
        if n > max:
            max = n
        if n < max and n > s_max:
            s_max = n
    return s_max


l = input("Enter some numbers: ").split(" ")
print(f"The second largest value is {sec_max(l):.1f}")