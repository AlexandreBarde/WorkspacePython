import sys
from random import randrange

# Ce script génère un chiffre aléatoire entre valMin et valMax
# L'utilisateur doit ensuite trouver ce chiffre en moins de nombreTentative

# Paramètres du jeu
valMin = 0
valMax = 100
nombreTentative = 10

# Initialisation nombre aléatoire
nombreAleatoire = randrange(valMin, valMax)

# Initilisation nombre proposé par le joueur, -1 car il pourrait être égal aux bornes et le jeu ne se lancerai pas
nombreJoueur = valMin - 1

# Initialisation nombre de tentatives du joueur
nombreTentativeJoueur = 0

print("=+=+[Le jeu du + ou -]+=+=")

while nombreJoueur != nombreAleatoire:
    nombreJoueur = int(input("Votre nombre ? "))
    nombreTentativeJoueur = nombreTentativeJoueur + 1
    if nombreTentativeJoueur == nombreTentative:
        print("Vous avez échoué !")
        sys.exit()
    else:
        if nombreJoueur > nombreAleatoire:
            print("Nombre trop grand !")
        elif nombreJoueur < nombreAleatoire:
            print("Nombre trop petit !")
        else:
            print("Bien joué !")
