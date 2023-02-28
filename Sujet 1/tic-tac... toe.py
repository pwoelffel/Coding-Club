#!/usr/bin/env python3

from typing import List

# Fonction pour vérifier si un joueur a gagné : 0 si personne, 1 si joueur 1, 2 si joueur 2, 3 si match nul
def partie_finie(carte: List[List[str]]) -> int:
    # On vérifie chaque ligne pour voir si les 3 cases sont identiques
    
    #...
    #...

    # On vérifie les colonnes pour voir si les 3 cases sont identiques

    #...
    #...

    # On vérifie les diagonales pour voir si les 3 cases sont identiques
    # D'abord la diagonale de gauche à droite
    # Ensuite la diagonale de droite à gauche

    #...
    #...

    # On vérifie si il y a encore des cases vides pour le match nul
    # Pour chaque case, est-ce qu'elle est vide ?

    #...
    #...

    # Pas de gagnants et encore des cases jouables 
    return ...


# Fonction pour afficher la carte
def afficher_carte(carte: List[List[str]]) -> None:
    # On affiche les numéros de colonnes
    print("   1   2   3")

    # On affiche les lignes
    for i in range(3):
        #...
        
        # On affiche les séparateurs si la ligne n'est pas la dernière
        #...
        print("  ---+---+---")

# Fonction pour faire jouer un joueur
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

    # On joue la case : Placer le X ou le O sur la case choisie par le joueur

    # On affiche la carte
    afficher_carte(carte)


def main() -> int:
    # On défini la carte du morpion avec toutes les cases vides
    carte: List[List[str]] = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

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
        # On démarre le tour du joueur

        #...

        # On change de joueur
        # 1 pour le joueur 1, 2 pour le joueur 2

        #...

        # On vérifie si la partie est finie ou non

        #...

    # On affiche le résultat
    # Message différent selon le gagnant ou en cas de match nul
    
    #...
    #...

    # return 0 de fin de fonction, ne pas toucher
    return 0


if __name__ == "__main__":
    main()
