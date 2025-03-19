import random
class Auto :

    tämän_hetkinen_nopeus = 0
    kuljettu_matka = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus


    def kiihdytä (self, nopeuden_muutos):
        self.tämän_hetkinen_nopeus += nopeuden_muutos
        if self.tämän_hetkinen_nopeus < 0 :
            self.tämän_hetkinen_nopeus = 0
        elif self.tämän_hetkinen_nopeus > self.huippunopeus :
            self.tämän_hetkinen_nopeus = 142
        return self.tämän_hetkinen_nopeus
    def kulje (self, aika):
        matka = self.tämän_hetkinen_nopeus * aika
        self.kuljettu_matka += matka
        return self.kuljettu_matka

class ralli () :
    def __init__(self, nimi, kilometri_määrä, auto_lista):
        self.nimi = nimi
        self.kilometri_määrä = kilometri_määrä
        self.auto_lista = auto_lista

    def tunti_kuluu(self):
        for b in self.auto_lista:
            b.kiihdytä(random.randrange(-10, 15))
            b.kulje(1)
        return
    def kilpailu_ohi(self):
        flag = False
        for a in self.auto_lista :
            if a.kuljettu_matka >= 8000 :
                flag = True
        return flag
    def tulosta_tillane(self):
        for c in self.auto_lista :
            print(f"{c.rekisteritunnus}, huipppunopeus {c.huippunopeus} km/h, tämän hetkinen nopeus {c.tämän_hetkinen_nopeus} km/h, kuljettu matka {c.kuljettu_matka} km.")


def kilpailu ():
    autot = []
    b = 0
    for i in range (10) :
        b += 1
        uusi_auto = Auto(f"ABC-{b}", random.randint(100, 200))
        autot.append(uusi_auto)
    s = ralli("Suuri romuralli", 8000, autot)
    tunnit = 0
    lippu = True

    while lippu :
        print(f"Kisassa kuluneet tunnit : {tunnit}")
        s.tunti_kuluu()
        if tunnit % 10 == 0:
            s.tulosta_tillane()
        if s.kilpailu_ohi() :
            lippu = False
            s.tulosta_tillane()
        tunnit += 1


kilpailu()
