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
text=ocr.extract("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\test12.jpg")
# print(text)
#Writing text to file
f = open("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\img2txt.txt", "w")
f.write(text)
f.close()
#open and read the file after the appending:
f = open("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\img2txt.txt")
print(f.read())
f.close()

text=text.translate(text.maketrans('','',string.punctuation))
li=text.split()
print(li)





