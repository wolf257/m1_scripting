#!/usr/bin/env python3
#-*- coding : utf8 -*-

import pprint
import collections

def traitement_donnee(file, dico):
    # La ligne 0 contient les titres des attributs, donc on va juste l'ignorer.
    next(file)

    for line in file:
        # pour notre travail, nous n'avons besoin que des colonnes :
        # 1 (année), 3 (nombre de logements financés) et 10 (arrondissement)
        datas = line.split(';')

        arrondissement = datas[10]
        anneeConcernee = datas[1]
        nombreTotalFinancesAnnee = int(datas[3])

        if not arrondissement.isdigit() :
            continue

        dico.setdefault(arrondissement, {})

        # on s'occupe d'une année particulière
        if anneeConcernee in dico[arrondissement].keys() :
            dico[arrondissement][anneeConcernee] += nombreTotalFinancesAnnee
        else :
            dico[arrondissement][anneeConcernee] = nombreTotalFinancesAnnee

        # on s'occupe du total
        if 'total' in dico[arrondissement].keys() :
            dico[arrondissement]['total'] += nombreTotalFinancesAnnee
        else :
            dico[arrondissement]['total'] = nombreTotalFinancesAnnee

    # TEST
    # print("Résultats détaillés : ")
    # pprint.pprint(dico)

def calcul_et_presentation_analyse(dico, arrondissement):
    total = dico[arrondissement]['total']
    chiffre2001 = dico[arrondissement]['2001']
    chiffre2016 = dico[arrondissement]['2016']
    if '2015' in dico[arrondissement].keys():
        lastYear = '2015'
        chiffreLastYear = dico[arrondissement]['2015']
    else:
        lastYear = '2014'
        chiffreLastYear = dico[arrondissement]['2014']

    evolutionFrom2001 = (chiffre2016 / chiffre2001) * 100
    evolutionFromLast = (chiffre2016 / chiffreLastYear) * 100

    message = (
        f"\n\nPour l'arrondissement {arrondissement}, on a :"
        f"\n\t * total sur toute la période : {total}, "
        f"\n\t * année de référence (2001) : {chiffre2001},"
        f"\n\t * année la plus proche disponible ({lastYear}) : {chiffreLastYear}"
        f"\n\t * dernière année (2016) : {chiffre2016},"
        f"\nCe qui nous donne : "
        f"\n\t ** Évolution (2016) par rapport à (2001) : {round(evolutionFrom2001, 2)} % "
        f"\n\t ** Évolution (2016) par rapport à {lastYear} : {round(evolutionFromLast, 2)} % "
    )
    print(message)


def main():
    nomficSource = 'logements_sociaux_paris.csv'
    dico = {}

    with open(nomficSource, mode='r', encoding='utf8') as file:
        traitement_donnee(file, dico)

        # On veut classer nos arrondissements par leur total :
        listeTotaux = [(dico[arrondissement]['total'] , arrondissement) for arrondissement in dico.keys()]
        listeTotaux = sorted(listeTotaux, reverse=True)

        # TEST
        print("\nListe des totaux classés par ordre décroissant : ")
        pprint.pprint(listeTotaux)

        # On ne garde que les 5 premiers.
        # Vu que listeTotaux est une liste, les éléments sont classés par leur indice.
        arrondissement_A_Conserver = [item[1] for item in listeTotaux[0:5]]

        # TEST
        print("\nListe des 5 arrondissements les plus actifs en maitère de logement sociaux : ")
        pprint.pprint(arrondissement_A_Conserver)

        for arrondissement in arrondissement_A_Conserver:
            calcul_et_presentation_analyse(dico, arrondissement)

if __name__ == '__main__':
    main()
