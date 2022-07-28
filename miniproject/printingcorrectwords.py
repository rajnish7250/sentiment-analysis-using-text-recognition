#from PyDictionary import PyDictionary
#from english_words import english_words_set

#dic=PyDictionary()

#Accessing any files 
f=open('img2txt.txt')
di=dict()
count=0
for line in f:
    line=line.rstrip()
    li=line.split()
    for words in li:
        di[words]=di.get(words,0)+1
print(di)

di2=dict()
f=open('englishwords.txt')
print('Complete words')
for line in f:
    line=line.rstrip()
    for i in di:
        if i.lower()==line:
            di2[i]=1
        #     continue
        # else:
        #     print(i,'0')
        #     continue
print(di2)
    



# word=input("enter words to search fro meaning: ")
# try:
#     meaning=dict.meaning(word)
#     print(meaning)
# except:
#     print("Enter valid words: ")