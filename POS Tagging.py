'''
    Author: Maria Alecu
    Date created: 11/11/2017
    Date last modified:  
    Python Version: 3.5
'''

import nltk
from nltk.tokenize import word_tokenize

from nltk.tree import Tree 
from nltk.chunk import ne_chunk
 
file = open("input_text2.txt")
#file = open('test_data_long.txt')
rawtext = file.read()

tokens = word_tokenize(rawtext)

words_pos_tags = nltk.pos_tag(tokens)
named_entities = [chunk for chunk in ne_chunk(words_pos_tags) if isinstance(chunk, Tree)]

named_entities_list = []

for entity in named_entities:
	if entity.label() == 'PERSON':
		person_name = ""
		for word, postag in entity.leaves():
			person_name += word + " "
		named_entities_list.append(person_name)

named_entities_list = list(set(named_entities_list))
named_entities_list = [ entity.strip() for entity in named_entities_list]

for i in named_entities_list:
	print(i)

anonymized_text = ""
i = 0
while i < len(tokens):
	token = tokens[i] 
	if token.isupper():
		for entity in named_entities_list:
			if entity.startswith(token):
				start_of_entity = token
				while start_of_entity != entity:
					i += 1
					start_of_entity += " " + tokens[i]
				anonymized_text += "****"	
				break 
	
	anonymized_text += token 
	i += 1
	 	

print(anonymized_text)


#######################################################################
# TODO:
# sentences = nltk.sent_tokenize(rawtext)
# tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
# tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
# chunked_sentences = nltk.ne_chunk(tagged_sentences, binary=True)