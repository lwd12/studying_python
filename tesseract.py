import cv2 
from PIL import Image
import pytesseract
from gtts import gTTS

import playsound


filename = 'C:\Mb_lwj\output.mp3'
def speak(text):
     tts = gTTS(text=text, lang='ko')
     tts.save(filename)
     playsound.playsound(filename)



pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

myConfig = ('-l kor --oem 3 --psm 4')
str = pytesseract.image_to_string(Image.open('C:/image.jpg'), config=myConfig)


print(str)
speak(str)



 