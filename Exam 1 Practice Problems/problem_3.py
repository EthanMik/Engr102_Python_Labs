roster = [  
            ["123004567", ["Joe", "Aggie", "ENGE", 3.50]  ],
            ["123004568", ["Jake", "Green", "OCEN", 3.75] ],
            ["123004569", ["Jill", "Apple", "ENGR", 3.25] ]
        ]

uin = input("Enter a UIN: ")
for i in range(len(roster)):
    if roster[i][0] == uin:
        d = roster[i][1]
        print(f"{d[0]} {d[1]}: {d[2]}, {d[3]:.2f}")