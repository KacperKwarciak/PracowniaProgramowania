kwota=input("Podaj kwote(liczbe naturalna): ")
kwota=int(kwota)
if kwota>=5:
    piec= kwota//5
    print(f"5zl-{piec}")
    reszta=kwota-(piec*5)
if reszta>=2:
    dwa=reszta//2
    print(f"2zl-{dwa}")
    reszta=reszta-(dwa*2)
if reszta>=1:
    jeden=reszta//1
    print(f"1zl-{jeden}")
