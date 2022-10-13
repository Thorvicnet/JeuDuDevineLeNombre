from random import randint

# Je l'ai mis dans un autre fichier à cause de sa laideur (une liste qui continue vers l'infini)


def citations():
    """Renvoie une citation aléatoire parmit la liste "citations"

    Returns:
        string: citation renvoyée
    """
    citations = ['La fortune sourit aux audacieux', 'Le mendiant ne craint pas les revers de fortune', 'C\'est au courage que va la fortune', 'Mais que sert le mérite où manque la fortune ?',
                 'On ne se ruine jamais mieux , que lorsqu\'on a beaucoup de fortune', 'La fortune vient à pas de tortue, et fuit comme une gazelle', 'La fortune est semblable au verre ; plus elle est brillante, plus elle est fragile', 'Ceci n\'est pas aléatoire']
    # renvoie une citations aléatoire parmi la liste en utilisant sa longueur ( "len()" )
    return '\033[0;32;40m' + citations[randint(0, len(citations)-1)] + '\033[0;37;40m'
