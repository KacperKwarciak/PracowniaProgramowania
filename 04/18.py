def getsum(number):
    n=str(number)
    sum=0
    for x in range(0,len(n)):
        sum=sum+int(n[x])
    return sum
print(getsum(7182))
    