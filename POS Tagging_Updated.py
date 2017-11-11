import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
from nltk.chunk import ne_chunk

def find_names(filename):
	"""(str) -> None
	Find all the names into a text file and print them into the terminal
	"""
	with open(filename, 'r') as f:
		rawtext = f.read()
		tokens = word_tokenize(rawtext)
		j = []

		tokens_with_pos = nltk.pos_tag(tokens)
		print("---------------------")
		print("Named entities")
		print()
		named_entities = [chunk for chunk in ne_chunk(tokens_with_pos) if isinstance(chunk, Tree)]
		for i in named_entities:
    	print(i)
