import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#for reading image
img=cv2.imread('C:\\Users\\Rajni\\Desktop\\Emotional photos\\img1.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
x=pytesseract.image_to_string(img)
#Writing text to file
f = open("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\img2box.txt", "w")
f.write(x)
f.close()
#open and read the file after the appending:
f = open("img2box.txt")
print(f.read())
f.close()


y=x.split()
print(y)

print(pytesseract.image_to_boxes(img))
hImg,wImg,_=img.shape
# cong=r'--oem 3 --psm 6 outputbase digits'
boxes=pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    # print(b)
    b=b.split(' ')
    print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,hImg-y+0),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

# cv2.imshow('Result',img)
# cv2.waitKey(0)






#2nd part program
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
sw=set(stopwords.words('english'))
f=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\img2box.txt')
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




#Creating dictionary of all recognised words
di=dict()
for words in filterated:
    di[words]=di.get(words,0)+1
print(di)















#comparing recognised words with english dictionary and printing it to list as1=if recognised words is present in english dictionary else 0
f=open('C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\dictionary\\englishwords.txt')
c=f.read()
#converting dictionary words in to list
dictionary_list=c.split()
# print(dictionary_list)
#creating list for storing 1's and 0's , sample is in projectlink.xlx
li=list()
for words in di:
    words=words.lower()
    if words in dictionary_list:
        li.append(1)
    else:
        li.append(0)
#for printing 1's and 0's
print(li)






#counting no of 1's and 0's present using dictionary
count_dict=dict()
for i in li:
    count_dict[i]=count_dict.get(i,0)+1
print('count_dict: ',count_dict)






#finding accuracy 
if 0 not in count_dict:
    count_dict[0]=0
    one=(count_dict[1])/((count_dict[0])+(count_dict[1]))*100
    zero=(count_dict[0])/((count_dict[0])+(count_dict[1]))*100
    print('Accuracy: ',one,'%')
    print('Error: ',zero,'%')
else:
    one=(count_dict[1])/((count_dict[0])+(count_dict[1]))*100
    zero=(count_dict[0])/((count_dict[0])+(count_dict[1]))*100
    print('Accuracy: ',one,'%')
    print('Error: ',zero,'%')



#building a synonyms for dictionary like happy end excited
#happy word list
happy=['happy','cheerful','contented','delighted','ecstatic','elated','glad','joyful','jubilant','lively','merry','overjoyed','peaceful','pleasant','pleased','satisfied','thrilled','upbeat','blessed','blest','blissful','blithe','captivated','chipper','chirpy','content','convivial','exultant','flying high','gay','gleeful','gratified','intoxicated']
happy.append('good')
happy.append('kind')
happy.append('loving')
happy.append('success')
happy.append('smile')
#sad wordlist
sad=['sad','bitter'
,'dismal'
,'heartbroken'
,'melancholy'
,'mournful'
,'pessimistic'
,'somber'
,'sorrowful'
,'sorry'
,'unhappy'
,'wistful'
,'bereaved'
,'blue'
,'cheerless'
,'dejected'
,'depressed'
,'despairing'
,'despondent'
,'disconsolate'
,'distressed'
,'doleful'
,'down'
,'down in dumps'
,'down in the mouth'
,'downcast'
,'forlorn']
sad.append('never')
sad.append('realize')
sad.append('struggle')

#neutal wordslist
neutral=['disinterested'
,'evenhanded'
,'fair-minded'
,'inactive'
,'indifferent'
,'nonaligned'
,'nonpartisan'
,'unbiased'
,'uncommitted'
,'undecided'
,'uninvolved'
,'calm'
,'cool'
,'noncombatant'
,'aloof'
,'bystanding'
,'clinical'
,'collected'
,'detached'
,'disengaged'
,'dispassionate'
,'easy'
,'impersonal'
,'inert'
,'middle-of-road'
,'nonbelligerent'
,'nonchalant'
,'nonparticipating'
,'on sidelines'
,'on the fence'
,'pacifistic'
,'poker-faced'
,'relaxed'
,'unaligned'
,'unconcerned'
,'unprejudiced']
# print(neutral)



happy_count=0
sad_count=0
neutral_count=0
for words in di:
    if words.lower() in happy:
        happy_count+=1
    elif words.lower() in sad:
        sad_count+=1
    elif words.lower() in neutral:
        neutral_count+=1
print('Happy count: ',happy_count)
print('Sad count: ',sad_count)
print('Neutral count: ',neutral_count)
if happy_count>sad_count:
    print('Emotions of Images are: Happy Happy')
elif sad_count>happy_count:
    print('Emotions of Images are: Sad Sad')
else:
    print('Emotions of Images are:  Neutral')