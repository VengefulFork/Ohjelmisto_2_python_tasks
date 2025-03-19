class Hissi ():

    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.aloitus_kerros = alin_kerros
        self.tämän_hetkinen_kerros = alin_kerros

    def kerros_alas(self):
        if self.tämän_hetkinen_kerros == self.alin_kerros :
            print("Hissi ei voi mennä tätä kerrosta alemmaksi")
        elif self.tämän_hetkinen_kerros > self.alin_kerros :
            self.tämän_hetkinen_kerros -= 1
            print(f"Hissin uusi kerros on {self.tämän_hetkinen_kerros}")
        return

    def kerros_ylös(self):
        if self.tämän_hetkinen_kerros == self.ylin_kerros :
            print("Hissi ei voi mennä tätä kerrosta alemmaksi")
        elif self.tämän_hetkinen_kerros < self.ylin_kerros :
            self.tämän_hetkinen_kerros += 1
            print(f"Hissin uusi kerros on {self.tämän_hetkinen_kerros}")
        return
    def siirrä (self, kerroksen_numero) :
        print(f"Hissin kerros on {self.tämän_hetkinen_kerros}")
        while self.tämän_hetkinen_kerros != kerroksen_numero :
            if self.tämän_hetkinen_kerros < kerroksen_numero :
                self.kerros_ylös()
            elif self.tämän_hetkinen_kerros > kerroksen_numero :
                self.kerros_alas()

        return

h = Hissi(1, 5)


h.siirrä(5)
h.siirrä(1)
