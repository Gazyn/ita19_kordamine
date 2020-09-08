class Laulja:
    """klass Laulja
        Klassi omadused: (attributes)
        nimi(str) - laulja nimi (name)
        laulud(list) - laulud (songs)
        albumid(list) - albumid (albums)
    """
    def __init__(self, nimi):
        self.nimi = nimi
        self.laulud = []
        self.albumid = []

    def lisaAlbum(self, album):
        self.albumid.append(album)
        for i in album.laulud:
            self.laulud.append(i)
