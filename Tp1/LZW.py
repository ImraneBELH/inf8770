
import numpy as np


def codageLZW(Message):
    dictsymb = [Message[0]]
    dictbin = ["{:b}".format(0)]
    nbsymboles = 1
    for i in range(1, len(Message)):
        if Message[i] not in dictsymb:
            dictsymb += [Message[i]]
            dictbin += ["{:b}".format(nbsymboles)]
            nbsymboles += 1

    longueurOriginale = np.ceil(np.log2(nbsymboles)) * len(Message)

    for i in range(nbsymboles):
        dictbin[i] = "{:b}".format(i).zfill(int(np.ceil(np.log2(nbsymboles))))

    dictsymb.sort()
    dictionnaire = np.transpose([dictsymb, dictbin])

    i = 0;
    MessageCode = ""
    longueur = 0
    while i < len(Message):
        precsouschaine = Message[i]
        souschaine = Message[i]

        while souschaine in dictsymb and i < len(Message):
            i += 1
            precsouschaine = souschaine
            if i < len(Message):  # Si on a pas atteint la fin du message
                souschaine += Message[i]

        codebinaire = dictbin[dictsymb.index(precsouschaine)]
        MessageCode += codebinaire
        longueur += len(codebinaire[0])
        if i < len(Message):
            dictsymb += [souschaine]
            dictbin += ["{:b}".format(nbsymboles)]
            nbsymboles += 1

        # Ajout de 1 bit si requis
        if np.ceil(np.log2(nbsymboles)) > len(MessageCode[-1]):
            for j in range(nbsymboles):
                dictbin[j] = "{:b}".format(j).zfill(int(np.ceil(np.log2(nbsymboles))))

    return MessageCode, longueur


