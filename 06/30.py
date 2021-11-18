import random
def rand_elem(array):
    a=random.randint(0,len(array)-1)
    return array[a]
array1=[1,5,2,3,6,4,23,5,6,2]
print(rand_elem(array1))
print(rand_elem(array1))
print(rand_elem(array1))