#imgtotxt
from pytesseract import pytesseract
import os
import string


class OCR:
    def __init__(self):
        self.path=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    def extract(self,filename):
        try:
            pytesseract.tesseract_cmd=self.path

            text=pytesseract.image_to_string(filename)
            return text
        except Exception as e:
            print(e)
            return "Error"

ocr=OCR()
text=ocr.extract("test10.png")
# print(text)
#Writing text to file
f = open("img2txt.txt", "w")
f.write(text)
f.close()
#open and read the file after the appending:
f = open("img2txt.txt")
print(f.read())
f.close()

text=text.translate(text.maketrans('','',string.punctuation))
li=text.split()
print(li)


#imgtobox

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('test10.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#
#for printing words present in images #
# print(pytesseract.image_to_string(img))
x=pytesseract.image_to_string(img)
#Writing text to file
f = open("img2box.txt", "w")
f.write(x)
f.close()
#open and read the file after the appending:
f = open("img2box.txt")
print(f.read())
f.close()


y=x.split()
print(y)
