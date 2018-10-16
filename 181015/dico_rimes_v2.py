#!/usr/bin/env python3
#-*- coding : utf8 -*-

import pprint, random
import string

def extractionDatas_FromLine_ToListOfTuples(nomFic):
    with open(nomFic, 'r') as filein:
        # listDatas = [tuple(line.split('\t')[0:2]) for line in filein]
        listDatas = [tuple(line.split('\t')) for line in filein]

    return listDatas

    # listDatas sous la forme :
    # [('hindoues', '5du', 'hindou', 'NOM', 'f', 'p', '\n'),
    #  ('réfrigérateur', 'RefRiZeRat9R', 'réfrigérateur', 'NOM', 'm', 's', '\n'), ... ]
    # AVEC :
    # orthograghe, phoneme, lemme = infosMot[0], infosMot[1], infosMot[2]
    # cgram, genre, nombre = infosMot[3], infosMot[4], infosMot[5]

def constructionOfRimeDict(lexique, longueurRimeVoulue):
    # TODO : dans dico_3 (3 lettre rime) travailler sur le lemme au lieu de l'ortho !

    dico = {}

    for infosMot in lexique:
        orthograghe, phoneme, lemme = infosMot[0], infosMot[1], infosMot[2]
        cgram, genre, nombre = infosMot[3], infosMot[4], infosMot[5]

        # ortho	    phon	     lemme	      cgram	genre	nombre
        # épinglette	ep5glEt	     épinglette	  NOM	f	    s
        # invariance	5vaRj@s	     invariance	  NOM	f	    s
        # sociologue	sosjolOg	 sociologue	  NOM		    s
        # appuis	    ap8i	     appui	      NOM	m	    p

        # v1: dico[rime] = ['ortho1', ortho2 ...]

        if len(phoneme) >= longueurRimeVoulue:
            rime = phoneme[-longueurRimeVoulue:]
            # On l'ajoute au dico
            # v1 : dico.setdefault(rime, []).append(orthograghe)

            dico.setdefault(rime, {})

            if genre in dico[rime].keys() :
                if nombre in dico[rime][genre].keys() :
                    dico[rime][genre][nombre].append(orthograghe)
                else:
                    dico[rime][genre].setdefault(nombre, [])
            else :
                dico[rime].setdefault(genre, {})

            # dico[rime] = { masc { sing : [ortho1, ortho2 ...],
                             #        pluriel : [ortho1, ortho2 ...]}
                             # fem { sing : [ortho1, ortho2 ...],
                             #       pluriel : [ortho1, ortho2 ...]}
            # }

    return dico

def trouveMonPhoneme(word, lexique):
    for item in lexique:
        # item forme :
        # ('réfrigérateur', 'RefRiZeRat9R', 'réfrigérateur', 'NOM', 'm', 's', '\n'),

        orthograghe, phoneme, lemme = item[0], item[1], item[2]
        cgram, genre, nombre = item[3], item[4], item[5]

        if word == orthograghe :
            return phoneme

    return ""

def trouveMotRimant(word, dicoRimeL, listeMotsWithInfos, n=3):

    # TODO : -si mot pas dans son dico, il est incapable de générer la rime.
    #  il doit pouvoir, à défaut de 3 rimes, faire 2 rime,

    # 1 trouver la transcription phonétique
    monPhoneme = trouveMonPhoneme(word, listeMotsWithInfos)

    # CAS 1 : le phoneme n'existe pas dans la liste des mots (listeMotsWithInfos)
    # TODO : le rendre intelligent
    # On arrête, on ne renvoie rien.
    if not monPhoneme:
        return None

    # 2 extraire de la transcription les 3 derniers phonèmes (ou 2 le cas échéant)
    # 3 trouver dans le dictionnaire la liste des mots du lexique qui ont la même suite de phonèmes finaux

    # CAS 2 : le phoneme existe dans la liste des mots (listeMotsWithInfos) :
    # On cherche si sa terminaison (phoneme avec longueurRimeVoulue) existe dans le
        # dico des rimes (dicoRimeL)
    # Si non, on arrête TODO :
    maRime = monPhoneme[-n:]

    if maRime not in dicoRimeL:
        return None

    # Si oui, on note la Rime concernée
    entreeDicoRimant = dicoRimeL[maRime]

    # print(f"\n- La rime concernée est : \'{maRime}\'")
    # print(f"\n- Elle est de forme : {rimeDuMot}")
    # dico[rime] = { masc { sing : [ortho1, ortho2 ...],
                     #        pluriel : [ortho1, ortho2 ...]}
                     # fem { sing : [ortho1, ortho2 ...],
                     #       pluriel : [ortho1, ortho2 ...]}
    # }

    genre, nombre = None, None

    if  'f' in entreeDicoRimant :
        if 's' in entreeDicoRimant['f']:
            if word in entreeDicoRimant['f']['s'] :
                genre = 'f'
                nombre = 's'
        if 'p' in entreeDicoRimant['f']:
            if word in entreeDicoRimant['f']['p'] :
                genre = 'f'
                nombre = 'p'
        if '' in entreeDicoRimant['f']:
            if word in entreeDicoRimant['f'][''] :
                genre = ''
                nombre = 'p'

    if 'm' in entreeDicoRimant:
        if 's' in entreeDicoRimant['m']:
            if word in entreeDicoRimant['m']['s'] :
                genre = 'm'
                nombre = 's'
        if 'p' in entreeDicoRimant['m']:
            if word in entreeDicoRimant['m']['p'] :
                genre = 'm'
                nombre = 'p'
        if '' in entreeDicoRimant['m']:
            if word in entreeDicoRimant['m'][''] :
                genre = 'm'
                nombre = ''

    # print(f"- Le mot \'{word}\' est de genre : \'{genre}\' et de nombre \'{nombre}\'.")
    # rimeDuMot[genre][nombre].remove(word)

    # SOUS-CAS2 : Si on note la Rime ET que le mot (pas le phoneme) existe dans le contenu
        # de la rime, on va l'exclure, pour ne pas avoir un remplacement par lui-même
    # if word in rimeDuMot:
    #     rimeDuMot.remove(word)

    # 4. piocher un mot au hasard dans la liste
    if (genre is not None) and (nombre is not None):
        ouPiocher = entreeDicoRimant[genre][nombre]
    # print(f"\n- Où allons-nous piocher : {ouPiocher}")

        if len(ouPiocher) > 1 :
            rand = random.randint(0, len(ouPiocher) - 1)
            return ouPiocher[rand]


