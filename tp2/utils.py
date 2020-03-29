import numpy as np

def blocks(image):
    image = np.array(image)
    m = int(len(image)/ 8)
    n = int(len(image[0])/8)
    im = np.zeros((m,n), dtype=object)

    for i in range(m):
        for j in range(n):
            im[i,j] = image[i:i+8, j:j+8,:]
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


def chrominance(im):
    for row in range(im.shape[0]):
        for col in range(im.shape[1]):
            oldi = row
            oldj = col
            if (row % 2 == 1):
                oldi = row - 1
            if (col % 2 == 1):
                oldj = col - 1
            im[row][col][1] = im[oldi][oldj][1]
            im[row][col][2] = im[oldi][oldj][2]

