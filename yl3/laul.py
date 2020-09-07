class Laul:
    """klass Laul
        Klassi omadused: (attributes)
        pealkiri(str) - laulu pealkiri (title)
        laulja(str) - laulu laulja (artist)
        aasta(int) - laulu aasta (year)
        album(str) - album, kus laul paikeb (album)
    """
    def __init__(self, pealkiri, laulja, aasta, album):
        self.pealkiri = pealkiri
        self.laulja = laulja
        self.aasta = aasta
        self.album = album