# TODO -il n'accorde pas le genre (or il a info.)

def main():

    ficLexiqueBrute = 'nom-lexique-brut.txt'
    # ficAModifier = 'brise-marine.txt'
    ficAModifier = 'hugo-lhomme.txt'

    listeMotsWithInfos = extractionDatas_FromLine_ToListOfTuples(ficLexiqueBrute)
    # pprint.pprint(listeMotsWithInfos)

    dicoRime_3pho = constructionOfRimeDict(listeMotsWithInfos, 3)
    dicoRime_2pho = constructionOfRimeDict(listeMotsWithInfos, 2)
    dicoRime_1pho = constructionOfRimeDict(listeMotsWithInfos, 1)

    # pprint.pprint(dicoRime_3pho)
    # pprint.pprint(dicoRime_2pho)
    # pprint.pprint(dicoRime_1pho)

    # for mot in ['jeunesse', 'beauté', 'vie', 'réfrigérateur', 'eau', 'amour'] :
    #     print(f"\n******* MOT : {mot}")
    #
    #     monPhoneme = trouveMonPhoneme(mot, listeMotsWithInfos)
    #     print(f"\n- Mon phoneme : {monPhoneme}.")
    #
    #     maRime = trouveMotRimant(mot, dicoRime_3pho, listeMotsWithInfos)
    #     print(f"- Je propose comme mot rimant : {maRime}.")

    with open(ficAModifier, mode='r') as file:
        for line in file :
            # si ligne vide, ne rien faire
            if not line.strip():
                continue

            # On récupère les mots de la ligne
            motsDeLaLigne = line.rstrip().split(" ")

            # Attention à la ponctuation
            punct = string.punctuation

            newline = []
            for mot in motsDeLaLigne:
                # print(mot)
                # on sépare les signes de ponctuation des mots
                if mot[-1] in punct:
                    signe = mot[-1]
                    mot = mot[:-1]
                    newline.append(mot)
                    newline.append(signe)
                else:
                    newline.append(mot)

            print(f"\n\n*** Ligne de base : \n\t{line}")
            # print(f"- Transfo en liste : \n\t{motsDeLaLigne}")
            # print(f"\n- Après traitement : \n\t{newline}")

            for wordATransforme in newline :
                index = newline.index(wordATransforme)
                if wordATransforme in punct :
                    continue
                # if len(wordATransforme) <=3 :
                #     continue

                # print(f"\n +++ {wordATransforme}")

                rimeEn3 = trouveMotRimant(wordATransforme, dicoRime_3pho, listeMotsWithInfos)
                if rimeEn3 :
                    # print(f"Youpi, j'ai : {rimeEn3}")
                    newline[index] = rimeEn3
                else:
                    rimeEn2 = trouveMotRimant(wordATransforme, dicoRime_2pho, listeMotsWithInfos)
                    if rimeEn2 :
                        newline[index] = rimeEn2
                    else:
                        rimeEn1 = trouveMotRimant(wordATransforme, dicoRime_1pho, listeMotsWithInfos)
                        if rimeEn1 :
                            newline[index] = rimeEn1

            newline = ' '.join(newline)
            print(f"\n+++ Ligne modifiée : \n\t{newline}")

if __name__ == '__main__':
    main()
