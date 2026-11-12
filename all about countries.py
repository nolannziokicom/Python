class Norway:
    def capital(self):
        print("The capital of Norway is Oslo")
    def language(self):
        print("Norweigans speak in english")
    def type(self):
        print("This is an actively developing country")

class Kenya:
    def capital(self):
        print("Kenya's capital is Nairobi")
    def language(self):
        print("Kenya speaks in swahili and english with many cultural languages")
    def type(self):
        print("Kenya is an actively developing country")

Norw=Norway()

Keny=Kenya()

for country in (Norw,Keny):
    country.capital()
    country.language()
    country.type()



