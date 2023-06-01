import cv2, pafy
from PIL import Image
import pytesseract
from gtts import gTTS
import numpy as np

url = 'https://www.youtube.com/watch?v=JdILVmHu290'
video = pafy.new(url)

best  = video.getbest()
#documentation: https://pypi.org/project/pafy/

capture = cv2.VideoCapture(best.url)
while(True):

    check, frame = capture.read()
    
    
   

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,200)
    cv2.imshow('edges',edges)
    cv2.imshow('FRAME',frame)

    '''
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

    myConfig = ('-l kor --oem 3 --psm 4')
    str = pytesseract.image_to_string(Image.open(edges), config=myConfig)
    '''
    key = cv2.waitKey(10)
    if key == 27: # Esc
        break

capture.release()
cv2.destroyAllWindows()