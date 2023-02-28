#!/usr/bin/env python3

from PIL import Image


# Fonction qui convertit un nombre décimal en binaire sous forme de liste
def dec_to_bin(dec: int) -> list:
    # On crée une liste vide
    bin_valeur = []

    # Tant que le nombre décimal est supérieur à 0
    # on ajoute le reste de la division par 2 à la liste (0 ou 1)
    # puis on divise le nombre décimal par 2 (division entière)
    
    # ...
    # ...

    # On ajoute des 0 à la fin de la liste jusqu'à ce qu'elle fasse 8 éléments

    # ...
    # ...

    # On retourne la liste pour la retrouver dans le bon ordre

    # ...

    # On renvoi la liste obtenue
    return bin_valeur

# Fonction qui convertit un nombre binaire sous forme de liste en décimal
def bin_to_dec(bin_valeur: list) -> int:

    # On retourne la liste pour la retrouver dans le bon ordre
    
    # ...

    # On initialise la variable qui contiendra le nombre décimal
    dec = 0

    # On parcourt la liste en entier et on ajoute à la variable dec la puissance de 2 correspondante
    
    # ...
    # ...

    # On renvoi la valeur obtenue
    return dec

# Fonction qui permet de charger une image et la convertir en RGBA
def charger_image(nom: str) -> Image:
    # On charger l'image et on la converti en RGBA
    
    # ...
    # ...

    # On retourne la variable contenant l'image
    return ...

# Fonction qui permet d'encoder une valeur dans un pixel
def changer_pixel(pixel: tuple, valeur: int) -> tuple:
    # On convertit la valeur en binaire
    
    # ...

    # On décompose les valeurs du tuple du pixel
    rouge, vert, bleu, alpha = pixel

    # On convertit les valeurs du pixel en binaire
    bin_rouge = dec_to_bin(...)
    bin_vert = ...
    # ...
    # ...

    # On modifie les 2 derniers bits de chaque couleur
    bin_rouge[6] = bin_valeur[0]
    bin_rouge[7] = bin_valeur[...]
    bin_vert[6] = ...
    # ...
    # ...

    # On convertit les valeurs binaires en décimal
    rouge = bin_to_dec(...)
    vert = ...
    # ...
    # ...

    # On renvoi le pixel modifié sous forme de tuple
    return (rouge, vert, bleu, alpha)

# Fonction qui permet de décoder une valeur d'un pixel
def lire_pixel(pixel: tuple) -> int:
    # On décompose les valeurs du tuple du pixel
    rouge, vert, bleu, alpha = pixel

    # On convertit les valeurs du pixel en binaire
    bin_rouge = dec_to_bin(...)
    bin_vert = ...
    # ...
    # ...

    # on constitue un tableau contenant les 2 derniers bits de chaque couleur
    bin_valeur = [
        bin_rouge[6],
        bin_rouge[...],
        # ...
        # ...
    ]

    # On renvoi la valeur décimale du pixel
    return # ...

# Fonction qui permet d'encoder un message dans une image
def encoder_message(message: str, image: Image, nom_sortie: str) -> None:
    # On récupère la taille du message
    
    # ...

    # On récupère la liste des pixels de l'image qui sont des tuples (R, G, B, A)
    pixels_image = list(image.getdata())
    
    # On modifie le premier pixel de l'image pour y stocker la taille du message
    
    # ...

    # Pour chaque caractère du message, on modifie le pixel correspondant en y stockant le code ASCII du caractère

    # ...
    # ...

    # On remplace la liste des pixels de l'image par la nouvelle liste
    image.putdata(...)

    # On sauvegarde l'image
    image.save(...)

# Fonction qui permet de décoder un message d'une image
def decoder_message(image: Image) -> str:
    # On récupère la liste des pixels de l'image qui sont des tuples (R, G, B, A)
    pixels_image = list(image.getdata())

    # On lit le premier pixel pour récupérer la taille du message

    # ...

    # On initialise la variable qui contiendra le message
    message = ""

    # On parcourt les pixels de l'image pour récupérer le code ASCII de chaque caractère du message
    # On converti le code ASCII en caractère et on l'ajoute à la variable message
    
    # ...
    # ...

    # On renvoi le message décodé
    return ...

def main() -> int:
    # Bloc de code pour tester le décodage d'un message dans une image
    
    # ...
    # ...

    # Bloc de code pour tester l'encodage d'un message dans une image (bonus)
    
    # ...
    # ...

    return 0


if __name__ == "__main__":
    main()