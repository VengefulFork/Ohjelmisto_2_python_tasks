class Julkaisu():

    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"Julkaisun nimi : {self.nimi}")


class Lehti(Julkaisu):

    def __init__(self, päätoimittaja, nimi):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulostus (self):
        super().tulosta_tiedot()
        print(f"Julkaisun päätoimittaja : {self.päätoimittaja}")
class Kirja(Julkaisu):
    def __init__(self, kirjailija, nimi, sivumäärä):
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä
        super().__init__(nimi)
    def tulostus (self):
        super().tulosta_tiedot()
        print(f"Kirjailija : {self.kirjailija} ja sivumäärä {self.sivumäärä}")
aku = Lehti("Aki Hyyppä", "Aku Ankka")
aku.tulostus()

hytti = Kirja("Rosa Liksom", "Hytti n:o 6", "200")
hytti.tulostus()