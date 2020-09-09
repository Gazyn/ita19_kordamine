class Album:
    """klass Album
        Klassi omadused: (attributes)
        nimi(str) - albumi pealkiri (title)
        aasta(int) - albumi väljastusaasta (year)
        laulja(str) - albumi laulja (artist)
        laulud(list) - albumi laulud (songs)
    """
    def __init__(self, nimi, aasta, laulja):
        self.nimi = nimi
        self.aasta = aasta
        self.laulja = laulja
        self.laulud = []

    def lisaLaul(self, laul):
        self.laulud.append(laul)