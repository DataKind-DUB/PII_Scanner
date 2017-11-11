import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

file = open('/Users/Swagat/Desktop/Semester 1/Text Analytics/Practical 2/Input_text2.txt')
rawtext = file.read()
tokens = word_tokenize(rawtext)

#x = WordNetLemmatizer()
j = []

words = nltk.pos_tag(tokens)
#for i in words:j.append(x.lemmatize(i))

print(words)
