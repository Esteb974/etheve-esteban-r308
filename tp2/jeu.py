# ============================================================
# TP2 - Partie C : Jeu complet du morpion
# ============================================================

from grille import Grille
from joueurs import JoueurHumain, JoueurIA


def choisir_mode():
    # Propose les differents modes de jeu
    print("\nChoisis un mode de jeu :")
    print("1 - Humain contre IA")
    print("2 - Deux joueurs humains")
    print("3 - IA contre IA")

    while True:
        choix = input("Ton choix : ")

        if choix in ["1", "2", "3"]:
            return choix

        print("Choix incorrect. Entre 1, 2 ou 3.")


def lancer_partie(mode):
    # Cree une nouvelle grille
    grille = Grille()

    # Cree les joueurs selon le mode choisi
    if mode == "1":
        joueur_x = JoueurHumain()
        joueur_o = JoueurIA()
    elif mode == "2":
        joueur_x = JoueurHumain()
        joueur_o = JoueurHumain()
    else:
        joueur_x = JoueurIA()
        joueur_o = JoueurIA()

    # Le joueur X commence
    symbole = "X"

    while True:
        grille.afficher()

        # Selectionne le joueur qui doit jouer
        if symbole == "X":
            joueur = joueur_x
        else:
            joueur = joueur_o

        print("\nAu tour de", symbole)

        # Le joueur choisit une case
        x, y = joueur.prochain_coup(grille.cases, symbole)

        # Si le coup est refuse, le meme joueur rejoue
        if not grille.jouer(x, y, symbole):
            continue

        # Affiche la grille apres le coup
        grille.afficher()

        # Verifie si le joueur vient de gagner
        if grille.est_gagnant(symbole):
            print("\nLe joueur", symbole, "a gagne !")
            return symbole

        # Verifie si la grille est pleine
        if grille.est_plein():
            print("\nMatch nul !")
            return "N"

        # Change de joueur
        if symbole == "X":
            symbole = "O"
        else:
            symbole = "X"


# ------------------------------------------------------------
# Lancement du jeu et score sur plusieurs parties

if __name__ == "__main__":
    scores = {"X": 0, "O": 0, "N": 0}
    mode = choisir_mode()

    while True:
        resultat = lancer_partie(mode)
        scores[resultat] = scores[resultat] + 1

        print("\n===== SCORES =====")
        print("Victoires X :", scores["X"])
        print("Victoires O :", scores["O"])
        print("Matchs nuls :", scores["N"])

        rejouer = input("\nFaire une autre partie ? (o/n) : ").lower()

        if rejouer != "o":
            break

    print("\nMerci d'avoir joue !")
