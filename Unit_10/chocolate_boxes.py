# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

chocolates = {1: ["milk", "round", "toffee", "sprinkles"],
2: ["milk", "square", "coconut", "none"],
3: ["dark", "heart", "strawberry", "white chocolate drizzle"],
4: ["dark", "round", "toffee", "white chocolate drizzle"],
5: ["milk", "square", "caramel", "nuts"],
6: ["milk", "heart", "toffee", "dark chocolate drizzle"],
7: ["dark", "rectangle", "caramel", "none"],
8: ["dark", "heart", "strawberry", "white chocolate drizzle"],
9: ["dark", "heart", "coconut", "white chocolate drizzle"],
10: ["milk", "square", "coconut", "none"],
11: ["milk", "round", "vanilla", "dark chocolate drizzle"],
12: ["milk", "round", "strawberry", "nuts"],
13: ["milk", "rectangle", "caramel", "sprinkles"],
14: ["dark", "rectangle", "toffee", "none"],
15: ["dark", "heart", "toffee", "none"],
16: ["dark", "heart", "coconut", "white chocolate drizzle"],
17: ["dark", "round", "vanilla", "none"],
18: ["dark", "rectangle", "toffee", "dark chocolate drizzle"],
19: ["milk", "round", "toffee", "none"],
20: ["milk", "square", "caramel", "dark chocolate drizzle"],
21: ["milk", "square", "vanilla", "none"],
22: ["dark", "heart", "caramel", "sprinkles"],
23: ["milk", "square", "caramel", "nuts"],
24: ["milk", "round", "caramel", "dark chocolate drizzle"],
25: ["milk", "round", "coconut", "dark chocolate drizzle"],
26: ["dark", "round", "coconut", "dark chocolate drizzle"],
27: ["milk", "rectangle", "strawberry", "sprinkles"],
28: ["white", "heart", "vanilla", "none"],
29: ["dark", "heart", "strawberry", "none"],
30: ["dark", "rectangle", "caramel", "none"],
31: ["white", "round", "caramel", "none"],
32: ["milk", "heart", "vanilla", "none"],
33: ["white", "round", "strawberry", "nuts"],
34: ["milk", "round", "coconut", "none"],
35: ["dark", "rectangle", "coconut", "dark chocolate drizzle"],
36: ["milk", "round", "vanilla", "dark chocolate drizzle"],
37: ["dark", "round", "coconut", "white chocolate drizzle"],
38: ["dark", "round", "coconut", "white chocolate drizzle"],
39: ["dark", "round", "coconut", "dark chocolate drizzle"],
40: ["dark", "round", "strawberry", "dark chocolate drizzle"],
41: ["milk", "rectangle", "toffee", "none"],
42: ["milk", "round", "strawberry", "white chocolate drizzle"],
43: ["milk", "heart", "coconut", "none"],
44: ["white", "round", "strawberry", "white chocolate drizzle"],
45: ["milk", "heart", "toffee", "sprinkles"],
46: ["milk", "rectangle", "strawberry", "none"],
47: ["white", "round", "caramel", "dark chocolate drizzle"],
48: ["white", "square", "toffee", "none"],
49: ["milk", "rectangle", "toffee", "none"],
50: ["dark", "rectangle", "caramel", "none"],
51: ["milk", "square", "vanilla", "none"],
52: ["dark", "round", "toffee", "dark chocolate drizzle"],
53: ["milk", "round", "toffee", "white chocolate drizzle"],
54: ["dark", "square", "strawberry", "none"],
55: ["milk", "heart", "caramel", "dark chocolate drizzle"],
56: ["milk", "heart", "vanilla", "none"],
57: ["milk", "heart", "caramel", "none"],
58: ["milk", "heart", "coconut", "sprinkles"],
59: ["milk", "heart", "vanilla", "sprinkles"],
60: ["dark", "square", "caramel", "none"],
61: ["milk", "rectangle", "vanilla", "none"],
62: ["milk", "heart", "toffee", "none"],
63: ["milk", "heart", "vanilla", "dark chocolate drizzle"],
64: ["white", "round", "coconut", "white chocolate drizzle"],
65: ["milk", "round", "coconut", "nuts"],
66: ["milk", "round", "coconut", "white chocolate drizzle"],
67: ["dark", "heart", "coconut", "none"],
68: ["dark", "square", "toffee", "none"],
69: ["dark", "round", "strawberry", "dark chocolate drizzle"],
70: ["milk", "heart", "caramel", "none"],
71: ["milk", "square", "caramel", "sprinkles"],
72: ["milk", "rectangle", "strawberry", "sprinkles"],
73: ["dark", "heart", "strawberry", "none"],
74: ["dark", "heart", "strawberry", "none"],
75: ["dark", "square", "coconut", "none"],
76: ["dark", "heart", "caramel", "none"],
77: ["dark", "heart", "coconut", "nuts"],
78: ["white", "rectangle", "caramel", "dark chocolate drizzle"],
79: ["milk", "heart", "vanilla", "sprinkles"],
80: ["white", "heart", "strawberry", "none"],
81: ["dark", "round", "toffee", "white chocolate drizzle"],
82: ["dark", "round", "vanilla", "none"],
83: ["white", "square", "coconut", "none"],
84: ["milk", "rectangle", "caramel", "dark chocolate drizzle"],
85: ["white", "heart", "toffee", "none"],
86: ["white", "round", "caramel", "nuts"],
87: ["white", "round", "caramel", "none"],
88: ["dark", "round", "caramel", "none"],
89: ["dark", "square", "coconut", "nuts"],
90: ["milk", "heart", "vanilla", "none"],
91: ["dark", "round", "coconut", "none"],
92: ["dark", "round", "caramel", "none"],
93: ["white", "round", "toffee", "none"],
94: ["milk", "round", "vanilla", "sprinkles"],
95: ["white", "round", "strawberry", "white chocolate drizzle"],
96: ["dark", "square", "strawberry", "nuts"],
97: ["milk", "round", "vanilla", "none"],
98: ["milk", "rectangle", "caramel", "sprinkles"],
99: ["milk", "heart", "vanilla", "none"],
100: ["dark", "rectangle", "strawberry", "white chocolate drizzle"],
}



def make_boxes(chocolates: dict) -> list[list]:
    # no two truffles can be same
    # caramel and vanilla creme cannot be in same box
    # sprinkes and nuts cannot be in same box
    # rectangles and squares cannot be in same box
    # boxes must contain two dark choclate truffles, no more than 3
    truffle_num = 4
    boxes_num = len(chocolates) / truffle_num

    def sort_bucket(bucket: list, segregation: str) -> list:
        bucket1 = []
        bucket2 = []
        for idx, val in enumerate(bucket):
            if segregation in chocolates[val]:
                bucket1.append(val)
            else:
                bucket2.append(val)
        return [bucket1, bucket2]

    buckets = [i + 1 for i in range(len(chocolates))]
    # Sort out all caramels from vanilla creme
    buckets = sort_bucket(buckets, "caramel")
    for idx, bucket in enumerate(buckets):
        buckets[idx] = sort_bucket(bucket, "sprinkles") 
    for b in buckets:
        for idx, bucket in enumerate(b):
            b[idx] = sort_bucket(bucket, "rectangle") 

    print(buckets)

make_boxes(chocolates)
