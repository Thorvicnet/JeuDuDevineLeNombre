from random import randint  # utilisé par game()
from modules.TestNombre import verification
import modules.AsciiArt as ascii


def rules():
    """Les règles du jeu avec utilisation des ANSI escape codes pour les couleurs
    """
    print("\033[0;32;40mVoici les règles du jeu : \033[0;37;40m\n\tAprès avoir choisi votre difficulté, un nombre "
          "aléatoire sera généré entre 1 et 100 inclus,\n\tvous disposerez par la suite d'un nombre limité de "
          "tentative en fonction de la difficulté,\n\tsi victoire s'ensuit votre score final sera calculé grâce à la "
          "difficulté et est sur 10")  # Ligne trop longue sinon PEP8: E501


def difficulty():  # difficulté
    """Permet de choisir la difficulté

    Returns:
        int: le niveau de difficulté choisit par le joueur
    """
    difficultylvl = input(
        '> Merci de choisir entre simple, moyen, difficile, impossible et custom : ')
    if difficultylvl == 'simple':
        guess = 10  # Ce nombre est le nombre de tentative que le joueur aura
    elif difficultylvl == 'moyen':
        guess = 8
    elif difficultylvl == 'difficile':
        guess = 5
    elif difficultylvl == 'impossible':
        guess = 1  # bonne chance
    elif difficultylvl == 'custom':  # on laisse le joueur choisir sa difficulté
        guess = int(input('> Combien de tentatives voulez-vous avoir : '))
        if guess <= 0:
            print("\033[1;31;40m A quoi vous attendiez vous ???\033[0;37;40m")
        elif guess == 42:  # rien à voir
            print('Ce n\'est pas le secret de ce code')
    else:
        print('Merci de rentrer une difficulté correcte !!!')
        # Le joueur va être relancer dans cette fonction jusqu'à ce qu'il ou l'ordinateur soit mort design voulu
        guess = difficulty()
    return guess


def game(guessnbr):
    """Lance une partie de jeu

    Args:
        guessnbr (int): nombre de tentatives que le joueur possède

    Returns:
        bool: renvoie True si il y a victoire ou False en cas de défaite
    """
    rndn = randint(1, 100)  # rndn = random number = nombre aléatoire
    for i in range(guessnbr):

        verif = None  # On donne à la variable une valeur qui permet de rentrer dans la boucles qui suit
        while not verif:  # Tant que le nombre est incorrect on relance l'input
            guess = input('> Devinez le nombre : ')
            # On regarde si la tentative est correcte et on stock le résultat
            verif = verification(guess)

        # On le met en integer maintenant que l'on sait que c'est possible
        guess = int(guess)

        if guess > rndn:  # On vérifie si le nombre est plus grand ou plus petit
            print(
                'Votre nombre est supérieur [' + str(i+1) + '/' + str(guessnbr) + ']')  # On rajoute un indicateur de progression
        elif guess < rndn:
            print(
                'Votre nombre est inférieur [' + str(i+1) + '/' + str(guessnbr) + ']')
        else:
            ascii.victory()  # VICTOIRE
            return True

    ascii.defeat()  # Vous avez perdu
    print('Le nombre était : ' + str(rndn))
    print('Vous aurez plus de chance la prochaine fois...')
    return False


def stats(victories, gamesplayed, highscore, streak):
    """Permet d'afficher les statistiques de la session

    Args:
        victories (int): nombre de victoires
        gamesplayed (int): nombre de parties jouées
        highscore (int): meilleur score de la session
        streak (int): suite de victoire actuelle
    """
    if gamesplayed == 0:  # On évite la division par 0
        print('Vous n\'avez pas encore joué !')
    else:
        print('Vous avez joué', gamesplayed,
              'partie(s) dont', victories, 'gagnée(s)')
        # Je rajoute round() puisque je ne suis pas sur si int() n'arrondi pas à la décimal inférieur
        print('Vous avez donc un pourcentage de réussite de', str(
            int(round((victories/gamesplayed)*100, 0))) + '%')
        print('Votre suite de victoire actuelle (streak) est de', streak, 'parties')
        print('Votre record est de', str(highscore) + '/10')
