wzrost=input("Podaj swoj wzrost w cm: ")
waga=input("Podaj swoja wage w kg: ")
wzrost=int(wzrost)
waga=int(waga)
wzrost=wzrost/100
bmi= waga/wzrost**2
print(f"Twoje BMI wynosi {bmi}")