import random
import os

from position import Position
from case import Case


class Objets:

    def __init__(self, name: str, position_objet: position_objet.Position = None):
        self.position_objet = position_objet
        self.name = name
        self.objet = None
        self.position_depart = False
        self.position_arriver = False
        self.list_objet = [1, 2, 3]
        # self.list_objet = []

    def recup_alea_obj(self):
        if self.list_objet:
            random.shuffle(self.list_objet)
        return self.list_objet


    ##### TEST : Mettre img comme objet. 
          
    ##### OBJECTIF : Transformer img en lettre ou chiffre 

    ## DEBUT du code test 

    # def ajout_img_objet(self, liste_images):
    #     liste_images = os.listdir('\ressource')

    #     for x, image in liste_images:
    #         liste_images = image[x]

    #         for liste_images in self.list_objet:
    #             self.list_objet = liste_images
            
    #         return self.list_objet
    

    
    # def ouvrir_ressource(self):
    #     with open("ressource", "r") as dossier_ressource:
    #         for liste_images in enumerate(dossier_ressource):
    #             for x, image in enumerate(image.strip()):

    #                 liste_images = image[x]

    #                 for liste_images in self.list_objet:
    #                     self.list_objet = liste_images
            
    #                 return self.list_objet

    ## FIN du code test


# mettre objet dans case dispo (chemin) via chiffre. Mettre condition pour que les objets n'aille pas sur 'd' et 'a'


#traduire img en lettre
# mettre au hasard 3 obj identique 
# ou 3 obj  meme opération mettre obj case libre (chemin)