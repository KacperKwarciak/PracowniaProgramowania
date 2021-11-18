array=[15, 8, 31, 47, 2, 19]
for x in range(0,int(len(arr)/2)):
    tmp=array[len(arr)-x-1]
    array[len(arr)-x-1]=arr[x]
    array[x]=tmp
print(array)   