#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import collections, pprint

def compterNombreMot(file, dico):

    with open(file, 'r') as filein:
        for line in filein:
            for word in line.split():
                dico[word] +=1

    return dico

def compterLettre(file, dico):
    with open(file, 'r') as filein:
        for line in filein:
            for lettre in line:
                dico[lettre] += 1

    return dico

def compterVoyCons(file, dico):
    vowels = 'iuoaeéèê'
    # c pour compteur, v : voyelle ...
    cvt, cct, cot = 0, 0, 0

    print("\n******************************************************")

    with open(file, 'r') as filein:
        listLine = [line.rstrip() for line in filein]
        for line in listLine:
            cvp, ccp, cop = 0,0,0
            # line.rstrip('\n')
            print(f"\nLa phrase \" {line} \" contient :")
            for mot in line.split():
                mot.lower()
                for lettre in mot :
                    if lettre.isalpha() :
                        if lettre in vowels :
                            cvt += 1
                            cvp +=1
                        else :
                            cct +=1
                            ccp += 1
                    else :
                        if not lettre.isspace() :
                            cot += 1
                            cop += 1

            print(f"{cvp} voyelle(s), {ccp} consonne(s), et {cop} objet(s) non-identifié(s).")


        print(f"\n++ Cela nous donne un total de : {cvt} voyelle(s), {cct} consonne(s), et  {cot} objet(s) non-identifié(s).")

def main():
    file = 'brise-marine.txt'

    # DECOMPTE VOY CONS
    dicoDecompteVoyCons = collections.Counter()
    compterVoyCons(file, dicoDecompteVoyCons)

    # DECOMPTE MOT BRISE
    dicoDecompteMot = collections.Counter()
    dicoDecompteMot = compterNombreMot(file, dicoDecompteMot)
    print("\n******************************************************")
    print(f"\nVoici la distribution des mots :\n\n {dicoDecompteMot}")

    # DECOMPTE LETTRE
    dicoDecompteLettre = collections.Counter()
    dicoDecompteLettre = compterLettre(file, dicoDecompteLettre)
    print("\n******************************************************")
    print(f"\nVoici la distribution des lettres :\n\n {dicoDecompteLettre}")

    print("\n******************************************************")
    print(f"\nNB : Pour voir le détails, ligne par ligne, remontez plus haut.")


if __name__ == '__main__':
    main()
