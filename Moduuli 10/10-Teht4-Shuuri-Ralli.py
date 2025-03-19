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


def kilpailu ():
    autot = []
    b = 0
    for i in range (10) :
        b += 1
        uusi_auto = Auto(f"ABC-{b}", random.randint(100, 200))
        autot.append(uusi_auto)
    suuri_romuralli = ralli("Suuri romuralli", 8000, autot)

    # for a in autot:


    #     print(f"Rekisteritunnus {a.rekisteritunnus}, huippunopeus {a.huippunopeus} km/h")
    # while lippu:
    #
    #
    #     for b in autot :
    #         b.kiihdytä(random.randrange(-10, 15))
    #         # print(f"Auton tämän hetkinen nopeus {b.tämän_hetkinen_nopeus} km/h")
    #         b.kulje(1)
    #         # print(f"Auton kulkema matka {b.kuljettu_matka}")
    #
    #     for c in autot :
    #
    #         if c.kuljettu_matka >= 10000 :
    #             lippu = False