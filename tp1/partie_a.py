# ============================================================
# TP1 - Partie A : Gestion d'un dictionnaire d'étudiants
# ============================================================

# Liste des étudiants avec leurs notes
etudiants = {
    "Alice": 12.0,
    "Bob": 15.0,
    "Claire": 9.5,
    "David": 14.0
}


# ------------------------------------------------------------
# Ajoute un étudiant dans le dictionnaire

def ajouter_etudiant(d, nom, note):
    try:
        # Transforme la note en nombre
        note = float(note)

        # Ajoute l'étudiant
        d[nom] = note

    except ValueError:
        # Affiche une erreur si la note n'est pas un nombre
        print("Erreur : la note doit être un nombre.")


# ------------------------------------------------------------
# Calcule la moyenne de la classe

def moyenne_classe(d):

    # Si le dictionnaire est vide
    if len(d) == 0:
        return 0.0

    somme = 0

    # Additionne toutes les notes
    for nom in d:
        somme = somme + d[nom]

    # Calcule la moyenne
    return somme / len(d)


# ------------------------------------------------------------
# Trouve l'étudiant avec la meilleure note

def meilleur_etudiant(d):

    # Valeurs de départ
    meilleure_note = 0
    meilleur_nom = ""

    # Parcourt les étudiants
    for nom in d:

        # Compare les notes
        if d[nom] > meilleure_note:

            # Enregistre la meilleure note
            meilleure_note = d[nom]

            # Enregistre le nom
            meilleur_nom = nom

    # Retourne le nom et la note
    return (meilleur_nom, meilleure_note)


# ------------------------------------------------------------
# Sauvegarde les étudiants dans un fichier

def sauvegarder_etudiants(d):

    # Ouvre le fichier
    with open("etudiants.txt", "w") as fichier:

        # Écrit chaque étudiant dans le fichier
        for nom in d:
            fichier.write(nom + ":" + str(d[nom]) + "\n")


# ------------------------------------------------------------
# Charge les étudiants depuis le fichier

def charger_etudiants():
    etudiants = {}

    # Ouvre le fichier
    with open("etudiants.txt", "r") as fichier:

        # Parcourt chaque ligne
        for ligne in fichier:
            ligne = ligne.strip()

            # Sépare le nom et la note
            nom, note = ligne.split(":")

            # Transforme la note en nombre
            note = float(note)

            # Ajoute l'étudiant
            etudiants[nom] = note

    return etudiants


# ------------------------------------------------------------
# TESTS

# Ajoute Emma avec une note de 16
ajouter_etudiant(etudiants, "Emma", "16")

# Affiche la moyenne
print("Moyenne de la classe :", moyenne_classe(etudiants))

# Affiche le meilleur étudiant
print("Meilleur étudiant :", meilleur_etudiant(etudiants))

# Affiche tous les étudiants
print("Liste des étudiants :", etudiants)

# Sauvegarde les étudiants
sauvegarder_etudiants(etudiants)

# Recharge les étudiants depuis le fichier
nouveaux_etudiants = charger_etudiants()

# Affiche les étudiants chargés
print(nouveaux_etudiants)