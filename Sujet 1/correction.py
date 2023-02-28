#!/usr/bin/env python3

from typing import List


# On défini la carte du morpion avec toutes les cases vides
carte: List[List[str]] = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Fonction pour vérifier si un joueur a gagné : 0 si personne, 1 si joueur 1, 2 si joueur 2, 3 si match nul
def partie_finie(carte: List[List[str]]) -> int:
    # On vérifie les lignes
    for line in carte:
        if line[0] == line[1] == line[2] != " ":
            if (line[0] == "X"):
                return 1
            else:
                return 2

    # On vérifie les colonnes
    for i in range(3):
        if carte[0][i] == carte[1][i] == carte[2][i] != " ":
            if (carte[0][i] == "X"):
                return 1
            else:
                return 2

    # On vérifie les diagonales
    if carte[0][0] == carte[1][1] == carte[2][2] != " ":
        if (carte[0][0] == "X"):
            return 1
        else:
            return 2
    if carte[0][2] == carte[1][1] == carte[2][0] != " ":
        if (carte[0][2] == "X"):
            return 1
        else:
            return 2

    # On vérifie si il y a encore des cases vides
    for line in carte:
        for case in line:
            if case == " ":
                return 0
    return 3


# Fonction pour afficher la carte
def afficher_carte(carte: List[List[str]]) -> None:
    # On affiche les numéros de colonnes
    print("   1   2   3")

    # On affiche les lignes
    for i in range(3):
        print(f"{i+1}  {carte[i][0]} | {carte[i][1]} | {carte[i][2]}")

        # On affiche les séparateurs si la ligne n'est pas la dernière
        if i != 2:
            print("  ---+---+---")


def tour_joueur(carte: List[List[str]], joueur: int) -> None:
    # On demande la case à jouer
    while True:
        case = input(
            f"Joueur {joueur}, quelle case voulez-vous jouer ? (colonne ligne, ex : 1 2)"
        ).split(" ")
        if len(case) != 2:
            continue
        try:
            x = int(case[0]) - 1
            y = int(case[1]) - 1
        except ValueError:
            continue
        if x < 0 or x > 3 or y < 0 or y > 3:
            continue
        if carte[y][x] != " ":
            continue
        break

    # On joue la case
    if (joueur == 1):
        carte[y][x] = "X"
    else:
        carte[y][x] = "O"

    # On affiche la carte
    afficher_carte(carte)


def main() -> int:
    # On défini la condition d'arrêt de la fin de la partie sur 0 (pas fini)
    fini = 0

    # On demande le nom des joueurs
    joueur1 = input("Nom du joueur 1 : ")
    joueur2 = input("Nom du joueur 2 : ")

    # On défini le joueur qui commence
    joueur = 1

    # On affiche la carte
    afficher_carte(carte)

    # On boucle tant que la partie n'est pas finie
    while fini == 0:
        # On demande la case à jouer
        tour_joueur(carte, joueur)

        # On change de joueur
        if (joueur == 1):
            joueur = 2
        else:
            joueur = 1
            
        fini = partie_finie(carte)

    # On affiche le résultat
    if fini == 1:
        print(f"Le joueur {joueur1} a gagné !")
    elif fini == 2:
        print(f"Le joueur {joueur2} a gagné !")
    else:
        print("Match nul !")

    return 0


if __name__ == "__main__":
    main()
