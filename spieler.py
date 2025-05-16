import random

class Spieler:
        """"""
        def __init__(self):
            self.figuren_draussen = False

        def wuerfeln(self):
            versuch = 0
            while not self.figuren_draussen and versuch < 3:
                augenzahl = random.randint(1, 6)
                versuch += 1
                if augenzahl == 6:
                    self.figur_draussen_pruefen()
                    return augenzahl                
            if self.figuren_draussen:
                return random.randint(1, 6)
                self.figur_draussen_pruefen()
            return None
            
        def figur_draussen_pruefen(self):
            # if keine figur von diesem Spieler auf dem Feld, dann
            return not self.figuren_draussen

        def zug_ausfuehren(self):
            pass

        def check_gewinner(self):
            pass