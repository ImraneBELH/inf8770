import numpy as np
import re
class RLE():

    #source : https://github.com/gabilodeau/INF8770/blob/master/Codage%20par%20plage.ipynb
    def compress(Message):
        compteur = 4  # La meilleure taille pour ce message est 4 bits. Plusieurs courtes répétitions
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
        print(dictionnaire)

        i = 0;
        MessageCode = []
        longueur = 0
        while i < len(Message):
            carac = Message[i]  # caractere qui sera codé
            repetition = 1
            # Calcul le nombre de répétitions.
            i += 1
            # tient compte de la limite du compteur
            while i < len(Message) and repetition < 2 ** compteur and Message[i] == carac:
                i += 1
                repetition += 1
            # Codage à l'aide du dictionnaire
            coderepetition = "{:b}".format(repetition - 1).zfill(compteur)
            codebinaire = dictbin[dictsymb.index(carac)]
            MessageCode += [coderepetition, codebinaire]
            longueur += len(codebinaire) + len(coderepetition)


    #source : https://exercism.io/tracks/python/exercises/run-length-encoding/solutions/b9efc25fffb046dba96b3705fe3c7ee7
    def decompress(string):
        if string == '':
            return ''
        multiplier = 1
        count = 0
        rle_decoding = []

        rle_encoding = []
        rle_encoding = re.findall(r'[A-Za-z]|-?\d+\.\d+|\d+|[\w\s]', string)
        for item in rle_encoding:
            if item.isdigit():
                multiplier = int(item)
            elif item.isalpha() or item.isspace():
                while count < multiplier:
                    rle_decoding.append('{0}'.format(item))
                    count += 1
                multiplier = 1
                count = 0
        return (''.join(rle_decoding))

