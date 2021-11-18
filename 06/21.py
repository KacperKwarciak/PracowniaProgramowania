def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

array=[5,1,9,6,1]
bubblesort(array)
largest=array[0]
largest2=largest
for x in array:
    if largest<x:
        largest2=largest
        largest=x
print(largest2)