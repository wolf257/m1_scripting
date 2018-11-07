#!/usr/bin/env python3
#-*- coding : utf8 -*-

import pprint
import random

import modules.fonctions as mesfonctions

linkToficSMS = 'heavy_files/cmr-88milsms-tei-v1.xml'
linkToficLexique = 'heavy_files/lexique382.txt'
linkToDbAbbr = 'db_abbr.pickle'

def main():

    listeDesSMS, liste_N_SMS_auHasard = [], []
    ensembleMotsLexique = set()
    ensembleDesMotsHorsLexique = set(tuple())
    dicoAbbr = {}

    while 1:
        a = input("""\n=======================================================
    Bonjour, et bienvenue. Veuillez m'indiquer votre cas :
    - 1 : C'est la première fois que vous lancez le programme.
    - 2 : Ce n'est pas la première fois.
    - (enter) Au secours, où suis-je ?? (pour quitter)
    Votre choix : """)

        if a.strip() == '1' or a.strip() == '2' :

            print("\n======== INFO ===========")
            mesfonctions.initialisation_des_donnees(listeDesSMS, ensembleMotsLexique, liste_N_SMS_auHasard, ensembleDesMotsHorsLexique, linkToficSMS, linkToficLexique)

            if a.strip() == '2' :

                dicoAbbr = mesfonctions.load_dico_abbr(dicoAbbr, linkToDbAbbr)
                print(f"\nNous avons déjà défini {len(dicoAbbr.keys())} abbréviations, dont par ex :")
                print(f"{dicoAbbr}")
                # for c in random.sample(list(dicoAbbr.items()), 5) :
                #     print(f"{c[0]} --> {c[1]}")

            b = input("\n..... Appuyer sur (enter) pour continuer .....")

            if b.strip() == '' :
                mesfonctions.remplir_dicoAbbr_aPartir_ensHorsLexique(dicoAbbr, ensembleDesMotsHorsLexique, linkToDbAbbr)

                break

            else :
                print("Doucement, juste le (enter).")

        elif a.strip() == '' :
            print('Au revoir')
            break

        else :
            print("Je n'ai pas compris, on reprend.")

if __name__ == '__main__':
    main()
