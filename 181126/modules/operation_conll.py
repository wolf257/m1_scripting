from collections import Counter


def retrieveInfos(ficConll, dicoInfos):
    dico = dicoInfos
    dico.setdefault('nbPhrases', 0)
    dico.setdefault('nbMots', 0)
    dico.setdefault('POS', {})
    with open(ficConll, mode='r') as filein:
        for line in filein:
            if line.startswith('#'):
                pass
            elif line.strip() == "":
                dico['nbPhrases'] += 1
            elif line.strip()[0].isdigit():
                dico['nbMots'] += 1
                pos = line.split()[3]
                if pos.strip().isdigit():
                    continue
                dico['POS'].setdefault(pos, 0)
                dico['POS'][pos] += 1

    return dico


def print_dataDico(dico):

    print(f"Notre fichier compte {dico['nbPhrases']} phrases.")
    print(f"Notre fichier compte {dico['nbMots']} mots.")


def which_POS(dico):
    print(f"\nVous les POS disponibles dans notre base :")
    for key in dico['POS'].keys():
        print(key, end='  ')

    listPOS = list(dico['POS'].keys())

    while 1:
        pos = input(f"\n\nQuelle est la catégorie morphosyntaxique qui vous intéresse (enter pour quitter) :  ")

        pos = pos.upper()

        if pos.strip() == '':
            break
        elif pos.strip() in listPOS:
            print(f"\nNous avons {dico['POS'][pos]} mots de POS : {pos}")
        else:
            print(f"\nIl y a une erreur je pense. {pos} n'existe pas dans la base. On réessaye.")

if __name__ == '__main__':
    print("Vous ne voudriez pas appeler mon supérieur hiérarchique ? :-)")
