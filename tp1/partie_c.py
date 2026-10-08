# ============================================================
# TP1 - Partie C : Gestion des mots
# ============================================================

import random

# Liste des mots
mots = ["python", "reseau", "ordinateur", "programmation"]


# Choisit un mot au hasard
def choisir_mot(liste):
    mot = random.choice(liste)
    return mot.upper()


# Crée le masque du mot
def masque(mot):
    resultat = []

    for lettre in mot:
        resultat.append("_")

    return resultat


# ------------------------------------------------------------
# TESTS

mot = choisir_mot(mots)

print("Mot choisi :", mot)
print("Masque :", masque(mot))