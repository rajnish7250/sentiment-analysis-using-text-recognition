#1. line 1 to 33 for text recognition
from pytesseract import pytesseract
import string
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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
text=ocr.extract("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\test6.png")
# print(text)
#Writing text to file
f = open("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\img2txt.txt", "w")
f.write(text)
f.close()
#open and read the file after the appending:
f = open("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\img2txt.txt")
print(f.read())
f.close()



#2.removing all punctuations in text recognition
text=text.translate(text.maketrans('','',string.punctuation))
withoutpunctuation= open("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\withoutpunctuation.txt", "w")
withoutpunctuation.write(text)
withoutpunctuation.close()



#3. Removing all stop words:
sw=set(stopwords.words('english'))
f=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\withoutpunctuation.txt')
get_txt=f.read()
#Removing all punctuations
quote=get_txt.translate(get_txt.maketrans('','',string.punctuation))
print(quote)
tokenized=word_tokenize(quote)
# filterated=[w for w in tokenized if not w in sw]
filterated=[]
#removing all stop words and making new list filterated without stop words
for w in tokenized:
    if w not in sw:
        filterated.append(w)
print(tokenized,'\n')
print('length of tokenized word is : ',len(tokenized),'\n')
print(filterated,'\n')
print('length of filterated word is : ',len(filterated),'\n')
f1=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\withoutstopwords.txt','w')
f1.write(' '.join(filterated))
f1.close()
f.close()


#4. Compare filterated word with english dictionary and making new list to store meaningful words
f=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\dictionary\\englishwords.txt')
c=f.read()
#converting dictionary words in to list
dictionary_list=c.split()
# print(dictionary_list)
#creating list for storing 1's and 0's , sample is in projectlink.xlx
li=list()
for words in filterated:
    words=words.lower()
    if words in dictionary_list:
        li.append(words)
print(li)
print('length of meaningful words: ',len(li))
f=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\meaningfulwords.txt','w')
f.write(' '.join(li))
f.close()
f.close()



#5.Sentimental analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def sentiment_scores(sentence):
	# Create a SentimentIntensityAnalyzer object.
	sid_obj = SentimentIntensityAnalyzer()

	# polarity_scores method of SentimentIntensityAnalyzer
	# object gives a sentiment dictionary.
	# which contains pos, neg, neu, and compound scores.
	sentiment_dict = sid_obj.polarity_scores(sentence)
	#Creating a new file to store sentiment 
	f=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\sentiment.txt','w')
	a="sentence was rated as  "+  str(sentiment_dict['neg']*100) +"% Negative\n"
	b="sentence was rated as " + str(sentiment_dict['neu']*100) + "% Neutral\n"
	c="sentence was rated as "+  str(sentiment_dict['pos']*100) + "% Positive\n"
	f.write(a)
	f.write(b)
	f.write(c)
	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
	d="Sentence Overall Rated As :  "
	f.write(d)
	print("Sentence Overall Rated As", end = " ")
	# decide sentiment as positive, negative and neutral
	if sentiment_dict['compound'] >= 0.05 :
		e="Positive"
		f.write(e)
		print("Positive\n")
	elif sentiment_dict['compound'] <= - 0.05 :
		e="Negative"
		f.write(e)
		print("Negative\n")
	else :
		e="Neutral"
		f.write(e)
		print("Neutral\n")
	f.write("\n\n\n\n\nThank You")
	f.close()
	return 
# Driver code
if __name__ == "__main__" :
	print("Statement :")
	f=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\meaningfulwords.txt')
	get_txt=f.read()
	quote=get_txt.translate(get_txt.maketrans('','',string.punctuation))
	print(quote)
	sentiment_scores(quote)
	



# #6. Text to speech Computer voice
# from gtts import gTTS
# import os
# f=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\sentiment.txt')
# mytext=f.read()
# # mytext='Hello bro this is rajnish kumar. Kaise ho sab khuch bhadiya chal raha hai kya '
# language='en'
# output=gTTS(text=mytext,lang=language, slow= False)
# output.save('output.mp3')
# os.system('start output.mp3')
# #End


