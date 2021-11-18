array=[1,2,3,4,5,6,7]
x=int(input("Enter number: "))
z=0
for i in array:
    if x<i:
        z=z+1
print(z)