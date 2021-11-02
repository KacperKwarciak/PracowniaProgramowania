liczba1=input("Podaj 1. liczbe: ")
liczba2=input("Podaj 2. liczbe: ")
liczba1=int(liczba1)
liczba2=int(liczba2)
if liczba1>liczba2:
    print(f"Liczby w kolejności rosnącej: {liczba2}, {liczba1}")
if liczba2>liczba1:
    print(f"Liczby w kolejności rosnącej: {liczba1}, {liczba2}")
else:
    print("Liczby są takie same")