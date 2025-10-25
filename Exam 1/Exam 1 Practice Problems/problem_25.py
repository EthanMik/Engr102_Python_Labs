list = ["sdjflsd", "s", "sd", "slsd"]

m = list[0]
for str in list:
    if len(str) > len(m):
        m = str

print(f"The longest word \"{m}\" has {len(m)} characters")