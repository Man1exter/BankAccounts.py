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

    @stanKonta.getter # pobieranie danych z konta
    def stanKonta(self):
        return "stan twojego konta => " + str(self.__stan) + " zl"


def menu1():
 print("WITAJ W BANKU MAN1EXTERA")
 print("=========================")
 print("[1] ====> ZALOGUJ <====")
 print("[2] ====> ZAREJESTRUJ <====")
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
          plik.write("\n")
          
        print("======================================")
        print("TWOJE DANE ZOSTALY DODANE DO KONTA")
        print("ZAPAMIETAJ ((LOGIN)) I ((HASLO)) DO KONTA")
        print("======================================")

menu1()
logins()