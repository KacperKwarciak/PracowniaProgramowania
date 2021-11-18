
array=[1,23,5,382,1,17,4,906]
for x in range(0,len(array)):
    if x!=0:
        print("-",end="")
    print("---",end="")
print("--")
print("|",end="")
for x in range(0,len(array)):
    a=2
    b=array[x]
    while b>10:
        a=a-1
        b=b/10
    for y in range(0,a):
        print(" ",end="")
    print(array[x],end="")
    print("|",end="")
print()
for x in range(0,len(array)):
    if x!=0:
        print("-",end="")
    print("---",end="")
print("--")