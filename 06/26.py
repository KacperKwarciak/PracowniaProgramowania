array1=[2,2,6,3,6,5,2,3]
array2=array1
a=0
b=len(array1)-1
for x in range(0,len(array1)):
    if array1[x]%2==0:
        array2[a]=array1[x]
        a=a+1
    else:
        array2[b]=array1[x]
        b=b-1
print(array2)