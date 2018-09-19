#!/usr/bin/env python3
#-*- coding : utf8 -*-

#-------------------------------------------------
#   GUEYE Ousseynou - M1 TAL Inalco - 21 50 50 55
#       Chifouni en python3
#-------------------------------------------------

def askChoice(nom) :
    while 1 :
        choix = input("\nQue joue " + str(nom) + " : " +\
            "\n 0 : Papier " + \
            "\n 1 : Cailloux " + \
            "\n 2 : Ciseaux " + \

            "\n\n Réponse : ")

        if (choix.strip().isnumeric()) and (int(choix) < 3) :
                choix = choix
        else :
            print("Mauvais choix, reprenons.")
            continue

        return choix

def whoWins(choix1 , choix2) :

    # choix1 correspond aux lignes. C'est le choix du joueur 0 --> 0 veut dire qu'il gagne.
    # choix2 correspond aux colonnes. C'est le choix du joueur 1 --> 1 veut dire qu'il gagne.
    # 2 veut dire qu'il y a égalité.
    # Ce qui nous donne :
    #          |papier|cailloux|ciseaux|
    # papier   |   2  |    0   |   1   |
    # cailloux |   1  |    2   |   0   |
    # ciseaux  |   0  |    1   |   2   |

    tableDesResultatsPossibles = [[2,0,1] , [1,2,0], [0,1,2]]

    winner = tableDesResultatsPossibles[choix1][choix2]

    return winner

def main():

    print("\n======= Bienvenue sur notre chifoumi =======\n")

    joueurs = ["Kobe" , "Lebron"]
    nomDesChoix = ["Papier" , "Cailloux" , "Ciseaux"]

    listeDesChoix = {}

    for joueur in joueurs :
        choixDuJoueur = askChoice(joueur)

        # TEST
        # print("choix : " + choixDuJoueur)

        listeDesChoix[joueur] = int(choixDuJoueur)

    numeroVainqueur = whoWins(listeDesChoix[joueurs[0]] , listeDesChoix[joueurs[1]])

    print("\n=====> {} a joué {}, et {} a joué {}.".format(joueurs[0], nomDesChoix[listeDesChoix[joueurs[0]]] , joueurs[1] , nomDesChoix[listeDesChoix[joueurs[1]]]))

    if numeroVainqueur == 2 :
        # c-a-d que les 2 gagnent, donc égalité.
        print("\nIl y a égalité.")

    elif numeroVainqueur == 3 :
        # c-a-d que le cas n'est pas traité.
        print("\nVotre programmeur est nul :-), c'est impossible !")

    else :
        # c-a-d qu'il y a un vainqueur.
        print("\nDonc {} a gagné.".format(joueurs[numeroVainqueur]))

    print("\n======= Au revoir =======\n\n")

if __name__ == '__main__':
    main()
