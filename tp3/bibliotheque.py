from livre import Livre, Utilisateur


# Classe qui gere les livres et les utilisateurs
class Bibliotheque:
    def __init__(self):
        self.livres = {}
        self.utilisateurs = {}

    # Ajouter un livre
    def ajouter_livre(self, livre):
        if livre.titre in self.livres:
            print("Ce livre existe deja.")
            return False
        self.livres[livre.titre] = livre
        return True

    # Ajouter un utilisateur
    def ajouter_utilisateur(self, utilisateur):
        if utilisateur.nom in self.utilisateurs:
            print("Cet utilisateur existe deja.")
            return False
        self.utilisateurs[utilisateur.nom] = utilisateur
        return True

    # Emprunter un livre
    def emprunter(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False
        if titre not in self.livres:
            print("Livre inconnu.")
            return False

        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        if utilisateur.emprunter_livre(livre):
            print("Emprunt effectue.")
            return True

        print("Ce livre est deja emprunte.")
        return False

    # Rendre un livre
    def rendre(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False
        if titre not in self.livres:
            print("Livre inconnu.")
            return False

        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        if utilisateur.rendre_livre(livre):
            print("Livre rendu.")
            return True

        print("Ce livre n'est pas emprunte par cet utilisateur.")
        return False

    # Afficher tous les livres
    def afficher_livres(self):
        if len(self.livres) == 0:
            print("La bibliotheque ne contient aucun livre.")
            return

        print("\n--- Liste des livres ---")
        for livre in self.livres.values():
            livre.afficher()

    # Donner les statistiques de la bibliotheque
    def stats(self):
        total = len(self.livres)
        empruntes = 0
        par_utilisateur = {}

        for utilisateur in self.utilisateurs.values():
            nombre = len(utilisateur.emprunts)
            par_utilisateur[utilisateur.nom] = nombre
            empruntes = empruntes + nombre

        return {
            "total": total,
            "empruntes": empruntes,
            "par_utilisateur": par_utilisateur
        }
