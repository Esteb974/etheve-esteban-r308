from livre import Livre, Utilisateur
from bibliotheque import Bibliotheque
from persistance import sauvegarder, charger


FICHIER = "tp3/bibliotheque.csv"

# Charger les donnees au lancement
bibliotheque = charger(FICHIER)


# Afficher le menu
def afficher_menu():
    print("\n===== GESTION DE LA BIBLIOTHEQUE =====")
    print("1. Ajouter un livre")
    print("2. Ajouter un utilisateur")
    print("3. Emprunter un livre")
    print("4. Rendre un livre")
    print("5. Afficher les livres")
    print("6. Quitter et sauvegarder")
    print("7. Afficher les statistiques")


# Boucle principale du programme
continuer = True

while continuer:
    afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre du livre : ")
        auteur = input("Auteur : ")

        try:
            annee = int(input("Annee : "))
            livre = Livre(titre, auteur, annee)
            if bibliotheque.ajouter_livre(livre):
                print("Livre ajoute.")
        except ValueError:
            print("L'annee doit etre un nombre.")

    elif choix == "2":
        nom = input("Nom de l'utilisateur : ")
        if nom.strip() == "":
            print("Le nom ne peut pas etre vide.")
        else:
            utilisateur = Utilisateur(nom)
            if bibliotheque.ajouter_utilisateur(utilisateur):
                print("Utilisateur ajoute.")

    elif choix == "3":
        nom = input("Nom de l'utilisateur : ")
        titre = input("Titre du livre : ")
        bibliotheque.emprunter(nom, titre)

    elif choix == "4":
        nom = input("Nom de l'utilisateur : ")
        titre = input("Titre du livre : ")
        bibliotheque.rendre(nom, titre)

    elif choix == "5":
        bibliotheque.afficher_livres()

    elif choix == "6":
        sauvegarder(bibliotheque, FICHIER)
        print("Donnees sauvegardees. Au revoir !")
        continuer = False

    elif choix == "7":
        print(bibliotheque.stats())

    else:
        print("Choix invalide. Veuillez choisir entre 1 et 7.")
