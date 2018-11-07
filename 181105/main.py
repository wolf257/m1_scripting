#!/usr/bin/env python3
#-*- coding : utf8 -*-

import pprint
import random
import pickle

import modules.fonctions as fonctions

class mesliens():
    """docstring for mesliens."""

    linkToficSMS = 'heavy_files/cmr-88milsms-tei-v1.xml'
    linkToficLexique = 'heavy_files/lexique382.txt'
    linkToDbAbbr = 'db_abbr.pickle'

class mesvariables():
    """docstring for mesvariables."""

    listeDesSMS = []
    ensembleMotsLexique = set()
    liste_N_SMS_auHasard = []
    ensembleDesMotsHorsLexique = set(tuple())

def initialisation_des_donnees() :
    listeDesSMS = mesvariables.listeDesSMS

    ensembleMotsLexique = mesvariables.ensembleMotsLexique

    #===================================
    fonctions.recuperer_contenusSMS_et_ajouter_a_liste(mesliens.linkToficSMS, listeDesSMS)

    #===================================
    fonctions.recuperer_listeMot_et_ajouter_a_ensemble(mesliens.linkToficLexique, ensembleMotsLexique)

    #===================================
    nombreSMS_aTraiter = 50

    liste_N_SMS_auHasard = mesvariables.liste_N_SMS_auHasard # no need, juste une habitude.
    liste_N_SMS_auHasard = random.sample(listeDesSMS, nombreSMS_aTraiter)

    fonctions.show_NbSMS_aTraiter(nombreSMS_aTraiter)
    # fonctions.show_5RandomSMS_aTraiter(nombreSMS_aTraiter, liste_N_SMS_auHasard)

    #===================================
    ensembleDesMotsHorsLexique = mesvariables.ensembleDesMotsHorsLexique

    for sms in liste_N_SMS_auHasard :
        for word in sms.split() :
            # pour le len <= 4, c'est un choix arbitraire.
            # il est plutôt rare d'avoir une abbr de plus de 4 lettres.
            if (not word.lower() in ensembleMotsLexique) and (len(word) <= 4) and (word.isalnum()) :
                mot_et_contexte = (word.lower(), sms)
                ensembleDesMotsHorsLexique.add(mot_et_contexte)

    fonctions.show_NbMotsHorsLexique(nombreSMS_aTraiter, ensembleDesMotsHorsLexique)
    # fonctions.show_10RandomMotsHorsLexique(ensembleDesMotsHorsLexique)

def load_dico_abbr(dicoAbbr, link) :
    with open(link, mode='rb') as filein:
        dicoAbbr = pickle.load(filein)

    return dicoAbbr

def dump_dico_abbr(dicoAbbr, link) :
    with open(link, mode='wb') as fileout:
        pickle.dump(dicoAbbr, fileout)


def remplir_dicoAbbr_aPartir_ensHorsLexique(dicoAbbr, ensembleDesMotsHorsLexique, linkToDbAbbr):

    while 1:

        # on choisit un mot au hasard
        mot_et_contexte = random.sample(ensembleDesMotsHorsLexique, 1) # produit une liste
        mot_et_contexte = mot_et_contexte[0] # on a notre tuple

        if len(mot_et_contexte) < 2 :
            continue

        mot = mot_et_contexte[0]
        contexte = mot_et_contexte[1]

        # si par hasard, on avait déjà rempli le mot, pas besoin
        if mot in dicoAbbr.keys():
            continue
#
#         # sinon, on peut commencer
        print(f"\n+++++++ NEW WORD +++++++")
        print(f"Mot : {mot} \nContexte : {contexte}")

        a = input("""Signification ou (enter) pour quitter : """)

        if a.strip() == '' :
            dump_dico_abbr(dicoAbbr, mesliens.linkToDbAbbr)
            print(f"\nAu revoir. J'ai enregistré le contenu de notre dictionnaire dans '{mesliens.linkToDbAbbr}'")
            break

        elif a.strip().isalnum() :
            signification = a.strip()
            dicoAbbr[mot] = signification
            print(f"\n+++++++ NEW WORD +++++++")

            continue

        else :
            print("Je n'ai pas compris, on reprend.")



def main():

    dicoAbbr = {}

    while 1:
        a = input("""\n=======================================================
    Bonjour, et bienvenue. Veuillez m'indiquer votre cas :
    - 1 : C'est la première fois que vous lancez le programme.
    - 2 : Ce n'est pas la première fois.
    - (enter) Au secours, où suis-je ?? (pour quitter)
    Votre choix : """)

        if a.strip() == '1' :
            initialisation_des_donnees()

            remplir_dicoAbbr_aPartir_ensHorsLexique(dicoAbbr, mesvariables.ensembleDesMotsHorsLexique, mesliens.linkToDbAbbr)

            break

        elif a.strip() == '2' :
            initialisation_des_donnees()
            dicoAbbr = load_dico_abbr(dicoAbbr, mesliens.linkToDbAbbr)
            print(f"Nous avons le dict : {dicoAbbr}.")

            remplir_dicoAbbr_aPartir_ensHorsLexique(dicoAbbr, mesvariables.ensembleDesMotsHorsLexique, mesliens.linkToDbAbbr)

            break

        elif a.strip() == '' :
            print('Au revoir')
            break

        else :
            print("Je n'ai pas compris, on reprend.")

if __name__ == '__main__':
    main()
