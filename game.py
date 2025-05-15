import pygame
from spieler import Spieler
from spielfeld import Spielfeld

# Konstanten
GELB = (255, 255, 0)
GRUEN = (0, 255, 0)
ROT = (255, 0, 0)
SCHWARZ = (0,0,0)

# Spielfeld
spielfeld = [
    (4, 0), (5, 0), (6, 0),
    (4, 1), (6, 1),
    (4, 2), (6, 2),
    (4, 3), (6, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4),
    (0, 5), (10, 5),
    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6),
    (4, 7), (6, 7),
    (4, 8), (6, 8),
    (4, 9), (6, 9),
    (4, 10), (5, 10), (6, 10)
]

farben = {
    "gelb": GELB,
    "gruen": GRUEN,
    "rot": ROT,
    "schwarz": SCHWARZ
}


# Pygame initialisieren
pygame.init()

# Fenster öffnen
screen = pygame.display.set_mode((900, 720))

# Titel setzen
pygame.display.set_caption("Mensch ärgere Dich nicht!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Spielfeld weiß darstellen
    screen.fill((255, 255, 255))

    # Fenstergröße abfragen, damit das Spielfeld responsive ist
    width = screen.get_width()
    height = screen.get_height()

    start = {
        "gelb": (0, 4),
        "gruen": (6, 0),
        "rot": (10, 6),
        "schwarz": (4, 10) 
    }

    figuren = {
        "gelb": [(0, 0), (1, 0), (0, 1), (1, 1)],
        "gruen": [(9, 0), (10, 0), (9, 1), (10, 1)],
        "rot": [(9, 9), (10, 9), (9, 10), (10, 10)],
        "schwarz": [(0, 9), (1, 9), (0, 10), (1, 10)]
    }

    zielfelder = {
        "gelb": [(1, 5), (2, 5), (3, 5), (4, 5)],
        "gruen": [(5, 1), (5, 2), (5, 3), (5, 4)],
        "rot": [(6, 5), (7, 5), (8, 5), (9, 5)],
        "schwarz": [(5, 6), (5, 7), (5, 8), (5, 9)]
    }

    # Spielfeld zeichnen
    feldgroesse = 50
    felder = Spielfeld()
    for feld in spielfeld:
        felder.feld_hinzufügen(x, y, (0,0,0))

    # for feld in spielfeld:
    #     x, y = feld
    #     pygame.draw.ellipse(screen, (0,0,0), [x * feldgroesse, y * feldgroesse, feldgroesse, feldgroesse], 1)

    # Startfelder zeichnen
    for key in figuren:
        for feld in figuren[key]:
            x, y = feld
            pygame.draw.ellipse(screen, farben[key], [x * feldgroesse, y * feldgroesse, feldgroesse, feldgroesse], 0)


     # Zielfelder zeichnen
    for key in zielfelder:
        for feld in zielfelder[key]:
            x, y = feld
            pygame.draw.ellipse(screen, farben[key], [x * feldgroesse, y * feldgroesse, feldgroesse, feldgroesse], 0)

    # Spielfeld aktualisieren
    pygame.display.flip()