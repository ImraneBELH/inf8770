import numpy as np


def CodagePlage(compteur, Message):
    dictsymb = [Message[0]]
    dictbin = ["{:b}".format(0)]
    nbsymboles = 1
    for i in range(1, len(Message)):
        if Message[i] not in dictsymb:
            dictsymb += [Message[i]]
            dictbin += ["{:b}".format(nbsymboles)]
            nbsymboles += 1

    longueurOriginale = np.ceil(np.log2(nbsymboles)) * len(Message)  # Longueur du message avec codage binaire

    for i in range(nbsymboles):
        dictbin[i] = "{:b}".format(i).zfill(int(np.ceil(np.log2(nbsymboles))))

    dictsymb.sort()
    dictionnaire = np.transpose([dictsymb, dictbin])

    i = 0;
    MessageCode = []
    longueur = 0
    while i < len(Message):
        carac = Message[i]
        repetition = 1
        i += 1
        # tient compte de la limite du compteur
        while i < len(Message) and repetition < 2 ** compteur and Message[i] == carac:
            i += 1
            repetition += 1
        coderepetition = "{:b}".format(repetition - 1).zfill(compteur)
        codebinaire = dictbin[dictsymb.index(carac)]
        MessageCode += [coderepetition, codebinaire]
        longueur += len(codebinaire) + len(coderepetition)

    return MessageCode, longueur, longueurOriginale