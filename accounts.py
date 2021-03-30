import linecache
class KontoBankowe:
    def __init__(self,imie,nazwisko,wiek,nrtel,pesel,zawod,__stan):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.nrtel = nrtel
        self.pesel = pesel
        self.zawod = zawod
        self.__stan = __stan

    @property
    def stanKonta(self):
        return self.__stan

    @stanKonta.getter # pobieranie danych z konta...
    def stanKonta(self):
        return "stan twojego konta => " + str(self.__stan) + " <= PLN"

    @stanKonta.setter # zmiany na koncie...
    def stanKonta(self,value):
        self.__stan += value
        

def menu1():
 print("WITAJ W BANKU [MAN1EXTERA]")
 print("=========================")
 print("[1] ====> ZALOGUJ <====")
 print("[2] ====> ZAREJESTRUJ <====")
 print("[3] ====> INFORMACJE O KONTACH UZYTKOWNIKOW <====")
 print("=========================")


def logins():
    plik = open("konta.txt","a")
    zdarzenie = int(input("[1]ZALOGUJ LUB [2]ZAREJESTRUJ =====> "))

    if zdarzenie == 1:

        print("======================================")
        login = input("podaj login do konta => ")
        haslo = input("podaj haslo do hasla => ")
        print("WITAJ NA KONCIE " + login )
        print("======================================")


        print("CO CHCESZ ZROBIC NA SWOIM KONCIE?")
        print("[1] zobaczenie salda na koncie")
        print("[2] wyplata pieniedzy z konta")
        print("[3] wplata pieniedzy na konto")
        print("[4] wyjscie z programu")
        celMenu = int(input("Operacja =========> "))

        if celMenu == 1:
            konto = KontoBankowe()
            print(konto.stanKonta())
        elif celMenu == 2:
            wyplata()
        elif celMenu == 3:
            wplata()
        elif celMenu == 4:
            exit()
        
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

        if plik.writable():
          plik.write(imie )
          plik.write(" ")
          plik.write( nazwisko )
          plik.write(" ")
          plik.write( wiek )
          plik.write(" ")
          plik.write( nrtel )
          plik.write(" ")
          plik.write( pesel )
          plik.write(" ")
          plik.write( zawod )
          plik.write(" ")
          plik.write( login )
          plik.write(" ")
          plik.write( haslo )
          plik.write(" ")
          konto = KontoBankowe()
          plik.write( konto.__stan )
          plik.write(" ")
          plik.write("\n")
        plik.close()
          
        print("======================================")
        print("TWOJE DANE ZOSTALY DODANE DO KONTA")
        print("ZAPAMIETAJ ((=> LOGIN <=)) I ((=> HASLO <=)) DO KONTA")
        print("======================================")

    elif zdarzenie == 3:
        info()

    else:
        print("nie wiem co chcesz zrobic..")

def wyplata():
    konto = KontoBankowe()
    wyplata = int(input("Ile chcesz wyplacic z konta? => "))
    wyplata = konto.__stan + wyplata
    print(konto.__stan)

    zrodlo = open("konta.txt").readlines()
    cel = open("konta.txt","w")
    for text in zrodlo:
        cel.write(text.replace(konto.__stan,wyplata))
    cel.close

def wplata():
    konto = KontoBankowe()
    wplata = int(input("Ile chcesz wplacic na konto? => "))
    wplata = konto.__stan - wplata
    print(konto.__stan)

    zrodlo = open("konta.txt").readlines()
    cel = open("konta.txt","w")
    for text in zrodlo:
        cel.write(text.replace(konto.__stan,wplata))
    cel.close

def info():
    print(" ===> INFORMACJE O KONTACH UZYTKOWNIKOW <===")
    stand = input("KONTO ===> premium czy standardowe? : ")
    
menu1()
logins()