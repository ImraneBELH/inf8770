import cv2
import sys
import numpy as np
from utils import *
from huffman import HuffmanCoding


image = cv2.imread("Fichiers_TP2-2/data/kodim01.png", cv2.IMREAD_COLOR)

print(sys.getsizeof(image))

cv2.imshow("Normale", image)
initialeSize = sys.getsizeof(image)

## Etape 1: Transformation YC_rC_b
image = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("YCC", image)


# Etape 2 : echantillionage de l'image 4:2:0:
# source : https://medium.com/@sddkal/chroma-subsampling-in-numpy-47bf2bb5af83
image[1::2] = image[::2, :]
image[:, 1::2] = image[:, ::2]

img2 = image
chrominance(img2)

cv2.imshow("Subsampling- 1", image)
cv2.imshow("Subsampling- 2", img2)


# Etape 3: Decoupage en blocs
blocs = blocks(image)


#Etape3 : Dct sur chaque block:
for j in range(blocs.shape[1]):
    for i in range(blocs.shape[0]):
        blocs[i, j][:, :, 0] = cv2.dct(np.float32(blocs[i, j][:, :, 0]) / 255) * 255
        blocs[i, j][:, :, 1] = cv2.dct(np.float32(blocs[i, j][:, :, 1]) / 255) * 255
        blocs[i, j][:, :, 2] = cv2.dct(np.float32(blocs[i, j][:, :, 2]) / 255) * 255


#Etape 4 et 5: application de quantification et Zigzag sur chaque block

for j in range(blocs.shape[1]):
    for i in range(blocs.shape[0]):
        blocs[i,j] = zigzag(blocs[i,j])
        blocs_string = ''.join([str(elem) for elem in blocs[i,j]])
        compressed_bloc = HuffmanCoding.compress(blocs_string)
        ##print(compressed_bloc)

#Etape 6 huffman and RLE
# list = list(blocs)
# compressed_bloc = HuffmanCoding.compress(list)
# print(compressed_bloc)
print(sys.getsizeof(blocs))
#cv2.imshow("Normal", image)
#cv2.imshow("YCC", YCCimage)
cv2.waitKey()


