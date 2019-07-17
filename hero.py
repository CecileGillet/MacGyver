from position import Position
from labyrinthe import Labyrinthe

class Hero:

    ''' MacGyver se déplace dans le labyrinthe et ramasse les objets sur son chemin'''

    def __init__(self):
        self.nom = "G"
        self.inventaire = []
        self.mon_labyrinthe = Labyrinthe
    

    def recup_objet(self):
        self.inventaire.append(Labyrinthe)
        print(f'Un objet s\'ajoute dans ton inventaire. Tu as {len(self.inventaire)} objets' )





