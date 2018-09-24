#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def main():
    mot = str(input("Quel est votre phrase : ")).lower()

    vowels = 'iuoaeéèê'

    compteur_voyelle, term_v =  0 , ''
    compteur_consonne, term_c = 0, ''
    compteur_ovni, term_o = 0, ''

    for lettre in mot :
        if lettre.isalpha() :
            if lettre in vowels :
                compteur_voyelle += 1
            else :
                compteur_consonne +=1
        else :
            if not lettre.isspace() :
                compteur_ovni += 1

    # juste question d'esthétique :-)
    if compteur_voyelle :
        term_v = 's'
    if compteur_consonne :
        term_c = 's'
    if compteur_ovni :
        term_o = 's'

    print("Le mot ou la phrase \"{}\" contient : {} voyelle{}, {} consonne{}, et {} objet{} non-identifié{}.".format(mot, str(compteur_voyelle), term_v, str(compteur_consonne), term_c , compteur_ovni, term_o, term_o ))


if __name__ == '__main__':
    main()
