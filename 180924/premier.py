#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def main() :
    a = int(input("Donnez votre nombre : "))

    premier = True
    list_diviseur = []

    for nombre in range(2, int(math.sqrt(a))):
        if a % nombre == 0 :
            premier = False
            list_diviseur.append(nombre)

    if premier :
        print("\n{} est un nombre premier.".format(a))
    else :
        print("\n{} n'est pas un nombre premier.".format(a))
        print("""En plus de 1 et lui-même, il est au moins divisible par : {}.
        """.format(', '.join(map(str, list_diviseur))))

    print("\n=== Au revoir ===\n")

if __name__ == '__main__':
    main()
