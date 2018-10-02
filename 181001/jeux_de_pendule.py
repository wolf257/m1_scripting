#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import random
def main():
# Liste des mots du pendu
    liste_mots = [
        "amour", "mort", "joie", "tristesse",
        "python", "bash", "fichier", "repertoire", "livre", "feuille"]

    mot_a_trouve = 'feuille'
    # mot_a_trouve = random.choice(liste_mots)
    mot_a_trous = list("_"*len(mot_a_trouve))

    nombreTentativesPermis, numeroTentative = len(mot_a_trouve), 0

    didHeFindIt = False

    liste_des_index = []


    print("\nBienvenu dans notre jeu du pendule. \n\nVous devez trouver le mot : {}.".format(" ".join(mot_a_trous)))

    print("\nPour être gentil, vous avez droit {} erreurs, soit le nombre de lettres du mot.".format(nombreTentativesPermis) +\
    "\nEn contrepartie, même si une lettre est présente plusieurs fois, elle apparaitra en autant de fois que d'occurences. Bonne chance !")


    while numeroTentative < nombreTentativesPermis :

        charFromUser = input("\nVotre choix : ")

        if charFromUser in mot_a_trouve:

            indexLettreInMot = mot_a_trouve.index(charFromUser)

            # print("TEST : liste_des_index : {}. \n".format(liste_des_index))

            if indexLettreInMot in liste_des_index :
                indexLettreInMot = mot_a_trouve.index(charFromUser, indexLettreInMot+1)

            mot_a_trous[indexLettreInMot] = charFromUser
            liste_des_index.append(indexLettreInMot)

            # print("TEST : liste_des_index : {}. \n".format(liste_des_index))

            if ''.join(mot_a_trous) == mot_a_trouve :
                didHeFindIt = True
                break
            else :
                print("***Bien ! Il nous reste : {}.".format(" ".join(mot_a_trous)))
                continue

        # BON
        else:
            numeroTentative +=1
            tentativesRestantes = nombreTentativesPermis - numeroTentative
            print ("***Oups. Il reste {} tentatives.".format(tentativesRestantes))

            continue

    if didHeFindIt == True :
        print("\nBien joué !")
    else:
        print("\nDommage. Le mot à trouver était : {}.".format(mot_a_trouve))

    print("\n=== Au revoir. ===")

if __name__ == '__main__':
    main()
