#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random
def main():
    # Liste des mots du pendu
    liste_mots = ["vie", "mort", "joie"]

    mot_a_trouve = random.choice(liste_mots)
    mot_a_trous = list("_"*len(mot_a_trouve))
    nombreTentativesPermis, numeroTentative = len(mot_a_trouve), 0
    didHeFindIt = False

    ######################################
    # PRESENTATION
    ######################################

    print("\nBienvenu dans notre jeu du pendule. \n\nVous devez trouver le mot : {}.".format(" ".join(mot_a_trous)))

    print("\nPour être gentil, vous avez droit {} erreurs, soit le nombre de lettres du mot.".format(nombreTentativesPermis) +\
    "\nEn contrepartie, même si une lettre est présente plusieurs fois, elle apparaitra en autant de fois que d'occurences. Bonne chance !")


    while numeroTentative < nombreTentativesPermis :

        charFromUser = input("\nVotre choix : ")

        if charFromUser in mot_a_trouve:

            indexLettreInMot = mot_a_trouve.index(charFromUser)

            mot_a_trous[indexLettreInMot] = charFromUser
            liste_des_index.append(indexLettreInMot)

            if ''.join(mot_a_trous) == mot_a_trouve :
                didHeFindIt = True
                break
            else :
                print("***Bien ! Il nous reste : {}.".format(" ".join(mot_a_trous)))
                continue

        else:
            numeroTentative +=1
            tentativesRestantes = nombreTentativesPermis - numeroTentative
            print ("***Oups. Il nous reste {} tentatives.".format(tentativesRestantes))
            continue


    messageGood = "\nBien joué, c'était bien le mot : {}.".format(mot_a_trouve)
    messageBad = "\nDommage. Le mot à trouver était : {}.".format(mot_a_trouve)

    print(messageGood) if didHeFindIt == True else print(messageBad)

if __name__ == '__main__':
    main()
