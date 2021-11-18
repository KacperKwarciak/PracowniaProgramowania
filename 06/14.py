array=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
maxlen = 0
maxstring = ""

for x in array:
    if len(x) > maxlen:
        maxlen = len(x)
        maxstring = x

print(f"longest name: {maxstring}")