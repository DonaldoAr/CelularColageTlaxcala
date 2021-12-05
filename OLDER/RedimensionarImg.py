import numpy as np
import cv2
import time
# CARPETA A CON IMAGENES
readPath=r"./MosaicoPython/public/rel"
 
 # AImagen redimensionada
savePath=r"./MosaicoPython/public/Img"

files = 9
n = 0;    
# REDIMENSIONAR LA IMAGEN
for i in range(1,3):
    n+=1
    imgPath = readPath + r"/"+str(i)+".jpg" # Construir ruta de la imagen
    img = cv2.imread(imgPath)               # Leer la imagen a la memoria img variable
    image = cv2.resize(img, (960, 1080))      # 28, 28
    cv2.imwrite(savePath+r"/"+ str(i)+".jpg",image)
    
    
