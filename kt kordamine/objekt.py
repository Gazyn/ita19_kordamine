class NegatiivsedVäärtused(Exception):
    pass

class Inimene:
    def __init__(self, kaal, pikkus):
        if kaal<0 or pikkus<0:
            raise NegatiivsedVäärtused

        self.kaal = kaal
        self.pikkus = pikkus
    def kehamassiindeks(self):
        return self.kaal/(self.pikkus/100)**2

try:
    mari = Inimene(60, 150)
    print(mari.kehamassiindeks())
except NegatiivsedVäärtused:
    print("Sisesta positiivsed väärtused")
