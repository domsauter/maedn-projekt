class Feld:
    """"""
    def __init__(self, position, farbe=None):
        self.position = position
        self.position = farbe
        self.figur = None


class Spielfeld:
    """"""
    def __init__(self):
        self.felder = {}

    def feld_hinzufügen(self, x, y, farbe=None):
        self.felder[(x, y)] = Feld((x, y), farbe)

    