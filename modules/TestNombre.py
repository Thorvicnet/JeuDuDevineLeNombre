def verification(n):
    """Verifie si ce qu'a rentré le joueur est correct

    Args:
        n (anything): ce qu'a rentré le joueur

    Returns:
        bool: renvoie True si ce qu'a rentré le joueur est valide et False sinon
    """
    try:
        n = int(n)
        if n < 1 or n > 100:  # On vérifie que l'utilisateur entre un nombre valide
            print("Erreur le nombre entré n'est pas valide...")
            return False
        else:
            return True
    except:
        print("Ce n'est pas un entier...")
        return False
