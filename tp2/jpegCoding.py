import cv2
import numpy as np

from utils import RGBtoYCCPixel

image = cv2.imread("Fichiers_TP2-2/data/kodim01.png", cv2.IMREAD_COLOR)
compressed = np.ndarray(image.shape)
rows,cols,_ = image.shape

for i in range(rows):
    print(i)
    for j in range(cols):
        compressed[i][j] = RGBtoYCCPixel(image[i][j])

cv2.imshow("Normal", image)
cv2.imshow("YCC", compressed)
cv2.waitKey()

print(compressed)