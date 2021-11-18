def minmax(array):
    maxnum=array[0]
    minnum=array[0]
    for i in array:
        if i>maxnum:
            maxnum=i
        if i<minnum:
            minnum=i
    print(minnum, maxnum)
array=[4,2,8,4,7,9,5]
minmax(array)
