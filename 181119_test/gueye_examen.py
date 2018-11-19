#!/usr/bin/env python3
# -*- coding : utf8 -*-

import re
import pprint
from collections import Counter

ficSource = 'les-conseillers-de-paris-de-1977-a-2014.csv'


def nombreTotalDeConseillers(file):
    nbTotalConseiller = int()
    with open(file, mode='r') as filein:
        next(filein)
        f = filein.readlines()
        nbTotalConseiller = len(f)

    print(f"\n======= Question 1 =======")
    print(f"\nNous avons un total de {nbTotalConseiller} conseillers, femmes et hommes confondus.")


def nombreConseillersSelonSexe(file):
    nbConseillers, nbConseilleres = 0, 0

    with open(file, mode='r') as filein:
        next(filein)
        for line in filein:
            sexe = line.split(";")[1]
            if sexe.endswith('er'):
                nbConseillers += 1
            if sexe.endswith('ère'):
                nbConseilleres += 1

    print(f"\n======= Question 2 =======")
    print(f"\nParmi ces personnes, on :"
          f"\n- {nbConseilleres} conseillères."
          f"\n- {nbConseillers} conseillers."
          f"\nSoit un total de {nbConseillers + nbConseilleres} personnes.")


def nombreConseillersSelonSexeAvant1995(file):
    nbConseillersAvt1995, nbConseilleresAvt1995 = 0, 0

    with open(file, mode='r') as filein:
        next(filein)
        for line in filein:
            sexe = line.split(";")[1]
            mandature = line.split(";")[0]
            debutMandat = int(mandature.split("-")[0])
            # print(debutMandat, end=' --- ')

            if debutMandat < 1995:
                if sexe.endswith('er'):
                    nbConseillersAvt1995 += 1
                if sexe.endswith('ère'):
                    nbConseilleresAvt1995 += 1

    print(f"\n======= Question 3 =======")
    print(f"\nOnt été élus avant 1995 (1995 exclu) :"
          f"\n- {nbConseilleresAvt1995} conseillères."
          f"\n- {nbConseillersAvt1995} conseillers."
          f"\nSoit un total de {nbConseilleresAvt1995 + nbConseillersAvt1995} personnes.")


def listeConseillersAParticules(file):
    print(f"\n======= Question 4 =======")
    print(f"\nVoici la liste des conseillers ayant un nom à particule :")

    with open(file, mode='r') as filein:
        next(filein)
        for line in filein:
            nomDeFamille = line.split(";")[4].strip()
            prenom = line.split(";")[3]
            sexe = line.split(";")[1]
            if nomDeFamille.endswith(f"(de)") \
                or nomDeFamille.endswith(f"(d')") \
                    or nomDeFamille.endswith(f"(de la)"):
                    if sexe.endswith('er'):
                        print(f"- Monsieur {nomDeFamille} {prenom}.")
                    if sexe.endswith('ère'):
                        print(f"- Madame {nomDeFamille} {prenom}.")


def nbConseillersSelonNbMandat(file):
    DicoNomEtNbMandat = {}

    with open(file, mode='r') as filein:
        next(filein)
        for line in filein:
            nomDeFamille = line.split(";")[4].strip()
            prenom = line.split(";")[3].strip()
            if (nomDeFamille, prenom) in DicoNomEtNbMandat.keys():
                DicoNomEtNbMandat[(nomDeFamille, prenom)] += 1
            else:
                DicoNomEtNbMandat[(nomDeFamille, prenom)] = 1

    recuperationDesNbDeMandats = [value for key, value in DicoNomEtNbMandat.items()]
    nbConseillersSelonNbMandat = Counter(recuperationDesNbDeMandats)

    print(f"\n======= Question 5 =======")

    totalMandat = 0

    print(f"\nVoici le nom de conseillers selon le nombre de mandats :")
    for nbMandat, nbConseillers in nbConseillersSelonNbMandat.most_common():
        if nbMandat == 1:
            formeMandat = 'mandat'
        else:
            formeMandat = 'mandats'

        print(f"- {nbConseillers} conseillers ont eu {nbMandat} {formeMandat}.")
        totalMandat += (nbMandat * nbConseillers)

    print(f"Cela nous donne un total de {totalMandat} mandats.\n")


def main():

    nombreTotalDeConseillers(ficSource)
    nombreConseillersSelonSexe(ficSource)
    nombreConseillersSelonSexeAvant1995(ficSource)

    listeConseillersAParticules(ficSource)
    nbConseillersSelonNbMandat(ficSource)


if __name__ == '__main__':
    main()
