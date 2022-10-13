import modules.Fonctions as func
import modules.AsciiArt as ascii
import modules.Citations as citations

# Variables utilisées pour les statistiques
gamesplayed = 0 # nombre de parties jouées
victories = 0 # nombre de victoire
highscore = 0 # meilleur score
streak = 0 # nombre de partie gagné d'affilé en ce moment


ascii.logo()  # Un petit logo pour faire beau
print('by Victor Faucher\n\n')

print(citations.citations()) # Les citations

while True:
    """Boucle principale
    """
    ascii.help()  # Toutes les commandes possibles
    choice = input('> Que voulez-vous faire : ')
    if choice == 'démarrer':
        difficulty = func.difficulty() # Choix de la difficulté
        victory = func.game(difficulty) # On lance une partie, elle renvera True si il y a victoire

        gamesplayed += 1
        if victory: # si il y a victoire on ajoute 1 à la variable
            victories += 1
            streak += 1
            score = 10-difficulty # Calcul du score : f(x) = 10-x
            if highscore < score: # si le score est supérieur au meilleur score il y a record
                print('-'*18 + '\n  NOUVEAU RECORD  \n' + ' '*9 + str(score) + '\n' + '-'*18)
                highscore = score
        else:
            streak = 0
        
    elif choice == 'stats':
        func.stats(victories, gamesplayed, highscore, streak)
    elif choice == 'règles':
        func.rules()
    elif choice == 'exit': # Gardé en anglais pour une meilleur comprehension et parce que c'est toujours comme cela
        break
    elif choice == 'tableflip':
        ascii.tableflip()
    elif choice == 'up up down down left right left right': # Rien à voir par ici
        print('↑, ↑, ↓, ↓, ←, →, ←, →')
        highscore = 11
    else:
        print('\033[1;31;40m Merci d\'entrer une commande valide \033[0;37;40m') # ANSI ecape codes permettent de mettre le texte en rouge
print('Au revoir')
