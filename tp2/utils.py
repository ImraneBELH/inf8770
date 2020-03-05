
import numpy as np
import math

## takes in RGB pixels
def RGBtoYCCPixel(pixel):

    Y = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
    C_b = 128 + 0.564 * (pixel[2] - Y)
    C_r = 128 + 0.713 * (pixel[0] - Y)

    return [Y, C_b,  C_r]

def yccToRgPixel(pixel):

    R = pixel[0] + 1.403 * (pixel[2] - 128)
    G = pixel[0] - 0.714 * (pixel[2] - 128) - 0.344 * (pixel[1] - 128)
    B = pixel[0] + 1.773 * (pixel[1] - 128)

    return [R, G, B]


def toblocs(image):
    im = np.array(image)
    m = int(len(image)/16)
    n = int(len(image[0])/16)
    idxs = np.zeros((m,n))
    idxs = idxs.tolist()

    for i in range(m):
        for j in range(n):
            idxs[i][j] = (i*16, j*16)

    idxs = np.array(idxs)

    return [[ im[coord[0]:coord[0]+16,coord[1]:coord[1]+16].tolist() for coord in coord_row ] for coord_row in idxs ]

# def toDTCblock(block):
#     for i in range(16):
#         for j in range(16):
#             #math.cos(math.pi*(2*))


def toDCTimage(imagesBloc):
    pass

def quantification(DTC):
    pass