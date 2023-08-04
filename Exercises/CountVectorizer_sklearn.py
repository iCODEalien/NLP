from sklearn.feature_extraction.text import CountVectorizer

corpus = ['I hate snakes',
          'I hate crocodiles',
          'Love cats and hate snakes',
          'I love cats']

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())

print(X)
print(X.toarray())
