import cv2
import numpy as np

imgGray = cv2.imread('C:\Mb_lwj\lena.jpg',0) #1번째 grayscale
'''
imgcolor = cv2.imread('C:\Mb_lwj\lena.jpg',cv2.IMREAD_COLOR)


height, width,channel= imgcolor.shape
imgGray = np.zeros((height, width), np.uint8)

for y in range(0,height ):
    for x in range(0,width):
        b = imgGray.item(y, x, 0)
        g = imgGray.item(y, x, 1)
        r = imgGray.item(y, x, 2)

        gray = (int(b) + int(g) + int(r)) / 3.0
        imgGray.itemset(y, x, gray)
       
'''


ret, dst = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('picture', dst)
cv2.imshow('picture1', imgGray)      

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
 