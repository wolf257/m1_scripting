#!/usr/bin/env python3
#-*- coding : utf8 -*-

#-------------------------------------
#   GUEYE Ousseynou
#   21 50 50 55
#       Devinette en python3
#-------------------------------------

# Faire un jeu un peu sur le modèle du chifoumi où
# l'utilisateur doit deviner un chiffre entre 1 et 10 (10 inclus).
# 5 essais possibles.
# Le jeu doit donner des indications (trop grand, trop petit) à chaque essai.

import random

def askNumber(numeroTentative):
    while 1:
        a = input("\nTentative {}. devinez le nombre que j'ai en tête : ".format(numeroTentative+1))

        if a.isnumeric() :
            numberFromUser = int(a)
            break
        else :
            print("\nCe n'est pas un nombre. Tentative non considérée. Reprenons.")

    return numberFromUser

def main():
    # Generation du nombre aleatoire dans l'intervalle [1,10]
    numberToGuess = random.randint(0,10)

    # TEST
    # print(numberToGuess)

    numeroTentative = 0
    # comment
    didHeFindIt = False

    while numeroTentative < 5 :
        numberFromUser = askNumber(numeroTentative)

        if numberFromUser == numberToGuess :
            didHeFindIt = True
            break

        elif numberFromUser < numberToGuess :
            print("\nTrop petit !")
            numeroTentative += 1
            continue

        elif numberFromUser > numberToGuess :
            print("\nTrop grand !")
            numeroTentative += 1
            continue

    if didHeFindIt == False :
        print("\nDommage, les 5 tentatives n'ont pas été suffisantes." +\
        "\n*** Le nombre était {}.".format(numberToGuess))
    else :
        print("\nExcellent, vous avez trouvé, c'était bien {}.".format(numberToGuess))

if __name__ == '__main__':
    main()
