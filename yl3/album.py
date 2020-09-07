class Album:
    """klass Album
        Klassi omadused: (attributes)
        pealkiri(str) - albumi pealkiri (title)
        aasta(int) - albumi väljastusaasta (year)
        laulja(str) - albumi laulja (artist)
        laulud(list) - albumi laulud (songs)
    """
    def __init__(self, pealkiri, aasta, laulja):
        self.pealkiri = pealkiri
        self.aasta = aasta
        self.laulja = laulja
        self.laulud = []

    def lisaLaul(self, laul):
        self.laulud.append(laul)