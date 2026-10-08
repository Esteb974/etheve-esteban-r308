# ============================================================
# TP1 - Partie B : Devine le nombre
# ============================================================

import random

# Choisit un nombre entre 1 et 100
nombre_secret = random.randint(1, 100)

# Nombre maximum d'essais
max_essais = 10

# Compteur d'essais
essais = 0

print("Devine le nombre entre 1 et 100 !")

# Boucle du jeu
while essais < max_essais:

    # Demande un nombre au joueur
    proposition = int(input("Entre un nombre : "))

    # Ajoute un essai
    essais = essais + 1

    # Vérifie la proposition
    if proposition < nombre_secret:
        print("Trop petit")

    elif proposition > nombre_secret:
        print("Trop grand")

    else:
        print("Gagné !")
        print("Nombre d'essais :", essais)
        break

# Si le joueur n'a pas trouvé
if essais == max_essais and proposition != nombre_secret:
    print("Perdu !")
    print("Le nombre était :", nombre_secret)