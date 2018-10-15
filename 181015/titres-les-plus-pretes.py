#!/usr/bin/env python3
#-*- coding : utf8 -*-

import collections
import pprint

def main():

    nomficSource = 'titres-les-plus-pretes.csv'
    dico = collections.Counter()

    with open(nomficSource, mode='r', encoding='utf8') as file:

        # La ligne 0 contient les titres des attributs, donc on va juste l'ignorer.
        next(file)
        for line in file:

            # pour notre travail, nous n'avons besoin que des colonnes 1 (type de document) et 2 (prêts)
            datas = line.split(';')[1:3]

            # on remplit notre Counter
            dico[datas[0]] = dico.setdefault(datas[0], 0) + int(datas[1])

    # affichage
    rang = 1
    for categorie , nombre in dico.most_common() :
        print(f"Rang {rang} : '{categorie}' avec {nombre} prêts.")
        rang+=1

if __name__ == '__main__':
    main()
