import random
from spielfeld import Spielfeld

class Spieler:
        """"""
        def __init__(self, farbe, spielfeld, startfeld):
            self.figuren_draussen = False
            self.farbe = farbe
            self.spielfeld = spielfeld
            self.startfeld = startfeld

        def wuerfeln(self):
            versuch = 0
            while not self.figuren_draussen and versuch < 3:
                augenzahl = random.randint(1, 6)
                versuch += 1
                if augenzahl == 6:
                    self.figur_draussen_pruefen()
                    self.zug_ausfuehren(self.startfeld)
                    return augenzahl                
            if self.figuren_draussen:
                return random.randint(1, 6)
            return None
            
        def figur_draussen_pruefen(self):
            # if keine figur von diesem Spieler auf dem Feld, dann
            return not self.figuren_draussen

        def zug_ausfuehren(self, position):
            self.spielfeld[position].figur = self.farbe

        def check_gewinner(self):
            pass