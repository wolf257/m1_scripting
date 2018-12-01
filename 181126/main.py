#!/usr/bin/env python3
# -*- coding : utf8 -8-

import modules.operation_conll as op


ficConll = 'fr_gsd-ud-test.conllu'


def main():
    dicoInfos = {}
    dicoInfos = op.retrieveInfos(ficConll, dicoInfos)

    op.print_dataDico(dicoInfos)
    op.which_POS(dicoInfos)


if __name__ == '__main__':
    main()
