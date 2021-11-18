arr=[2,3,2,5,8,1,9,8]
for x in range(0,len(arr)):
    appear=False
    for y in range(0,len(arr)):
        if arr[x]==arr[y] and x!=y:
            appear=True
    if appear==False:
        print(arr[x])