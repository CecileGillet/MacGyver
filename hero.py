# from position import Position
# from labyrinthe import Labyrinthe

# class Hero:

#     ''' MacGyver se déplace dans le labyrinthe et ramasse 5 objets sur son chemin'''

#     def __init__(self, lab):
#         self.nom = "MG"
#         self.inventaire = []
#         self.mon_labyrinthe = lab
#         self.position_hero = Labyrinthe(0,0) 
#         self.nouvelle_position = []

#     def deplacement_hero(self):
#         self.nouvelle_position = self.position_hero.deplacement(self.mon_labyrinthe)
#         if self.nouvelle_position in self.mon_labyrinthe:
#             self.position_hero = self.nouvelle_position
#         return self.position_hero

#     def recup_objet(self):
#         self.inventaire.append(Labyrinthe)
#         print(f'Un objet s\'ajoute dans ton inventaire. Tu as {len(self.inventaire)} objets')

#     def total_objet(self):
#         if len(self.inventaire) == 5:
#             print('Tu as gagné !!!')
#         else:
#             print('Perdu ! Retente ta chance.')

    



