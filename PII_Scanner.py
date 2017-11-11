#!/usr/bin/python3 -i
'''
    Authors: Maria Alecu, Morgane Mahaud, Prasad Pore, Swagat Mhaske, Jeet J., Christopherpraveen
    Date created: 11/11/2017
    Date last modified:  
    Python Version: 3.5
'''

import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
from nltk.chunk import ne_chunk
from namelist import txt_to_set

def print_names(filename):
	"""(str) -> None
	Find all the names into a text file and print them into the terminal
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
		tokens = word_tokenize(rawtext)
		tokens_with_pos = nltk.pos_tag(tokens)
		print("---------------------")
		print("Named entities")
		print()
		named_entities = [chunk for chunk in ne_chunk(tokens_with_pos) if isinstance(chunk, Tree)]
		for i in named_entities:
			print(i)
			
			
def 
			
	
def replace_proper_names(filename, outputfile = None, replacetoken = '***'):
	"""(str) -> None
	Replace all proper names by replacetoken (defaut ***)
	if outputfile, the file is not rewritten but an new file output is written 
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
	tokens = word_tokenize(rawtext)
	tokens_with_pos = nltk.pos_tag(tokens)
	if not outputfile: outputfile = filename
	with open(outputfile, 'w') as f:
		for tok in tokens_with_pos:
			if tok[1] == 'NNP': f.write(replacetoken+' ')
			else: f.write(tok[0]+' ')
	
			
def replace_person_names(filename, outputfile = None, replacetoken = '***'):
	"""(str) -> None
	Replace all person names by replacetoken (defaut ***)
	if outputfile, the file is not rewritten but an new file output is written 
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
	tokens = word_tokenize(rawtext)
	tokens_with_pos = nltk.pos_tag(tokens)
	person_entities = set([chunk for chunk in ne_chunk(tokens_with_pos) if isinstance(chunk, Tree)])
	first_parts = set([item.split()[0] for item in person_entities])
	maxlen = max(len(x) for x in person_entities)
	buff = []#buffer of tokens
	maybename = False
	if not outputfile: outputfile = filename
	with open(outputfile, 'w') as f:
		for tok in tokens:
#			if uppercase
			if tok in first_parts: maybename = True#add token in the buffer
			if maybename: buff.append(tok) #add token in the buffer
			else: f.write(tok+' ')
			if len(buff) == maxlen:#check if the name in the buffer is in the list
				is_buff_in_person_entities(buff, person_entities)
				
def is_buff_in_person_entities(buff, person_entities):
	if buff in person_entities: 
		f.write(' '.join(buff)+' ')
	else: 
		is_buff_in_person_entities(buff[:-1], person_entities)

		
def replace_person_names_maria(filename, outputfile = None, replacetoken = '***'):
	"""(str) -> None
	Replace all person names by replacetoken (defaut ***)
	if outputfile, the file is not rewritten but an new file output is written 
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
	tokens = word_tokenize(rawtext)
	tokens_with_pos = nltk.pos_tag(tokens)
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
					anonymized_text += replacetoken	
					break 
			anonymized_text += token 
		i += 1
	if not outputfile: outputfile = filename
	with open(outputfile, 'w') as f: f.write(anonymized_text)
	



			
#def replace_person_names(filename, outputfile = None, replacetoken = '***'):
#	"""(str) -> None
#	Replace all person names by replacetoken (defaut ***)
#	if outputfile, the file is not rewritten but an new file output is written 
#	"""
#	with open(filename, 'r') as f:
#		rawtext = f.read()
#	tokens = word_tokenize(rawtext)
#	tokens_with_pos = nltk.pos_tag(tokens)
#	person_entities = set([chunk for chunk in ne_chunk(tokens_with_pos) if isinstance(chunk, Tree)])
#	first_parts = set([item.split()[0] for item in person_entities])
#	dic_person_entities = {}
#	maxlen = 0
#	for item in person_entities:
#		lenitem = len(item)
#		if lenitem > maxlen: maxlen = lenitem
#		try: dic_person_entities[lenitem].append(item)
#		except KeyError: dic_person_entities[lenitem] = [item]
#	buff = []#buffer of tokens
#	maybename = False
#	nbtokinbuff = 1#number of token in the buffer
#	if not outputfile: outputfile = filename
#	with open(outputfile, 'w') as f:
#		for tok in tokens:
#			if tok in first_parts: 
#				maybename = True
#				buff.append(tok)#write what is in the buffer
#				buff = ''#clean the buffer
#			if maybename and c == ' ':
#				lenbuff = len(buff)
#				try: 
#					if buff in dic_person_entities[lenbuff]: pass#check if the name in the buffer is in the list
#						#if yes, replace the buffer by replacetoken and continue
#						#if not, write the first word and check if the rest of the buffer is in the list 
#				except KeyError: pass
#			tmp += c
#		for tok in tokens_with_pos:
#			if tok[1] == 'NNP': f.write(replacetoken+' ')
#			else: f.write(tok[0]+' ')


if __name__ == "__main__":
	#print(txt_to_set("Irish Name Dict with Number.txt"))
#	POS_Tagging('Input_text2.txt')
	replace_person_names_maria('Input_text2.txt', 'test')

