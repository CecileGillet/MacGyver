class Players:
    '''Classe du joueur'''
    
    def __init__(self, pseudo):
        self.pseudo = pseudo

    def get_pseudo(self):
        return self.pseudo

joueur = Players("MG")
print(joueur.get_pseudo())
    # def get_pseudo(self):
    #     return self.pseudo

    # def catch_object(self, objet):
    #     objet.append()
    #     return self.inventaire

# mac = Players("MG")
# print(mac.get_pseudo())