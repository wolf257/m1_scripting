from lxml import etree
import re
import random
import pickle

#==============================================
#=================== PICKLE ===================
#==============================================

def load_dico_abbr(dicoAbbr, link) :
    with open(link, mode='rb') as filein:
        dicoAbbr = pickle.load(filein)

    return dicoAbbr

def dump_dico_abbr(dicoAbbr, link) :
    with open(link, mode='wb') as fileout:
        pickle.dump(dicoAbbr, fileout)

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

#==========================================================================
#=================== INIT DATAS (fonction de fonctions) ===================
#==========================================================================

def initialisation_des_donnees(listeDesSMS, ensembleMotsLexique, liste_N_SMS_auHasard, ensembleDesMotsHorsLexique, linkToficSMS, linkToficLexique) :

    listeDesSMS = listeDesSMS

    ensembleMotsLexique = ensembleMotsLexique

    #===================================
    recuperer_contenusSMS_et_ajouter_a_liste(linkToficSMS, listeDesSMS)

    #===================================
    recuperer_listeMot_et_ajouter_a_ensemble(linkToficLexique, ensembleMotsLexique)

    #===================================
    nombreSMS_aTraiter = 50

    liste_N_SMS_auHasard = liste_N_SMS_auHasard # no need, juste une habitude.
    liste_N_SMS_auHasard = random.sample(listeDesSMS, nombreSMS_aTraiter)

    show_NbSMS_aTraiter(nombreSMS_aTraiter)
    # mesfonctions.show_5RandomSMS_aTraiter(nombreSMS_aTraiter, liste_N_SMS_auHasard)

    #===================================
    ensembleDesMotsHorsLexique = ensembleDesMotsHorsLexique

    for sms in liste_N_SMS_auHasard :
        for word in sms.split() :
            # pour le len <= 4, c'est un choix arbitraire.
            # il est plutôt rare d'avoir une abbr de plus de 4 lettres.
            if (not word.lower() in ensembleMotsLexique) and (len(word) <= 4) and (word.isalpha()) :
                new_sms = ''.join([word.lower() for word in sms])
                mot_et_contexte = (word.lower(), new_sms)
                ensembleDesMotsHorsLexique.add(mot_et_contexte)

    show_NbMotsHorsLexique(nombreSMS_aTraiter, ensembleDesMotsHorsLexique)
    # mesfonctions.show_10RandomMotsHorsLexique(ensembleDesMotsHorsLexique)

#=====================================================================================
#=================== REMPLISSAGE DICO ABBR (fonction de fonctions) ===================
#=====================================================================================

def remplir_dicoAbbr_aPartir_ensHorsLexique(dicoAbbr, ensembleDesMotsHorsLexique, linkToDbAbbr):
    listeOut = []

    while (1 and len(ensembleDesMotsHorsLexique) > 0):
        # TEST
        # print(f"---- on a {len(dicoAbbr)} abbr. Up to the next.")

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

        # si on avait demandé à ne pas revoir le mot pendant cette session
        if mot in listeOut:
            continue

        # sinon, on peut commencer
        print(f"\n+++++++ NEW WORD +++++++")
        print(f"- Mot : {mot} \n- Contexte : {contexte}")

        a = input("\nOPTIONS : Écrivez la signification, ou \n- (s) si vous ne voulez plus le voir cette session - (0) si vous ne savez pas, - (enter) pour quitter \n\t Réponse : ")

        if isinstance(a, str) and len(a.strip()) > 1 :
            signification = a.strip()
            dicoAbbr[mot] = signification
            print(f"\n------- WORD ADDED -------")

            continue

        elif a.strip() == '0' :
            continue

        elif a.strip() == 's' :
            listeOut.append(mot)
            continue

        elif a.strip() == '' :
            dump_dico_abbr(dicoAbbr, linkToDbAbbr)
            print(f"\nAu revoir. J'ai enregistré le contenu de notre dictionnaire dans '{linkToDbAbbr}'")
            break

        else :
            print("Je n'ai pas compris, on reprend.")
