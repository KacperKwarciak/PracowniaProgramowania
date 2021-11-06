x=input("Podaj x: ")
y=input("Podaj y: ")
x=int(x)
y=int(y)
if x>0 and y>0:
    print(f"Punkt P({x},{y}) lezy na 1 cwiartce")
elif x<0 and y>0:
    print(f"Punkt P({x},{y}) lezy na 2 cwiartce")
elif x<0 and y<0:
    print(f"Punkt P({x},{y}) lezy na 3 cwiartce")
elif x>0 and y<0:
    print(f"Punkt P({x},{y}) lezy na 4 cwiartce")
elif x==0 and y!=0:
    print(f"Punkt P({x},{y}) lezy na osi Y")
elif x!=0 and y==0:
    print(f"Punkt P({x},{y}) lezy na osi X")
elif x==0 and y==0:
    print(f"Punkt P({x},{y}) jest na środku układu wspolrzednych")