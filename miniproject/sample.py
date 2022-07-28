import string
text='Catalog #273 lists 5 @ $2.07, 31 @ $8.40, 62 @ $2.10, and 69 @ $1.90. Catalog #273 lists 3 @ $1.07, 37 @ $6.86, 65 @ $3.10, and 99 @ $2.02. A salary bonus of 64% announced by Saul & Benjamin was welcomed. On 8/12/11 he got 20# of bricks @ $3.32, an increase of 63%.'
print('\n\n\n',text,'\n\n\n')
text=text.translate(text.maketrans('','',string.punctuation))
withoutpunctuation= open("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\withoutpunctuation.txt", "w")
print(text,'\n\n\n')


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