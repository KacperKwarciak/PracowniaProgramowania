numbers=[5, 1, 9, 6, 1]
maxnum=numbers[0]
minnum=numbers[0]
for i in numbers:
    if i>maxnum:
        maxnum=i
    if i<minnum:
        minnum=i
y=maxnum-minnum
print(y)