

class Auto :

    tämän_hetkinen_nopeus = 0
    kuljettu_matka = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

    def kiihdytä(self, nopeuden_muutos):
        self.tämän_hetkinen_nopeus += nopeuden_muutos
        if self.tämän_hetkinen_nopeus < 0:
            self.tämän_hetkinen_nopeus = 0
        elif self.tämän_hetkinen_nopeus > self.huippunopeus:
            self.tämän_hetkinen_nopeus = 142
        return
    def kulje (self, aika):
        self.kuljettu_matka = self.tämän_hetkinen_nopeus * aika
        return

uusi_auto = Auto("ABC-120", 142)
uusi_auto.kiihdytä(60)
uusi_auto.kulje(1.5)

print(f"{uusi_auto.kuljettu_matka} km")
