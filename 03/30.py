n=input("N: ")
n=int(n)
i=1
while i<=n:
    if i%(i+1)!=0 :
        i=i+1
    else:
        print(i)
        i=i+1;
