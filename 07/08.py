file = open('countries.txt','r')
ln=1
for line in file:
     print(ln,line, end="")
     ln+=1

file.close()

