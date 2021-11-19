file = open('numbers.txt','r')
sum=0
for line in file:
    num=int(line)
    print(num)
    sum+=num
print(sum)
file.close()