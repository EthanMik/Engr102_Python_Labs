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

from typing import Dict, List, Tuple

def make_boxes(chocolates: Dict[int, List[str]]) -> List[List[int]]:
    ids = list(chocolates.keys())
    TRUFFLES_PER_BOX = 4

    attrs: Dict[int, Tuple[str, str, str, str]] = {i: tuple(chocolates[i]) for i in ids}

    def is_dark(tid: int) -> bool:
        return attrs[tid][0] == "dark"

    # Heuristic: try "hard" items first (dark + square/rectangle)
    def sort_key(tid: int) -> Tuple[int, int]:
        t, s, _, _ = attrs[tid]
        return (-(t == "dark"), -(s in ("square", "rectangle")))
    
    ids.sort(key=sort_key)

    def can_add(box: List[int], tid: int) -> bool:
        if len(box) >= TRUFFLES_PER_BOX:
            return False
        
        if any(attrs[x] == attrs[tid] for x in box):
            return False

        t, s, f, top = attrs[tid]
        fillings = {attrs[x][2] for x in box}
        toppings = {attrs[x][3] for x in box}
        shapes   = {attrs[x][1] for x in box}

        # Pairwise incompatibilities
        if ("caramel" in fillings and f == "vanilla") or ("vanilla" in fillings and f == "caramel"):
            return False
        if ("sprinkles" in toppings and top == "nuts") or ("nuts" in toppings and top == "sprinkles"):
            return False
        if ("square" in shapes and s == "rectangle") or ("rectangle" in shapes and s == "square"):
            return False

        # Darks constraint (0 allowed; otherwise 2–3)
        before = sum(attrs[x][0] == "dark" for x in box)
        after  = before + (t == "dark")
        if after > 3:
            return False

        slots_left = TRUFFLES_PER_BOX - (len(box) + 1)

        # If we would have exactly 1 dark, we must still have at least one slot to reach 2.
        if after == 1 and slots_left < 1:
            return False

        # If we already have darks (after >= 1), we must be able to reach at least 2 by the end.
        # (after==0 is fine; we may finish with 0.)
        if after >= 1 and after + slots_left < 2:
            return False

        return True

    def box_valid(box: List[int]) -> bool:
        if len(box) != TRUFFLES_PER_BOX:
            return False
        darks = sum(attrs[x][0] == "dark" for x in box)
        # 0 is okay; otherwise 2–3
        return darks == 0 or 2 <= darks <= 3

    total_boxes = len(ids) // TRUFFLES_PER_BOX
    boxes: List[List[int]] = []

    def remaining_capacity() -> int:
        return total_boxes * TRUFFLES_PER_BOX - sum(len(b) for b in boxes)

    # Canonical snapshot for memoization (order-free)
    def normalize_state() -> Tuple[Tuple[int, ...], ...]:
        return tuple(sorted(tuple(sorted(b)) for b in boxes if b))

    visited = set()  # (idx, normalized_state)

    def darks_left_from(i: int) -> int:
        # Remaining darks among ids[i:]
        return sum(1 for k in ids[i:] if is_dark(k))

    def place_next(idx: int) -> bool:
        # Base: all placed?
        if idx == len(ids):
            return len(boxes) == total_boxes and all(box_valid(b) for b in boxes)

        # Not enough total slots left?
        if remaining_capacity() < (len(ids) - idx):
            return False

        # Prune on darks feasibility:
        boxes_darks = [sum(is_dark(x) for x in b) for b in boxes]
        ones_need_dark = sum(1 for d in boxes_darks if d == 1)  # each needs +1 dark
        darks_left = darks_left_from(idx)

        # If we can't supply at least one more dark to every 1-dark box, dead.
        if ones_need_dark > darks_left:
            return False

        # Also ensure we have enough capacity to absorb all remaining darks without exceeding 3/box
        dark_slots_available = sum(3 - d for d in boxes_darks) + 3 * (total_boxes - len(boxes))
        if darks_left > dark_slots_available:
            return False

        # Memoize
        key = (idx, normalize_state())
        if key in visited:
            return False
        visited.add(key)

        tid = ids[idx]

        # 1) Try existing boxes
        for b in boxes:
            if not can_add(b, tid):
                continue

            b.append(tid)

            # Validate immediately if filled
            if len(b) == TRUFFLES_PER_BOX and not box_valid(b):
                b.pop()
                continue

            if place_next(idx + 1):
                return True

            b.pop()

        # 2) Start a new box
        if len(boxes) < total_boxes:
            boxes.append([tid])
            if place_next(idx + 1):
                return True
            boxes.pop()

        return False

    if place_next(0):
        return boxes
    return []


if __name__ == "__main__":
    boxes = make_boxes(chocolates)
    print(f"Made {len(boxes)} boxes.")
    for i, b in enumerate(boxes, 1):
        print(f"Box {i}: {b}")


