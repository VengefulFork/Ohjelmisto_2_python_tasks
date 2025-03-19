


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


uusi_auto = Auto("ABC-120", 142)
uusi_auto.kiihdytä(30)
uusi_auto.kiihdytä(50)
uusi_auto.kiihdytä(70)
print(f"{uusi_auto.tämän_hetkinen_nopeus} km/h")

uusi_auto.kiihdytä(-200)
print(f"{uusi_auto.tämän_hetkinen_nopeus} km/h")


