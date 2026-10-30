# ============================================================
# TP2 - Partie A : Classe Grille
# ============================================================

class Grille:

    def __init__(self):
        # Cree une grille de 3 lignes et 3 colonnes
        self.cases = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def afficher(self):
        # Affiche les trois lignes de la grille
        for ligne in range(3):
            print(" " + " | ".join(self.cases[ligne]))

            # Affiche une separation entre les lignes
            if ligne < 2:
                print("-----------")

    def jouer(self, x, y, joueur):
        # Verifie que les coordonnees sont dans la grille
        if not isinstance(x, int) or not isinstance(y, int):
            print("Coordonnees invalides.")
            return False

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Cette case est hors de la grille.")
            return False

        # Verifie que le symbole est correct
        if joueur not in ["X", "O"]:
            print("Symbole invalide.")
            return False

        # Verifie que la case est libre
        if self.cases[x][y] != " ":
            print("Cette case est deja occupee.")
            return False

        # Place le symbole dans la case
        self.cases[x][y] = joueur
        return True

    def est_gagnant(self, joueur):
        # Verifie les lignes
        for ligne in self.cases:
            if ligne[0] == joueur and ligne[1] == joueur and ligne[2] == joueur:
                return True

        # Verifie les colonnes
        for colonne in range(3):
            if (self.cases[0][colonne] == joueur
                    and self.cases[1][colonne] == joueur
                    and self.cases[2][colonne] == joueur):
                return True

        # Verifie la diagonale de gauche a droite
        if (self.cases[0][0] == joueur
                and self.cases[1][1] == joueur
                and self.cases[2][2] == joueur):
            return True

        # Verifie la diagonale de droite a gauche
        if (self.cases[0][2] == joueur
                and self.cases[1][1] == joueur
                and self.cases[2][0] == joueur):
            return True

        return False

    def est_plein(self):
        # Retourne False s'il reste au moins une case libre
        for ligne in self.cases:
            for case in ligne:
                if case == " ":
                    return False

        return True


# Petit test de la classe
if __name__ == "__main__":
    grille = Grille()
    grille.jouer(0, 0, "X")
    grille.jouer(0, 1, "O")
    grille.jouer(1, 1, "X")
    grille.afficher()
