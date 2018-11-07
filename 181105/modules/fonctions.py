from lxml import etree
import re
import random

#========================================================
#=================== DATAS_RETRIEVING ===================
#========================================================

def recuperer_contenusSMS_et_ajouter_a_liste(BD_SMS, listeARemplir):
    """ Récupérer le contenu brut de notre fichier xml,
        et le rend en format liste.
        Entrée : fichier xml
        Sortie : list() """

    tree = etree.parse(BD_SMS)
    root = tree.getroot()

    # la méthode findall renvoie une liste avec tous les éléments correspondant au chemin argument
    p = root.findall("./tei:text/tei:body//tei:post/tei:p", namespaces={'tei':"http://www.tei-c.org/ns/1.0"})

    for elem in p:
        p_text = elem.xpath(".//text()", namespaces={'tei':"http://www.tei-c.org/ns/1.0"})
        text = "".join(p_text)
        text = re.sub(r'\n\s+', ' ', text)
        ## Mettre un espace avant les PONCTUATIONs
        text = re.sub(r'([?!,.]+)',r' \1 ', text)

        listeARemplir.append(text)

    nombreSMS = len(listeARemplir)
    print(f"\nNous avons un total de {nombreSMS:,d} SMS.")

def recuperer_listeMot_et_ajouter_a_ensemble(bd_lexique, ensembleARemplir):
    """ Récupérer le contenu brut de notre fichier lexique,
        et rend l'ensemble des orthographe.
        Entrée : fichier csv
        Sortie : ens() """

    with open(bd_lexique, mode='r') as filein:
        next(filein)

        for line in filein:
            word = line.split('\t')[0]
            ensembleARemplir.add(word)

    nombreMots = len(ensembleARemplir)
    print(f"Nous avons un total de {nombreMots:,d} mots issue de notre lexique.")

#==================================================
#=================== DATAS_SHOW ===================
#==================================================

def show_NbSMS_aTraiter(nombreSMS_aTraiter):
    print("\n--------------------------------------")
    print(f"Nous avons choisi {nombreSMS_aTraiter} sms au hasard.")

def show_5RandomSMS_aTraiter(nombreSMS_aTraiter, liste_N_SMS_auHasard):
    print("\n--------------------------------------")
    print(f"Nous avons choisi {nombreSMS_aTraiter} sms au hasard, donc voici les 5 premiers : ")
    for i, sms in enumerate(liste_N_SMS_auHasard[:5]) :
        print(f"{i} : {sms}")

def show_NbMotsHorsLexique(nombreSMS_aTraiter, ensembleDesMotsHorsLexique):
    print("\n--------------------------------------")
    print(f"Sur ces {nombreSMS_aTraiter} sms, nous avons {len(ensembleDesMotsHorsLexique)} mots hors lexique.")

def show_10RandomMotsHorsLexique(ensembleDesMotsHorsLexique):
    print("\n--------------------------------------")
    print(f"Prenons au hasard 10 mots :")
    for i, mot_et_contexte in enumerate(random.sample(ensembleDesMotsHorsLexique, 10)) :
        if len(mot_et_contexte) < 2 :
            continue
        mot = f"{mot_et_contexte[0]}"
        contexte = f"{mot_et_contexte[1]}"
        print(f"{i} - Mot : {mot}, Contexte : {contexte}")
