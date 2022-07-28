from sklearn.feature_extraction.text import CountVectorizer
corpus = [''') 5a WW) mor
as eat BT

��

7
y
x

| = The shone chariot =

History of the Chariot. The chariot was built by King Krishnadevaraya of the
Vijayanagara Empire during the 16th century, who got fascinated with
the Konark Sun temple chariot while fighting a battle in Odissa.

{
i
3

The Stone Chariot of Vittala Temple is actually a shrine that has been designed in
the shape of an ornamental chariot. The Vittala Temple or Vitthala Temple in
Hampi is an ancient monument that is well-known for its exceptional
architecture and unmatched craftsmanship.

You can still see the remains of the painting on the carvings of the chariot.

Probably because it was relatively protected from the natural weather elements,

undercarriage of the chariot spots one of the best preserved specimens of

| of paintings. it is believed the whole of the Vittala Temple�s sculptures were
ifully painted in similar fashion using the minerals as medium.

''' ]
vectorizer=CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(type(vectorizer.get_feature_names_out()))
print(X.toarray())
print(type(X.toarray()))
vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2,2 ))
X2 = vectorizer2.fit_transform(corpus) 
print(vectorizer2.get_feature_names_out())
print(X2.toarray())



