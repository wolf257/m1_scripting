#!/usr/bin/env python3
# -*- coding : utf8 -*-

from collections import Counter
import pprint


def combien_conservatoires_par_departement(file, conteur):
    with open(file, mode='r') as filein:
        for line in filein:
            codepostal = line.split(";")[6]
            if codepostal.isnumeric():
                dept = codepostal[:2]
                conteur[dept] += 1


def qui_a_la_meilleure_offre(file, listRef, offreParDept):
    with open(file, mode='r') as filein:

        for line in filein:
            dpt = line.split(',')[0]
            nomDpt = line.split(',')[1]
            nbHbtsJeune = line.split(',')[2]

            if dpt in listRef.keys():
                nbConservatoire = int(listRef[dpt])
                nbHbtsJeune = int(nbHbtsJeune)
                # nbConservatoireParJeune = nbConservatoire / nbHbtsJeune
                nbJeuneParConservatoire = nbHbtsJeune / nbConservatoire

                offreParDept.append((nbJeuneParConservatoire, dpt, nomDpt))


def main():
    ficODT = 'les-conservatoires-et-ecoles-de-musique-en-ile-de-france.csv'
    conservatoires_par_dpt = Counter()

    combien_conservatoires_par_departement(ficODT, conservatoires_par_dpt)

    ficINSEE = 'estim-pop-dep-sexe-gca2018.csv'
    offreParDept = []

    qui_a_la_meilleure_offre(ficINSEE, conservatoires_par_dpt, offreParDept)

    bestOffer = sorted(offreParDept, key=lambda x: x[0])

    print(f"Si nous nous intéressons juste au nombre de conservatoires, voici l'ordre : ")
    for i, cp in enumerate(conservatoires_par_dpt.most_common()):
        print(f"Rang : {i+1} - Département : {cp[0]} avec {cp[1]} conservatoires.")

    print(f"\nPar contre, ce nombre doit être ajusté par rapport aux principaux consommateurs, ")
    print(f"soit les jeunes de 0-19ans. Cela donne : ")
    for i, cp in enumerate(bestOffer):
        print(f"Rang : {i+1} - Département : {cp[1]} avec {round(cp[0])} jeunes par conservatoire.")


if __name__ == '__main__':
    main()
