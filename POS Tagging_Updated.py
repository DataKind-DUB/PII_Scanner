import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
from nltk.chunk import ne_chunk


file = open('/Users/Swagat/Desktop/PII Scanner/Input_text2.txt')
rawtext = file.read()
tokens = word_tokenize(rawtext)

#x = WordNetLemmatizer()
j = []

tokens_with_pos = nltk.pos_tag(tokens)
#for word, postag in tokens_with_pos:
#    if postag == "NNP":
#        print(word, postag)


#print(word_count(word))
#for i in words:j.append(x.lemmatize(i))

#print(words)

print("---------------------")
print("Named entities")
print()

named_entities = [chunk for chunk in ne_chunk(tokens_with_pos) if isinstance(chunk, Tree)]
for i in named_entities:
    print(i)


#[i[0] for i in list(chain(*[chunk.leaves() for chunk in ne_chunk(tagged_sent) if isinstance(chunk, Tree)]))]
#['Michael', 'Jackson', 'Daniel']


#print(word_count(named_entities))
