     ______   ______     ______     ______   __  __     __   __     ______    
    /\  ___\ /\  __ \   /\  == \   /\__  _\ /\ \/\ \   /\ "-.\ \   /\  __ \   
    \ \  __\ \ \ \/\ \  \ \  __<   \/_/\ \/ \ \ \_\ \  \ \ \-.  \  \ \  __ \  
     \ \_\    \ \_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\\"\_\  \ \_\ \_\ 
      \/_/     \/_____/   \/_/ /_/     \/_/   \/_____/   \/_/ \/_/   \/_/\/_/ 


Le nom du programme vient de Fortuna, la déesse romaine de la chance et de la fortune.

**Objectif :**

L'objectif de ce programme est de permettre à l'utilisateur de jouer au jeu du

"DEVINE LE NOMBRE". Un nombre devra donc être tiré au sort et le joueur devra

deviner ce nombre en une quantité de tentatives fixée. Le seul retour qu'il aura, sera

que son nombre est trop petit ou trop grand.

--------------------------------------------------------------------------------------------------------------------------------

**Fonctionnalités du programme :**

- jouer au jeu sans relancer le programme
- difficultés ajustable
- score calculé en fonction de cette dernière
- affichage de citations au démarrage
- menu
- affichage des règles grâce au menu
- statistiques de jeu grâce au menu
- sortie du jeu grâce au menu

--------------------------------------------------------------------------------------------------------------------------------

**Étapes de création du programme :**

1. Création d'une boucle principale qui appellera les autres fonctions et permettra de jouer indéfiniment (elle est dans le fichier principal, "fortuna.py" )
2. Création de la fonction pour le choix de la difficulté (elle renvoie le nombre de tentatives que le joueur possédera, "difficulty()" )
3. Création du programme permettant de jouer une partie en prenant en compte la difficulté ( "game()" )
4. Rajout de la vérification de la validité des nombres entrés pour les tentatives sans l'arrêt du programme ( "TestNombre.py", "verification()" )
5. Création d'une fonction donnant les règles du jeu ( "rule()" )
6. Création d'un menu pour sortir du jeu, démarrer une partie, lire les règles, ou regarder ses statistiques de jeu (ce dernier n'est pas encore implémenté) dans la boucle principale
7. Rajout des statistiques accessible grâce au menu
8. Rajout de proverbes/citations sur la fortune au démarrage
9. Message dans la console en couleur grâce aux ANSI escape codes (exemple : "\033[0;37;40m" pour un texte normal)
10. Ajout de détails, correction de bugs (exemple : impossibilité de regarder ses stats avant d'avoir fait une partie, une image qui permet de montrer le programme "exemple.png", juste en dessous)

**Difficultés rencontrées :**

- Compréhension des consignes pour la fonction "verification()" dans "TestNombre.py", solution : réfléchir
- Trouver des citations, solution : perdre du temps (google)
- import depuis un dossier, solution : "modules.lemodule" (rajouter un " . " pas un " / ")

[alt text](https://github.com/Thorvicnet/JeuDuDevineLeNombre/blob/3768c9c9bcac8f6036c3bf98b04ed0eaaee9987b/exemple.png)
