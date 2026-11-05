# Classe qui represente un livre
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        self.emprunteur = None

    # Afficher les informations du livre
    def afficher(self):
        if self.disponible:
            etat = "Disponible"
        else:
            etat = "Emprunte par " + str(self.emprunteur)
        print(self.titre, "-", self.auteur, "-", self.annee, "-", etat)

    # Emprunter le livre s'il est disponible
    def emprunter(self, nom):
        if self.disponible:
            self.disponible = False
            self.emprunteur = nom
            return True
        return False

    # Rendre le livre
    def rendre(self, nom=None):
        if not self.disponible:
            if nom is not None and nom != self.emprunteur:
                return False
            self.disponible = True
            self.emprunteur = None
            return True
        return False


# Classe qui represente un utilisateur
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []

    # Ajouter un livre a ses emprunts
    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True
        return False

    # Retirer un livre de ses emprunts
    def rendre_livre(self, livre):
        if livre in self.emprunts and livre.rendre(self.nom):
            self.emprunts.remove(livre)
            return True
        return False

    # Afficher ses emprunts
    def afficher_emprunts(self):
        if len(self.emprunts) == 0:
            print(self.nom, "n'a aucun emprunt.")
        else:
            print("Emprunts de", self.nom, ":")
            for livre in self.emprunts:
                print("-", livre.titre)
