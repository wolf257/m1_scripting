#!/usr/bin/env python3
#-*- coding : utf8 -*-

#-------------------------------------------------
#   GUEYE Ousseynou - M1 TAL Inalco - 21 50 50 55
#       Devinette en python3
#-------------------------------------------------

import random

def askNumber(numeroTentative):
    while 1:
        a = input("\nTentative {}/5. Devinez le nombre que j'ai en tête : ".format(numeroTentative+1))

        if a.isnumeric() :
            numberFromUser = int(a)
            break
        else :
            print("\nCe n'est pas un nombre. Tentative non considérée. Reprenons.")

    return numberFromUser

def main():

    print("\n======= Bienvenue =======")
    print("\nVous avez 5 tentatives pour trouver le nombre que j'ai en tête. Good luck !")

    # Generation du nombre aleatoire dans l'intervalle [1,10]
    numberToGuess = random.randint(0,10)

    # TEST
    # print(numberToGuess)

    numeroTentative = 0
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
        "\n\n*** Le nombre était {}.".format(numberToGuess))
    else :
        print("\nExcellent, vous avez trouvé, c'était bien {}.".format(numberToGuess))

    print("\n======= Au revoir =======")

if __name__ == '__main__':
    main()
