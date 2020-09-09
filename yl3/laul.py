class Laul:
    """klass Laul
        Klassi omadused: (attributes)
        nimi(str) - laulu nimi (title)
        laulja(str) - laulu laulja (artist)
        aasta(int) - laulu aasta (year)
        album(str) - album, kus laul paikeb (album)
    """
    def __init__(self, nimi, laulja, aasta, album):
        self.nimi = nimi
        self.laulja = laulja
        self.aasta = aasta
        self.album = album