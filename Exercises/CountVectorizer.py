from collections import Counter
import pandas as pd
import numpy as np

#sample data
list_of_sentences = ['I hate eggs',
                     'I hate bananas',
                     'Love and Hate',
                     'Dammit! I hate eggs!'
    ]

##Vocabulary = Counter((' '.join(list_of_sentences)).split(' '))
##
##size_of_vocab = len(Vocabulary)

###all the words in the list_of_sentences
bag_of_words = list(set(' '.join(list_of_sentences).split(' ')))

### empty dictionary
d1 = {}

### Filling up the dictionary
for sentence in list_of_sentences:
##    print('sentence : ',sentence)
    for word in bag_of_words:
##        print('word : ',word)
        similar_words = [ x for x in sentence.split() if word == x]
##        print('similar : ',similar_words)
        if d1.get(word):
            d1[word] = d1[word] + [0 if len(similar_words) == 0 else len(similar_words)]
        else:
            d1[word] = [len(similar_words)]
##print(d1)

### dictionary of sentences
d2 = {'sentences':list_of_sentences}

### adding both the dictionaries
d1 = {**d2, **d1}

print(d1)

### creating a dataframe

vector_df = pd.DataFrame(d1)
print(vector_df)
