#!/usr/bin/env python3
#-*- coding : utf8 -*-

import pprint, random
import string

def extractionDatas_FromLine_ToListOfTuples(nomFic):
    with open(nomFic, 'r') as filein:
        # on prend toutes les données
        listDatas = [tuple(line.split('\t')) for line in filein]

    return listDatas

def constructionOfRimeDict(lexique, longueurRimeVoulue):
    dico = {}

    for infosMot in lexique:
        orthograghe, phoneme, lemme = infosMot[0], infosMot[1], infosMot[2]
        cgram, genre, nombre = infosMot[3], infosMot[4], infosMot[5]

        if len(phoneme) >= longueurRimeVoulue:
            rime = phoneme[-longueurRimeVoulue:]

            dico.setdefault(rime, {})
            if genre in dico[rime].keys() :
                if nombre in dico[rime][genre].keys() :
                    dico[rime][genre][nombre].append(orthograghe)
                else:
                    dico[rime][genre].setdefault(nombre, [])
            else :
                dico[rime].setdefault(genre, {})

            # On aura une structure de type dict, de forme :
            # dico[rime] = { 'f' { 's' : [... , ...],
            #                         'p' : [..., ...],
            #                         '' : [..., ...]}
            #                'm' { 's' : [... , ...],
            #                      'p' : [..., ...],
            #                      '' : [..., ...]}
            # }

    return dico

def trouveMonPhoneme(word, lexique):
    for item in lexique:
        orthograghe, phoneme = item[0], item[1],
        genre, nombre = item[4], item[5]

        if word == orthograghe :
            return phoneme

    return ""

def trouveMotRimant(word, dicoRimeL, listeMotsWithInfos, n=3):

    # 1 trouver la transcription phonétique
    monPhoneme = trouveMonPhoneme(word, listeMotsWithInfos)

    # CAS 1 : le phoneme n'existe pas dans la liste des mots (listeMotsWithInfos)
    # On arrête, on ne renvoie rien.
    # TODO : le rendre intelligent
    if not monPhoneme:
        return None

    # CAS 2 : le phoneme existe dans la liste des mots (listeMotsWithInfos) :
    # On cherche si sa terminaison (phoneme avec longueurRimeVoulue) existe dans le
        # dico des rimes (dicoRimeL) ?
    maRime = monPhoneme[-n:]

    # Si non, on ne renvoie rien :
    if maRime not in dicoRimeL:
        return None

    # Si oui, on note l'entrée du dico correspondant à la rime
    entreeDicoRimant = dicoRimeL[maRime]

    # TEST
    # print(f"\n- La rime concernée est : \'{maRime}\'")
    # print(f"\n- Elle est de forme : {rimeDuMot}")

    # On s'occupe du genre et du nombre de notre mot
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

    # TEST
    # print(f"- Le mot \'{word}\' est de genre : \'{genre}\' et de nombre \'{nombre}\'.")

    # Si on trouve la localisation du mot, on sait où piocher notre mot rimant
    if (genre is not None) and (nombre is not None):
        ouPiocher = entreeDicoRimant[genre][nombre]

    # TEST
    # print(f"\n- Bassin ou nous allons-nous piocher : {ouPiocher}")

        if len(ouPiocher) > 1 :
            rand = random.randint(0, len(ouPiocher) - 1)
            return ouPiocher[rand]

def main():

    listeFicSource = ['brise-marine.txt', 'hugo-amour.txt', 'hugo-amour.txt', 'lamartine-a-un-enfant.txt' ]
    numficAModifier = random.randint(0, len(listeFicSource) - 1)
    ficAModifier = listeFicSource[numficAModifier]
    print(f"J'ai choisi le fichier : {ficAModifier}")

    ficLexiqueBrute = 'nom-lexique-brut.txt'
    listeMotsWithInfos = extractionDatas_FromLine_ToListOfTuples(ficLexiqueBrute)

    dicoRime_3pho = constructionOfRimeDict(listeMotsWithInfos, 3)
    dicoRime_2pho = constructionOfRimeDict(listeMotsWithInfos, 2)
    dicoRime_1pho = constructionOfRimeDict(listeMotsWithInfos, 1)

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
                # on sépare les signes de ponctuation des mots
                if mot[-1] in punct:
                    signe = mot[-1]
                    mot = mot[:-1]
                    newline.append(mot)
                    newline.append(signe)
                else:
                    newline.append(mot)

            for wordATransforme in newline :
                index = newline.index(wordATransforme)
                if wordATransforme in punct :
                    continue

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

            print(f"\n\n*** : {line}")
            newline = ' '.join(newline)
            print(f"+++ {newline}")

if __name__ == '__main__':
    main()
