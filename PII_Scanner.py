#!/usr/bin/python3 -i

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
			
			
def replace_names(filename, outputfile = None, replacetoken = '***'):
	"""(str) -> None
	Find all the names into a text file and print them into the terminal
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
	tokens = word_tokenize(rawtext)
	tokens_with_pos = nltk.pos_tag(tokens)
	person_entities = set([chunk for chunk in ne_chunk(tokens_with_pos) if isinstance(chunk, Tree)])
	if not outputfile: outputfile = filename
	with open(outputfile, 'w') as f:
		for tok in tokens_with_pos:
			if tok[1] == 'NNP': f.write(replacetoken+' ')
			else: f.write(tok[0]+' ')


if __name__ == "__main__":
	#print(txt_to_set("Irish Name Dict with Number.txt"))
	print_names('Input_text2.txt')
	replace_names('Input_text2.txt', 'test')

