import cv2
import numpy as np
img1 = cv2.imread("tlaxcalaFin.jpg")
img2 = cv2.imread("fondo.jpg")
print(np.shape(img1))
print(np.shape(img2))
# TAMAÑO DE LA IMAGEN (MATRIZ) DE MOZAICO
# s = np.shape(img)  # tamaño de matriz (756, 1920, 3)
total = cv2.addWeighted(src1=img1, alpha=1, src2=img2, beta=0.5, gamma=0)
cv2.imwrite("fin.jpg",total)
cv2.imshow('', total)
cv2.waitKey(0)
