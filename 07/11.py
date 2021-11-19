film_titles=["Django","Avatar","Spider-man","Avengers","It"]
file=open("films.txt","w")
for line in film_titles:
    file.write(line+"\n")
file.close()