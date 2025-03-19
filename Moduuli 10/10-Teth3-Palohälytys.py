class Hissi ():

    def __init__(self, alin_kerros, ylin_kerros, hissin_nimi):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.aloitus_kerros = alin_kerros
        self.tämän_hetkinen_kerros = alin_kerros
        self.hissin_nimi = hissin_nimi

    def kerros_alas(self):
        if self.tämän_hetkinen_kerros == self.alin_kerros :
            print("Hissi ei voi mennä tätä kerrosta alemmaksi")
        elif self.tämän_hetkinen_kerros > self.alin_kerros :
            self.tämän_hetkinen_kerros -= 1
            print(f"\nHissin uusi kerros on {self.tämän_hetkinen_kerros}")
        return

    def kerros_ylös(self):
        if self.tämän_hetkinen_kerros == self.ylin_kerros :
            print("Hissi ei voi mennä tätä kerrosta alemmaksi")
        elif self.tämän_hetkinen_kerros < self.ylin_kerros :
            self.tämän_hetkinen_kerros += 1
            print(f"\nHissin uusi kerros on {self.tämän_hetkinen_kerros}")


        return
    def siirrä (self, kerroksen_numero) :
        print(f"\nHissin {self.hissin_nimi} kerros on {self.tämän_hetkinen_kerros}")
        while self.tämän_hetkinen_kerros != kerroksen_numero :
            if self.tämän_hetkinen_kerros < kerroksen_numero :
                self.kerros_ylös()
            elif self.tämän_hetkinen_kerros > kerroksen_numero :
                self.kerros_alas()
        if self.tämän_hetkinen_kerros == self.alin_kerros:
                print(f"Hissi {self.hissin_nimi} on alimmassa kerroksessa")

        return

class Talo () :
    def __init__(self, talon_alin_kerros, talon_ylin_kerros, hissien_määrä):
        self.talon_alin_kerros = talon_alin_kerros
        self.talon_ylin_kerros = talon_ylin_kerros
        self.hissien_määrä = hissien_määrä
        self.hissit = []
        self.hissien_luonti()
    def hissien_luonti(self):
        b = 0
        for a in range(self.hissien_määrä) :
            b += 1
            a = Hissi(self.talon_alin_kerros, self.talon_ylin_kerros, b)
            self.hissit.append(a)
        return
    def talo_hissien_siirtäminen (self, hissin_numero, kohde_kerros) :
        for a in self.hissit :
            if hissin_numero == a.hissin_nimi :
                print(f"\nSiirrät hissiä {hissin_numero}")
                a.siirrä(kohde_kerros)


        return
    def hälytys (self):
        for b in self.hissit :
            b.siirrä(self.talon_alin_kerros)
        return


t = Talo(1, 10, 5)

t.talo_hissien_siirtäminen(5, 9)
t.talo_hissien_siirtäminen(2, 5)
t.hälytys()