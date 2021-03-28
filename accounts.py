class Rejestrowany:
    def __init__(self,imie,nazwisko,wiek,nrtel,pesel,zawod):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.nrtel = nrtel
        self.pesel = pesel
        self.zawod = zawod


def menu1():
 print("WITAJ W BANKU MAN1EXTERA")
 print("=========================")
 print("[1] ====> ZALOGUJ <====")
 print("[2] ====> ZAREJESTRUJ <====")
 print("=========================")


def logins():
    zdarzenie = int(input("[1]ZALOGUJ LUB [2]ZAREJESTRUJ =====> "))

    if zdarzenie == 1:

        login = input("podaj login do konta => ")
        haslo = input("podaj haslo do hasla => ")
        
    elif zdarzenie == 2:
        
        print("======================================")
        print("PODAJ DANE POTRZEBNE DO REJESTRACJI")
        imie = input("Podaj imie => ")
        nazwisko = input("Podaj nazwisko => ")
        wiek = input("Podaj wiek => ")
        nrtel = input("Podaj nrtel => ")
        pesel = input("Podaj pesel => ")
        zawod = input("Podaj zawod => ")
        print("DODATKOWE INFORMACJE DO KONTA : ")
        login = input("podaj login => ")
        haslo = input("podaj haslo => ")
        print("======================================")

menu1()
logins()