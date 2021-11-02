x=input("Podaj x: ")
y=input("Podaj y: ")
x=int(x)
y=int(y)
if x>0 and y>0:
    print(f"Punkt P({x},{y}) lezy na 1 cwiartce")
if x<0 and y>0:
    print(f"Punkt P({x},{y}) lezy na 2 cwiartce")
if x<0 and y<0:
    print(f"Punkt P({x},{y}) lezy na 3 cwiartce")
if x>0 and y<0:
    print(f"Punkt P({x},{y}) lezy na 4 cwiartce")