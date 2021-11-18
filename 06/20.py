def occurs(number, array):
    for x in array:
        if number==x:
            return True
            print("T")
array=[15, 38, 7, 23, 14]
number=int(input("Enter number: "))
occurs(number, array)