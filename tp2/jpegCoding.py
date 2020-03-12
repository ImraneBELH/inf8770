import cv2
import numpy as np

def blocks(image):
    image = np.array(image)
    m = int(len(image)/ 16)
    n = int(len(image[0])/16)
    im = np.zeros((m,n), dtype=object)
    #print(image[16:32, 48:64, 1])
    print(im)

    for i in range(m):
        for j in range(n):
            im[i,j] = image[i:i+16, j:j+16,:]
    return im

def zigzag(block):
    est = True
    south = False
    west = False
    north = False

    stack = []
    i = 0
    j = 0
    stack.append(block[0, 0])
    while not(i == 7 and j == 7):
        if est:
            i = i + 1
        if west:
            i = i - 1
        if south:
            j = j + 1
        if north:
            j = j - 1

        stack.append(block[j, i])

        if i == 0 and j != 7:
            if not west:
                est = True
                south = False
                north = True
            else:
                west = False
            continue
        if j == 0:
            if not north :
                est = False
                west = True
                south = True
            else:
                north = False
                continue
        if j == 7:
            if south:
                west = False
                est = True
                south = False
                north = False
            else:
                north = True
            continue

        if i == 7 and j != 0:
            if est:
                est = False
                north = False
                south = True
            else:
                west = True
    return stack

image = cv2.imread("Fichiers_TP2-2/data/kodim01.png", cv2.IMREAD_COLOR)

## Etape 1: santillionage de l'image 4:2:0:
# source : https://medium.com/@sddkal/chroma-subsampling-in-numpy-47bf2bb5af83
image[1::2] = image[::2, :]
image[:, 1::2] = image[:, ::2]
cv2.imshow("subsampling", image)

# transformation YC_rC_b

YCCimage = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
cv2.imshow("YCC", YCCimage)

# Etape 2: Decoupage en blocs
blocs = blocks(image)
print(blocs.shape)

#Etape3 : Dct sur chaque block:
for j in range(blocs.shape[1]):
    for i in range(blocs.shape[0]):
        blocs[i, j][:, :, 0] = cv2.dct(np.float32(blocs[i, j][:, :, 0]) / 255)
        blocs[i, j][:, :, 1] = cv2.dct(np.float32(blocs[i, j][:, :, 1]) / 255)
        blocs[i, j][:, :, 2] = cv2.dct(np.float32(blocs[i, j][:, :, 2]) / 255)

print(blocs[29,1][:,:,0])

# etape 4
m = 0
x = np.zeros((8,8))

for i in range(8):
    for j in range(8):
        x[i,j] = m
        m = m + 1

#Etape 5 : Zigzag
# todo zigzag for each block


#etape 6



#cv2.imshow("Normal", image)
#cv2.imshow("YCC", YCCimage)
cv2.waitKey()


