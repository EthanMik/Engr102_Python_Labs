def myinsert(sorted: str, char: str):
    for idx, l in enumerate(sorted):
        if char < l:
            return sorted[:idx] + char + sorted[idx:] 

print(myinsert("123589", "7"))