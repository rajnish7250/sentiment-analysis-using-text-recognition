#to get meanings of any words from dictionary
from PyDictionary import PyDictionary
searchword=input("enter words to : ")
try:
    mydict=PyDictionary(searchword)
    print(mydict.getMeanings())
except:
    print('enter correct words')