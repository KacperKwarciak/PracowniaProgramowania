colors = ["Red", "Green","Blue"]
with open("colors.txt", "w") as f:
    for line in colors:
        f.write(line)
        f.write('\n')