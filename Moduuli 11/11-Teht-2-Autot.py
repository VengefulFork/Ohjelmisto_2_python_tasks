class Auto :

    tämän_hetkinen_nopeus = 0
    kuljettu_matka = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
    def liiku(self, aika):
        self.kuljettu_matka = self.tämän_hetkinen_nopeus * aika
        return
class Sähkö(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)
        self.tämän_hetkinen_nopeus = self.huippunopeus

class Polttomoottori(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_kapasiteetti):
        self.tankin_kapasiteetti = tankin_kapasiteetti
        super().__init__(rekisteritunnus,huippunopeus)
        self.tämän_hetkinen_nopeus = self.huippunopeus

a = Sähkö("ABC-15", 180, 52)
a.liiku(3)
b = Polttomoottori("ACD-123", 165, 32.3)
b.liiku(3)
print(f"Auton {a.rekisteritunnus} kulkema matka {a.kuljettu_matka} km")
print(f"AUton {b.rekisteritunnus} kulkema matka {b.kuljettu_matka} km")


