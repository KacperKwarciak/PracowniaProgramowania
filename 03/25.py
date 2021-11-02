a=input("a: ")
b=input("b: ")
a=int(a)
b=int(b)
b2=b
a2=a
t1="*"
t2=" "
for a in range(1,a+1):
    if a==1 or a==a2:
        print(t1*b)
    if a>1 and a<a2:
        print(t1+t2*(b-2)+t1)
  
