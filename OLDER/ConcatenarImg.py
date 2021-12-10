import cv2
import numpy as np

readPath = r"./MosaicoPython/public/Img"

# lEEMOS IMAGEN QUE VA A OCUPAR EL MOSAICO
img = cv2.imread("tlax1.bmp")
# TAMAÑO DE LA IMAGEN (MATRIZ) DE MOZAICO
s = np.shape(img)  # tamaño de matriz (756, 1920, 3)
imgMo = cv2.imread("./MosaicoPython/public/Img/1.jpg")
# TAMAÑO DE MATRIZ DE IMAGEN CHICA
size_imgMo = np.shape(imgMo)  # (90, 160, 3)
final = np.zeros((1080, 1920, 3), dtype=np.uint8)
# final = np.zeros((1080, 1920, 3))
Reg = int(1080 / size_imgMo[0])
Col = int(1920 / size_imgMo[1])

im = 1
for reg in range(12):
    for col in range(12):
        # print(reg,col)
        little = cv2.imread(readPath+r"/"+str(im)+".jpg")
        concat_h1 = cv2.hconcat([little])
        final[reg * 90: (reg + 1) * 90, col * 160: (col+ 1) * 160] = concat_h1
        im += 1
        if im == 8:
            im = 1
    concat_v = cv2.vconcat([concat_h1])

cv2.imwrite("tlaxcalaFin.jpg",final)
cv2.imshow('', final )
cv2.waitKey(0)
