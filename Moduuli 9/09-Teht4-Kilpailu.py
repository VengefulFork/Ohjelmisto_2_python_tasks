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

def kilpailu ():
    autot = []
    b = 0
    lippu = True

    for i in range (10) :
        b += 1
        uusi_auto = Auto(f"ABC-{b}", random.randint(100, 200))
        autot.append(uusi_auto)
    for a in autot:
        print(f"Rekisteritunnus {a.rekisteritunnus}, huippunopeus {a.huippunopeus} km/h")
    while lippu:


        for b in autot :
            b.kiihdytä(random.randrange(-10, 15))
            # print(f"Auton tämän hetkinen nopeus {b.tämän_hetkinen_nopeus} km/h")
            b.kulje(1)
            # print(f"Auton kulkema matka {b.kuljettu_matka}")

        for c in autot :

            if c.kuljettu_matka >= 10000 :
                lippu = False
    for c in autot :
        print(f"Auton rekisteritunnus {c.rekisteritunnus}, huippunopeus {c.huippunopeus} km/h, tämän hetkinen nopeus {c.tämän_hetkinen_nopeus} km/h, kuljettu matka {c.kuljettu_matka} km.")


    return
kilpailu()