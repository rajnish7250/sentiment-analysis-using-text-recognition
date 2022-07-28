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