#!/usr/bin/env python3
#-*- coding : utf8 -*-

from operator import itemgetter
from collections import Counter

def extraire_Infinitifs_VerbesPremierGroupe(ficlexique, listeARemplir) :
    # Trois conditions pour être un infinitif du 1er groupe :
        # 1 : que le lemme soit l'orthographe (merci le français)
        # 2 : que la cgram soit VER (sinon abricotier (un nom) sera compté comme verbe)
        # 3 : que le lemme se termine par 'er' (marque du 1er groupe)

    with open(ficlexique, mode='r') as filein :

        for line in filein :
            ortho = line.split()[0]
            lemme = line.split()[2]
            cgram = line.split()[3]

            if (ortho == lemme) and (lemme.endswith('er')) and (cgram == 'VER') :
                listeARemplir.append(ortho)

def extraire_AdjectifsEnAble(ficlexique, listeARemplir) :
    # Deux conditions pour être un adjectif en able :
        # 1 : que l'orthographe se termine par '-able'.
        # 2 : par précaution, que la cgram soit ADJ.

    # Plus pour l'instant, nous ne voulons que les adjectifs 'affirmatifs' ou 'positifs' donc
        # ne commençant ni par 'im', ni par 'in'.

    with open(ficlexique, mode='r') as filein :

        for line in filein :
            ortho = line.split()[0]
            cgram = line.split()[3]
            freqlemfilms = line.split()[6]

            if (ortho.endswith("able")) and (cgram == 'ADJ') \
            and not (ortho.startswith("im") or ortho.startswith("in")):
                listeARemplir.append((ortho, freqlemfilms))

def trouver_lesContraires_desAdjectifs_enAble(ficlexique, listeReference, listeARemplir) :
    # Conditions pour être un infinitif du 1er groupe :
        # 1 : que l'ortho commence soit par 'im', soit par 'in'.
        # 2 : que le mot que l'on peut en extraire ('i(m|n) exclu') soit dans notre liste d'ajectifs en able.

    with open(ficlexique, mode='r') as filein :

        for line in filein :
            orthoNeg = line.split()[0]
            freqlemfilmsNeg = line.split()[6]
            orthoPos = orthoNeg[2:]

            if ((orthoNeg.startswith('im') or orthoNeg.startswith('in')) \
            and (orthoPos in map(itemgetter(0), listeReference))):

                # On va rechercher l'info freq sur l'adjectif positifs
                for t in listeReference :
                    if t[0] == orthoPos :
                        freqlemfilmsPos = t[1]

                # Pour nous faciliter le décompte plus tard
                if freqlemfilmsNeg > freqlemfilmsPos :
                    reponse = 'NegGagne'
                else:
                    reponse = 'PosGagne'

                listeARemplir.append((orthoNeg, freqlemfilmsNeg, orthoPos, freqlemfilmsPos, reponse))

def main():

    print(f"******* DEBUT *******")
    print(f"Bienvenue. Vous n'avez rien à faire, juste attendre.")

    # Pour ne pas se trimbaler ce gros fichier, on va construire de petites listes.

    infinitifs_PremierGroupe = []
    extraire_Infinitifs_VerbesPremierGroupe('lexique382.txt', infinitifs_PremierGroupe)

    adjectifsEnAble = []
    extraire_AdjectifsEnAble('lexique382.txt', adjectifsEnAble)

    contraires_adjectifsEnAble = []
    trouver_lesContraires_desAdjectifs_enAble('lexique382.txt', adjectifsEnAble, contraires_adjectifsEnAble)

    print(f"******* DECOMPTE *******")

    nbre_infinitifs = len(infinitifs_PremierGroupe)
    nbre_positifs_able = len(adjectifsEnAble)
    nbre_negatifs_able = len(contraires_adjectifsEnAble)

    print(f"On a : \n- {nbre_infinitifs} verbes du 1er groupe.")
    print(f"- {nbre_positifs_able} adjectifs en able ne commençant ni par in, ni par im.")
    print(f"- {nbre_negatifs_able} adjectifs négatifs dont les positifs existent dans notre liste d'ajectifs en able.")

    print(f"******* STATISTIQUES *******")

    pourcentage_infinitifs_with_Adj = round((nbre_positifs_able * 100) / nbre_infinitifs , 2)
    pourcentage_adjectifs_with_Neg = round((nbre_negatifs_able * 100) / nbre_positifs_able, 2)

    print(f"Nous avons ainsi {pourcentage_infinitifs_with_Adj} % des verbes ({nbre_positifs_able} de {nbre_infinitifs}) qui ont un adjectif en -able.")
    print(f"Parmi ces adjectifs, {pourcentage_adjectifs_with_Neg} % possédent un négatif ({nbre_negatifs_able} de {nbre_positifs_able}).")

    print(f"******* COMPARAISONS *******")

    nbreFreqTotal = len(contraires_adjectifsEnAble)
    c = Counter()

    for *args, reponse in contraires_adjectifsEnAble :
        if reponse == 'PosGagne' :
            c['pos'] += 1
        else :
            c['neg'] += 1

    nbreNeg_superieur_Pos = c['neg']
    nbrePos_superieur_Neg = c['pos']

    prcent_Neg_sup_Pos = round(nbreNeg_superieur_Pos * 100 / nbreFreqTotal, 2)

    print(f"Sur un total de {nbreFreqTotal} situations où nous avons aussi bien l'adjectif positif que celui négatif, on a : ")
    print(f"- {nbreNeg_superieur_Pos} fois où le dérivé négatif est plus fréquent dans 7_freqlemfilms2, soit {prcent_Neg_sup_Pos} %.")


    print(f"******* FIN *******")

    with  open('verbes.txt', mode='w') as target:
        for i in range(len(infinitifs_PremierGroupe)) :
            target.write(f"{i} : {infinitifs_PremierGroupe[i]}\n")

    with  open('adjectifs.txt', mode='w') as target:
        for i in range(len(adjectifsEnAble)) :
            target.write(f"{i} : {adjectifsEnAble[i]}\n")

    with  open('contraires.txt', mode='w') as target:
        for i in range(len(contraires_adjectifsEnAble)) :
            target.write(f"{i} : {contraires_adjectifsEnAble[i]}\n")

    print(f"J'ai enregistré trois fichiers 'verbes.txt', 'adjectifs.txt' et 'contraires.txt', où vous pouvez voir les extractions.")

if __name__ == '__main__':
    main()






#
