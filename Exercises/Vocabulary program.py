Text = 'Hello world, Im new to this place. Me a Computer Program. Are you a computer program? Can you give me a name? What is your name? Where do you come from? Are you my creator?'

Text_split = Text.split(' ')
##print(Text_split)

##### using for loop

##Vocabulary = {}
##
##for word in Text_split:
##    similar_words = [ x for x in Text_split if word == x]
##    Vocabulary[word] = len(similar_words)
##
##print(Vocabulary)
##print(len(Vocabulary))


##### Using Counter from collections library
##
##from collections import Counter
##
##Vocabulary = Counter(Text_split)
##
##print(Vocabulary)
##print(len(Vocabulary))
