class Position :
    '''Classe qui gére toutes les positions dans le labyrinthe x étant le numéro de ligne et y le numéro de colonne'''

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def bouger_bas(self):
        return Position(self.x+1, self.y)

    def bouger_haut(self):
        return Position(self.x-1, self.y)

    def bouger_droit(self):
        return Position(self.x, self.y+1)
    
    def bouger_gauche(self):
        return Position(self.x, self.y-1)

    def __add__(self, direction):
        if direction == "Z":
            return self.bouger_haut()
        elif direction == "S":
            return self.bouger_bas()
        elif direction == "Q":
            return self.bouger_gauche()
        elif direction == "D":
            return self.bouger_droit()
        else: 
            print('Les touches pour se déplacer sont Z Q S D')

    def __eq__(self,comparaison):
        if self.x == comparaison.x and self.y == comparaison.y:
            return True
        else:
            False
