#!/usr/bin/env python3
#-*- coding : utf8 -*-

import pprint
import collections

def main():

    nom_du_fichier = 'sem_Ef9POe.txt'

    with open(file=nom_du_fichier, mode='r', encoding='utf8') as fic_in:
        liste_des_tuples = [tuple(line.split()) for line in fic_in.readlines() if line.strip()]

    pprint.pprint(liste_des_tuples)

    dico_des_pos = collections.Counter()

    for (_, pos, _) in liste_des_tuples :
        # j'ai remarqué que certaines POS commence par un underscore (ex : ADV et _ADV)
        # pour ne pas fausser le calcul, on les enlève
        if pos.startswith('_'):
            pos = pos[1:]

        dico_des_pos[pos] += 1

    pprint.pprint(dico_des_pos)

# 1. À partir du fichier tsv `sem_Ef9POe.conll`
#   1. pour chaque POS listez les types classés par ordre d'occurrence décroissante, (DONE)
#   2. pour chaque type de chunk indiquez les longueurs min et max (en nb de mots).


if __name__ == '__main__':
    main()
