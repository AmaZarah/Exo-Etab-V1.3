class Utilisateur:
    def __init__(self, id, identifiant, motDePasse):
        self.__id = id
        self.__identifiant = identifiant
        self.__motDePasse = motDePasse

    def authentication(self,identifiant, motDePasse):
        return True