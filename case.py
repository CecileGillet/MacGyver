from position import Position

class Case:

    def __init__(self, position):
        self.position = position
        self.entree = False
        self.sortie = False
       
    def nouvelle_case(self, coordonnee):
        new_case = Case()        

