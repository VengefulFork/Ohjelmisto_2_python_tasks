class Auto :

    tämän_hetkinen_nopeus = 0
    kuljettu_matka = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus


uusi_auto = Auto("ABC-120", 142)

print(f"Auton rekisteritunnus on {uusi_auto.rekisteritunnus}, huippunopeus on {uusi_auto.huippunopeus}km/h."
      f"\nAuton tämän hetkinen nopeus on {uusi_auto.tämän_hetkinen_nopeus} km/h ja tähän menessä kulkema matka on {uusi_auto.kuljettu_matka} km")