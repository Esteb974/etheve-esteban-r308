import csv
from bibliotheque import Bibliotheque
from livre import Livre, Utilisateur


# Sauvegarder les livres dans un fichier CSV
def sauvegarder(bibliotheque, nom_fichier):
    with open(nom_fichier, "w", newline="", encoding="utf-8") as fichier:
        colonnes = ["titre", "auteur", "annee", "disponible", "emprunteur"]
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()

        for livre in bibliotheque.livres.values():
            writer.writerow({
                "titre": livre.titre,
                "auteur": livre.auteur,
                "annee": livre.annee,
                "disponible": livre.disponible,
                "emprunteur": livre.emprunteur
            })


# Charger les livres depuis le fichier CSV
def charger(nom_fichier):
    bibliotheque = Bibliotheque()

    try:
        with open(nom_fichier, "r", newline="", encoding="utf-8") as fichier:
            lecteur = csv.DictReader(fichier)

            for ligne in lecteur:
                livre = Livre(
                    ligne["titre"],
                    ligne["auteur"],
                    int(ligne["annee"])
                )

                # Si le livre est emprunte, retrouver son utilisateur
                if ligne["disponible"].lower() == "false":
                    nom = ligne["emprunteur"]
                    livre.disponible = False
                    livre.emprunteur = nom

                    if nom not in bibliotheque.utilisateurs:
                        utilisateur = Utilisateur(nom)
                        bibliotheque.ajouter_utilisateur(utilisateur)

                    bibliotheque.utilisateurs[nom].emprunts.append(livre)

                bibliotheque.ajouter_livre(livre)

    except FileNotFoundError:
        print("Aucune sauvegarde trouvee. Une nouvelle bibliotheque est creee.")
    except (ValueError, KeyError):
        print("Le fichier CSV contient des donnees incorrectes.")

    return bibliotheque
