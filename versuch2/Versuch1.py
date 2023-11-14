import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

cap = cv2.VideoCapture(0)

def produceIMG(path,grayscaleB:bool):
    
    ret, frame = cap.read()
    grayscale = rgb2gray(frame)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(grayscale, cmap=plt.cm.gray)
    ax.set_title("Grayscale")
    plt.show()
    if(not grayscaleB):
        cv2.imwrite(path, frame)
    else:
        cv2.imwrite(path, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

#produceIMG("./Bilder/grayscalePic.png",True);

#for i in range(0,10):
#    produceIMG("./Bilder/White"+str(i+1)+".png",False)





cap.release()
cv2.destroyAllWindows()


def readImg(path:str, x1, x2, y1, y2):
    M = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return M[x1:x2][y1:y2]

plt.plot(readImg("./Bilder/grayscalePic.png",0, -1, 0,-1))
plt.show()
#Settings: Brightness -6 Distance:30cm