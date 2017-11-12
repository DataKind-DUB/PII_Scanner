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
from nltk.tokenize import word_tokenize, wordpunct_tokenize
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
		named_entities = [chunk for chunk in ne_chunk(tokens_with_pos)]# if isinstance(chunk, Tree)]
		print(tokens_with_pos)
		print(named_entities)
#		for i in named_entities:
#			print(i)
			
			
def get_names_entities_list(tokens):
	"""(nltk.tokens) -> list
	Return a list of the person names among the tokens"""
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
	return named_entities_list
			
	
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
	
			
def replace_person_names_version2(filename, outputfile = None, replacetoken = '***'):
	"""(str) -> None
	Replace all person names and begining of email adresses by replacetoken (defaut ***)
	if outputfile, the file is not rewritten but an new file output is written 
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
	tokens = word_tokenize(rawtext)#"Mrs.Truc" -> ['Mrs.Truc'] and "nemo.nemo@xmail.com" -> ["nemo.nemo","@","xmail.com"]
#	tokens = wordpunct_tokenize(rawtext)#"Mrs.Truc" -> ['Mrs', '.', 'Truc'] and "nemo.nemo@xmail.com" -> ["nemo",".","nemo","@","xmail",".","com"]
	tokens_with_pos = nltk.pos_tag(tokens)
	chunked_tokens = ne_chunk(tokens_with_pos)
	if not outputfile: outputfile = filename
	with open(outputfile, 'w') as f:
		for tok in chunked_tokens:
			if isinstance(tok, Tree) and tok.label() == 'PERSON':#if the token is a person, replace by replacetoken
				f.write(replacetoken + ' ')
			elif isinstance(tok, Tree): f.write(' '.join(x[0] for x in tok) + ' ')
			else: f.write(tok[0] + ' ')
			
			
def replace_person_mail_names(filename, outputfile = None, replacetoken = '***'):
	"""(str) -> None
	Replace all person names and begining of email adresses by replacetoken (defaut ***)
	if outputfile, the file is not rewritten but an new file output is written 
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
	tokens = word_tokenize(rawtext)#"Mrs.Truc" -> ['Mrs.Truc'] and "nemo.nemo@xmail.com" -> ["nemo.nemo","@","xmail.com"]
#	tokens = wordpunct_tokenize(rawtext)#"Mrs.Truc" -> ['Mrs', '.', 'Truc'] and "nemo.nemo@xmail.com" -> ["nemo",".","nemo","@","xmail",".","com"]
	chunked_tokens = ne_chunk(nltk.pos_tag(tokens))
	
	if not outputfile: outputfile = filename
	with open(outputfile, 'w') as f:
		prec, curr = '', ''
		for tok in chunked_tokens:
			if isinstance(tok, Tree) and tok.label() == 'PERSON':#if the token is a person, replace by replacetoken
				curr = replacetoken
			elif isinstance(tok, Tree): curr = ' '.join(x[0] for x in tok)
			elif tok[0] == '@':#if the token is @, replace last token by replacetoken
				prec = replacetoken
				curr = '@'
			else: curr = tok[0]
			f.write(prec + ' ')
			prec = curr
		f.write(curr)

		
def replace_person_names_version1(filename, outputfile = None, replacetoken = '***'):
	"""(str) -> None
	Replace all person names by replacetoken (defaut ***)
	if outputfile, the file is not rewritten but an new file output is written 
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
	tokens = word_tokenize(rawtext)
	named_entities_list = get_names_entities_list(tokens)
	print(named_entities_list)
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
					anonymized_text += '***'
					break 
		else: anonymized_text += " " + token 
		i += 1
	if not outputfile: outputfile = filename
	with open(outputfile, 'w') as f: f.write(anonymized_text)


if __name__ == "__main__":
	#print(txt_to_set("Irish Name Dict with Number.txt"))
#	print_names("Input_text2.txt")
#	replace_proper_names('Input_text2.txt', 'test0')
#	replace_person_names_version2('Input_text2.txt', 'test1')
	replace_person_mail_names('input_text.txt', 'test2')

