# Tic-Tac... Toe

> Un savant fou vous a kidnappé et enfermé dans une pièce sombre qui semble vide à part pour un ordinateur. Il vous informe qu'une bombe est placée dans le bâtiment et qu'elle va exploser bientôt. Il vous laisse cependant une chance de vous en sortir si vous arrivez à compléter le programme informatique laissé sur l'ordinateur.

## Sommaire
- [Consignes](#consignes)
- [A vous de jouer](#a-vous-de-jouer)
	- [Démarrer le projet](#démarrer-le-projet)
	- [Informations complémentaires](#informations-complémentaires)
	- [Tic-Tac](#tic-tac)

## Consignes
- Si vous avez des questions, pensez à demander de l'aide à votre voisin de droite. Puis de gauche. Demandez enfin à un Cobra (ceux-là ne mordent pas) si vous êtes toujours bloqué(e).
- Vous avez tout à fait le droit d'utiliser internet pour trouver des réponses ou pour vous renseigner.
- Vous avez tout à fait le droit d'utiliser internet pour trouver des réponses ou pour vous renseigner.
- [Cliquez ici](https://www.w3schools.com/python/) pour accéder à la documentation de Python

## A vous de jouer

### Démarrer le projet

Pour exécuter le projet, il vous suffit de cliquer sur le bouton "*Run*" en haut à droite de votre fenêtre VSCode, si vous n'y arrivez pas, n'hésitez pas à appeler un Cobra

### Informations complémentaires

Pour compléter le programme, vous devrez écrire du code aux endroits où vous pouvez voir écrit :
```python
# ...
```
Le code à écrire sur ces lignes vous est indiqué dans les commentaires au-dessus des lignes.
Le nombre de lignes "`#...`" ne représente pas nécessairement le nombre exact de lignes que  vous devez ajouter.
Les lignes que vous devez ajouter peuvent contenir des structures de contrôle, prêtez donc attention à l'indentation.

### Tic-Tac

Tout d'abord, la fonction principale : `main()` 

Cette fonction va permettre de faire tourner le jeu entier. 
Elle met donc en place une boucle qui va s'effectuer tant que la partie n'est pas finie et elle va donc inviter les joueurs à saisir les cases où ils veulent jouer et à la fin de la partie elle va afficher le nom du gagnant.

[*Conditions*](https://www.w3schools.com/python/python_conditions.asp)

La fonction d'affichage de la carte : `afficher_carte()`

Cette fonction va permettre d'afficher la carte actuelle.
(Pensez à afficher le numéro de la ligne actuellement affichée pour que ça soit plus facile de cibler les cases.)

[*Tableaux*](https://www.w3schools.com/python/python_lists.asp)
[*Boucles for*](https://www.w3schools.com/python/python_for_loops.asp)

La fonction de fin : `partie_finie(carte)`

Cette fonction va vérifier si la partie est finie ou non.
On regarde donc si un joueur a complété une ligne, une colonne ou une diagonale, ensuite, on vérifie s'il reste des cases jouables ou non pour repérer les matchs nuls.

---

## Félicitations

Si vous en êtes arrivé là, brave vous avez réussi à compléter le programme du savant fou, il vous révèlera finalement qu'il cherchait juste quelqu'un capable de réparer son jeu car il n'en était pas capable seul et il vous propose à présent de faire une partie contre lui. 
