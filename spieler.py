import random

class Player:
        """"""
        def __init__(self):
            pass

        def wuerfeln(self):
            versuch = 0
            while not self.figuren_draussen and versuch < 3:
                augenzahl = random.randint(1,6)
                versuch += 1
                if augenzahl == 6:
                    return augenzahl                
            if self.figuren_draussen:
                return random.randint(1, 6)
            return None
            
        def figuren_draussen(self):
            return False