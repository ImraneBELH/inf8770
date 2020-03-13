import cv2
import sys
import numpy as np
from utils import *
from huffman import HuffmanCoding
from rle import *
from decimal import *
import scipy.fftpack as dctpack


BLOCK_SIZE = 8

QUANT = np.matrix('16 11 10 16 24 40 51 61;\
    12 12 14 19 26 58 60 55;\
    14 13 16 24 40 57 69 56;\
    14 17 22 29 51 87 80 62;\
    18 22 37 56 68 109 103 77;\
    24 35 55 64 81 104 103 92;\
    49 64 78 77 103 121 120 101;\
    72 92 95 98 112 100 103 99').astype('float')

image = cv2.imread("Fichiers_TP2-2/data/kodim01.png", cv2.IMREAD_COLOR)

print(sys.getsizeof(image))

cv2.imshow("Normale", image)
initialeSize = sys.getsizeof(image)

## Etape 1: Transformation YC_rC_b
image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("canal Y", image[:,:,0])
cv2.imshow("Ycc", image)


# Etape 2 : echantillionage de l'image 4:2:0:
# # source : https://medium.com/@sddkal/chroma-subsampling-in-numpy-47bf2bb5af83
image[1::2] = image[::2, :]
image[:, 1::2] = image[:, ::2]

# img2 = image
# chrominance(image)

cv2.imshow("Subsampling", image)
# cv2.imshow("Subsampling- 2", img2)

# Etape 3: Decoupage en blocs
blocs = blocks(image)

print(sys.getsizeof(image))
#Etape3 : Dct sur chaque block:
image[:] -= 128
for bloc in blocs:
    # bloc[:, :, 0] = cv2.dct(np.float32(bloc[:, :, 0]) / 255) * 255
    # bloc[:, :, 1] = cv2.dct(np.float32(bloc[:, :, 1]) / 255) * 255
    # bloc[:, :, 2] = cv2.dct(np.float32(bloc[:, :, 2]) / 255) * 255
    BlocDCT = dctpack.dct(dctpack.dct(bloc[:, :, 0], axis=0, norm='ortho'), axis=1, norm='ortho')
    BlocDCT2 = dctpack.dct(dctpack.dct(bloc[:, :, 1], axis=0, norm='ortho'), axis=1, norm='ortho')
    BlocDCT3 = dctpack.dct(dctpack.dct(bloc[:, :, 2], axis=0, norm='ortho'), axis=1, norm='ortho')
    bloc[:, :, 0] = BlocDCT
    bloc[:, :, 1] = BlocDCT2
    bloc[:, :, 2] = BlocDCT3

print(sys.getsizeof(blocs))

jpegImage = []

zigzag_string = []

for bloc in blocs:
    #Etape 4 qunatification:
    bloc[:, :, 0] = np.round(np.divide(bloc[:, :, 0], QUANT))
    bloc[:, :, 1] = np.round(np.divide(bloc[:, :, 1], QUANT))
    bloc[:, :, 2] = np.round(np.divide(bloc[:, :, 2], QUANT))

    # Etape 5 zigzag
    zigzag_string.append(zigzag(bloc))

    # Etape 6 huffman and RLE
    # blocs_stringY = ''.join([str(elem) for elem in bloc[0]])
    # blocs_stringCb = ''.join([str(elem) for elem in bloc[1]])
    # blocs_stringCr = ''.join([str(elem) for elem in bloc[2]])
    # str_bloc = np.asarray(bloc).flatten().astype('str')
    # str_bloc = ''.join(str_bloc)
    # #print(blocs_stringCr)
    # rleBlock = RLE.compress(str_bloc)
    # rleBlock = str(int(rleBlock, 2))
    # huffmanBlock = HuffmanCoding.compress(rleBlock)
    # jpegImage.append(huffmanBlock)

rle_compress = RLE.compress(zigzag_string)
rle_ascii =''
for i in range(len(rle_compress)):
    rle_ascii += chr((int(rle_compress[i], 2)))
huffman_compress, dictionnaire = HuffmanCoding.compress(rle_ascii)
print(len(huffman_compress))

#Decompress




#cv2.imshow("Normal", image)
#cv2.imshow("YCC", YCCimage)
cv2.waitKey()


