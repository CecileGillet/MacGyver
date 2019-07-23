class Position:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def en_bas(self, laby):
        self.x = self.x + 1

    def en_haut(self, laby):
        self.x = self.x - 1

    def a_droite(self, laby):
        self.y = self.y + 1
    
    def a_gauche(self, laby):
        self.y = self.y - 1
    
    # def deplacement(self, direction, laby):
    #     if direction == 'Z':
    #         return self.en_haut(laby)
    #     elif direction == 'S':
    #         return self.en_bas(laby)
    #     elif direction == 'Q':
    #         return self.a_gauche(laby)
    #     elif direction == 'D':
    #         return self.a_droite(laby)