# ============================================================
# TP2 - Partie B : Classes des joueurs
# ============================================================

import random


class JoueurHumain:

    def prochain_coup(self, tab, symbole):
        # Demande les coordonnees au joueur
        print("Joueur", symbole)

        try:
            x = int(input("Ligne (0, 1 ou 2) : "))
            y = int(input("Colonne (0, 1 ou 2) : "))
            return (x, y)

        except ValueError:
            # Le joueur doit entrer des nombres
            print("Entre des nombres pour la ligne et la colonne.")
            return (-1, -1)


class JoueurIA:

    def prochain_coup(self, tab, symbole):
        # Cherche toutes les cases qui sont encore libres
        cases_libres = []

        for x in range(3):
            for y in range(3):
                if tab[x][y] == " ":
                    cases_libres.append((x, y))

        # Choisit une case libre au hasard
        if len(cases_libres) > 0:
            return random.choice(cases_libres)

        return (-1, -1)
