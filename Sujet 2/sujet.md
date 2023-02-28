
# 00Steg

  

> *Communication entrante*
> Bonjour Agent 00Steg, on vient de nous informer que Buonaparte Ignacio Gallia a fait placer une bombe dans le palais du Roi. 
> Nous suspectons son agent sur place de lui avoir envoyé des informations sur la bombe par une communication étrange.

> La communication en question : 
> ![communication](message.png)

> Votre mission, si vous l'acceptez : Déccodez le message transmis et désamorcez la bombe.

  

## Sommaire

- [Consignes](#consignes)

- [Concepts](#concepts)
	
	- [Stéganographie](#stéganographie)
	- [LSB](#lsb)
	- [Binaire](#binaire)

- [A vous de jouer](#a-vous-de-jouer)

	- [Démarrer le projet](#démarrer-le-projet)
	- [Informations complémentaires](#informations-complémentaires)
	- [Tic-Tac](#tic-tac)

  

## Consignes

- Demandez à un Cobra de s'assurer que les librairies requises pour le projet sont installées sur le PC sur lequel vous travaillez

- Si vous avez des questions, pensez à demander de l'aide à votre voisin de droite. Puis de gauche. Demandez enfin à un Cobra (ceux-là ne mordent pas) si vous êtes toujours bloqué(e).

- Vous avez tout à fait le droit d'utiliser internet pour trouver des réponses ou pour vous renseigner.

- Vous avez tout à fait le droit d'utiliser internet pour trouver des réponses ou pour vous renseigner.

- [Cliquez ici](https://www.w3schools.com/python/) pour accéder à la documentation de Python
- [Cliquez ici](https://pillow.readthedocs.io/en/latest/reference/index.html) pour accéder à la documentation de la librairie de manipulation d'image

## Concepts

### Stéganographie

Pour cet exercice, nous allons utiliser une technique cryptographique appelée **stéganographie**. 
Ce procédé consiste à dissimuler des messages ou données à l'intérieur d'un autre fichier de manière à ce qu'elles soient indétectables. L'intérêt de la stéganographie est que seul le destinataire du message sait qu'il y a un message caché.
La stéganographie peut prendre plusieurs formes et utiliser plusieurs méthodes, par exemple un spectrogramme d'un son ou des variations de police de caractères.

### LSB

La méthode de stéganographie que l'on va utiliser ici est appelée *Least Significant Bit* (Bit de poids faible en français). 
Cette méthode se base sur le fait que dans un octet binaire, le dernier et l'avant-dernier bit ne peuvent changer la valeur d'origine qu'entre +3 et -3.
Ainsi pour une valeur allant de 0 à 255, la différence ne sera pas visible à l'oeil nu.
On profite aussi du fait que les pixels ont 4 canaux (Rouge, Vert, Bleu, Alpha) pour y cacher nos caractères 2 bits par canaux dans les bits les moins puissants.

### Binaire

Le binaire est un système de numération utilisé en informatique pour représenter des données. Il utilise uniquement les chiffres 0 et 1 pour compter et se base sur les puissances de 2.

Pour convertir un nombre de décimal vers le binaire on fait des divisions euclidiennes par 2 successives en stockant le reste de la division tant que le résultat de la division est différent de 0.

Par exemple, pour convertir le nombre décimal 13 en binaire :

1.  13 ÷ 2 = 6 reste 1
2.  6 ÷ 2 = 3 reste 0
3.  3 ÷ 2 = 1 reste 1
4.  1 ÷ 2 = 0 reste 1

Le nombre binaire équivalent est donc 1101.

Pour convertir un nombre binaire en décimal, on lit les bits de droite à gauche en multipliant la valeur du bit par 2 à la puissance de l'indice du bit.

Par exemple, pour convertir 1101 en décimal :

1. 1 \* 2³ + 1 \* 2² + 0 \* 2¹ + 1 \* 2⁰
2. 8 + 4 + 0 + 1
3. 13

On retrouve bien notre équivalence 13 = 1101.


## A vous de jouer

  

### Démarrer le projet

  

Pour exécuter le projet, il vous suffit de cliquer sur le bouton "*Run*" en haut à droite de votre fenêtre VSCode, si vous n'y arrivez pas, n'hésitez pas à appeler un Cobra.

  

### Informations complémentaires

  

Pour compléter le programme, vous devrez écrire du code aux endroits où vous pouvez voir écrit :

```python

# ...

```

Le code à écrire sur ces lignes vous est indiqué dans les commentaires au-dessus des lignes.

Le nombre de lignes "`#...`" ne représente pas nécessairement le nombre exact de lignes que vous devez ajouter.

Les lignes que vous devez ajouter peuvent contenir des structures de contrôle, prêtez donc attention à l'indentation.

  

### Tic-Tac

  

Tout d'abord, la fonction principale : `main()`

Cette fonction va permettre de lancer le décodage et/ou l'encodage de message dans les images.

Elle va donc charger l'image, appeler les fonctions de décodage et/ou encodage et ensuite fermer les fichiers d'image.

  

[*Documentation PIL*](https://pillow.readthedocs.io/en/latest/reference/index.html)

---

La fonction de conversion de nombres décimaux vers le binaire : `dec_to_bin(dec)`

Cette fonction sert à convertir des nombre décimaux en binaire sous forme de liste.  

[*Tableaux*](https://www.w3schools.com/python/python_lists.asp)

[*Boucles while*](https://www.w3schools.com/python/python_while_loops.asp)

[*Opérateurs mathématiques*](https://www.w3schools.com/python/python_operators.asp)

---  

La fonction de conversion des nombres binaires en décimal : `bin_to_dec(bin_valeur)`

Cette fonction sert à convertir des nombres en binaire en nombres décimaux.


[*Tableaux*](https://www.w3schools.com/python/python_lists.asp)

[*Boucles for*](https://www.w3schools.com/python/python_while_loops.asp)

[*Opérateurs mathématiques*](https://www.w3schools.com/python/python_operators.asp)
  
---

La fonction pour charger les images:  `charger_image(nom)`

Cette fonction permet d'ouvrir un fichier d'image.

[*Documentation PIL*](https://pillow.readthedocs.io/en/latest/reference/index.html)

---

La fonction qui modifie un pixel: `changer_pixel(pixel, valeur)`

Cette fonction va prendre en argument le tuple RGBA d'un pixel et la valeur à encoder dans le pixel par méthode de LSB et renvoi un nouveau tuple avec la valeur encodée.

[*Tableaux*](https://www.w3schools.com/python/python_lists.asp)

---

La fonction qui lit une valeur encodée:
`lire_pixel(pixel)`

Cette fonction va prendre le tuple RGBA d'un pixel et renvoyer la valeur encodée à l'intérieur par méthode de LSB.

[*Tableaux*](https://www.w3schools.com/python/python_lists.asp)

---

La fonction d'encodage : `encoder_message(message, image, nom_sortie)`

Cette fonction va faire le travail principal d'encodage d'un message dans une image. 
Elle prend en argument le message à encoder, l'image dans laquelle écrire et le nom du fichier dans lequel enregistrer l'image.

[*Tableaux*](https://www.w3schools.com/python/python_lists.asp)

[*Boucles for*](https://www.w3schools.com/python/python_while_loops.asp)

[*Documentation PIL*](https://pillow.readthedocs.io/en/latest/reference/index.html)

---

La fonction de décodage: `décoder_message(image)`

Cette fonction va faire le travail principal de décodage de message caché dans une image.
Elle prend en argument l'image dans laquelle elle va lire le message.

[*Tableaux*](https://www.w3schools.com/python/python_lists.asp)

[*Boucles for*](https://www.w3schools.com/python/python_while_loops.asp)

## Félicitations

  

Si vous en êtes arrivé là et que vous avez décodé le message caché dans l'image, bravo ! Vous pouvez à présent aller désamorcer la bombe avant qu'elle n'explose. 
Félicitations Agent 00Steg, vous savez maintenant utiliser des méthodes de communication cachées, ça fait toujours bien sur un CV.
