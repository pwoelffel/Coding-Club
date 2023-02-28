#!/usr/bin/env python3

from PIL import Image

def dec_to_bin(dec: int) -> list:
    bin_valeur = []
    while dec > 0:
        bin_valeur.append(dec % 2)
        dec //= 2

    while len(bin_valeur) < 8:
        bin_valeur.append(0)
    bin_valeur.reverse()
    return bin_valeur

def bin_to_dec(bin_valeur: list) -> int:
    bin_valeur.reverse()
    dec = 0
    for i in range(len(bin_valeur)):
        dec += bin_valeur[i] * 2**i
    return dec

def charger_image(nom: str) -> Image:
    image = Image.open(nom)
    image = image.convert("RGBA")
    return image

def changer_pixel(pixel: tuple, valeur: int) -> tuple:
    bin_valeur = dec_to_bin(valeur)

    rouge, vert, bleu, alpha = pixel
    bin_rouge = dec_to_bin(rouge)
    bin_vert = dec_to_bin(vert)
    bin_bleu = dec_to_bin(bleu)
    bin_alpha = dec_to_bin(alpha)

    bin_rouge[6] = bin_valeur[0]
    bin_rouge[7] = bin_valeur[1]
    bin_vert[6] = bin_valeur[2]
    bin_vert[7] = bin_valeur[3]
    bin_bleu[6] = bin_valeur[4]
    bin_bleu[7] = bin_valeur[5]
    bin_alpha[6] = bin_valeur[6]
    bin_alpha[7] = bin_valeur[7]

    rouge = bin_to_dec(bin_rouge)
    vert = bin_to_dec(bin_vert)
    bleu = bin_to_dec(bin_bleu)
    alpha = bin_to_dec(bin_alpha)

    return (rouge, vert, bleu, alpha)

def lire_pixel(pixel: tuple) -> int:
    rouge, vert, bleu, alpha = pixel
    bin_rouge = dec_to_bin(rouge)
    bin_vert = dec_to_bin(vert)
    bin_bleu = dec_to_bin(bleu)
    bin_alpha = dec_to_bin(alpha)

    bin_valeur = [
        bin_rouge[6],
        bin_rouge[7],
        bin_vert[6],
        bin_vert[7],
        bin_bleu[6],
        bin_bleu[7],
        bin_alpha[6],
        bin_alpha[7]
    ]

    return bin_to_dec(bin_valeur)

def encoder_message(message: str, image: Image, nom_sortie: str) -> None:
    taille_message = len(message)
    pixels_image = list(image.getdata())
    
    pixels_image[0] = changer_pixel(pixels_image[0], taille_message)

    for i in range(taille_message):
        caractere_code = ord(message[i])
        pixels_image[i+1] = changer_pixel(pixels_image[i+1], caractere_code)

    image.putdata(pixels_image)
    image.save(nom_sortie)

def decoder_message(image: Image) -> str:
    pixels_image = list(image.getdata())
    taille_message = lire_pixel(pixels_image[0])
    message = ""

    for i in range(taille_message):
        caractere_code = lire_pixel(pixels_image[i+1])
        message += chr(caractere_code)

    return message

def main() -> int:
    image = charger_image("résultat.png")
    print(decoder_message(image))
    image.close()

    image = charger_image("message.png")
    encoder_message("Le message est libre ici", image, "resultat.png")
    image.close()
    return 0


if __name__ == "__main__":
    main()