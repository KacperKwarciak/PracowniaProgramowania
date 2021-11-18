
def appear(array1,array2):
    appears1=True
    for x in array1:
        appears2=False
        for y in array2:
            if x==y:
                appears2=True
                break
        if appears2==False:
            appears1=False
            break
    return appears1
array1=[1,2,3]
array2=[1,2,3,4,5,6]
print(appear(array1,array2))