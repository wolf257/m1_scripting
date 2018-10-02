#!/usr/bin/env python3
#-*- coding : utf8 -*-

import pprint
import collections

def main():

    nom_du_fichier = 'sem_Ef9POe.txt'

    with open(file=nom_du_fichier, mode='r', encoding='utf8') as fic_in:
        liste_des_tuples = [tuple(line.split()) for line in fic_in.readlines() if line.strip()]

    dico_des_pos = collections.Counter()

    for (_, pos, _) in liste_des_tuples :
        if pos.startswith('_'):
            pos = pos[1:]

        dico_des_pos[pos] += 1

    print("Voici la liste des POS classées par fréquence décroissante : ")
    for (pos, occ) in dico_des_pos.most_common() :
        print(occ, pos)

if __name__ == '__main__':
    main()
