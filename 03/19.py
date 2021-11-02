pies=input("Podaj ludzkie lata psa: ")
pies=int(pies)
i=0
x=0
pies=pies+1
for i in range(1,pies):
    if i<=2:
        x=x+10.5
    if i>2:
        x=x+4
print(f"Psie lata psa: {x}")
