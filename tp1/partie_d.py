# ============================================================
# TP1 - Partie D : Jeu du pendu
# ============================================================

import random

# Liste des mots
mots = ["PYTHON", "RESEAU", "ORDINATEUR", "PROGRAMMATION"]

# Choisit un mot
mot = random.choice(mots)

# Crée le masque du mot
masque = ["_"] * len(mot)

# Lettres déjà proposées
lettres_proposees = []

# Nombre d'erreurs
erreurs = 0

# Nombre maximum d'erreurs
max_erreurs = 7

print("=== JEU DU PENDU ===")


# Boucle principale du jeu
while erreurs < max_erreurs and "_" in masque:

    print()
    print("Mot :", " ".join(masque))
    print("Erreurs :", erreurs, "/", max_erreurs)
    print("Lettres proposées :", lettres_proposees)

    # Demande une lettre
    lettre = input("Propose une lettre : ").upper()

    # Vérifie que l'utilisateur entre une seule lettre
    if len(lettre) != 1:
        print("Entre une seule lettre.")
        continue

    # Vérifie si la lettre a déjà été proposée
    if lettre in lettres_proposees:
        print("Tu as déjà proposé cette lettre.")
        continue

    # Ajoute la lettre aux lettres proposées
    lettres_proposees.append(lettre)

    # Vérifie si la lettre est dans le mot
    if lettre in mot:

        print("Bonne lettre !")

        # Révèle les positions de la lettre
        for i in range(len(mot)):
            if mot[i] == lettre:
                masque[i] = lettre

    else:

        print("Mauvaise lettre !")
        erreurs = erreurs + 1


# Résultat final
if "_" not in masque:

    print()
    print("Gagné !")
    print("Le mot était :", mot)

else:

    print()
    print("Perdu !")
    print("Le mot était :", mot)