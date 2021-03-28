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
        print("ok")
    elif zdarzenie == 2:
        print("ok")

menu1()
logins()