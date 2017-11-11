#!/usr/bin/python3 -i
"""This file contain functions to transform a list of names text file to a set 
"""

def txt_to_set(filename):
	"""(str) -> set()
	Convert a text file containing a list of names into a set"""
	res = set()
	with open(filename,'r') as f:
		for line in f:
			l = line.strip().split()
			for item in l:
				try: int(item[0])
				except ValueError: res.add(item)
	return res
	

def cleaned_txt_to_set(filename):
	"""(str) -> set()
	Convert a cleaned text file containing a list of names into a set
	a clean text is formatted as a name each line
	Same effect as txt_to_set but quicker"""
	res = set()
	with open(filename,'r') as f:
		for line in f:
			res.add(line.strip())
	return res


def clean_txt(filename):
	"""(str) -> None
	Rewrite a file with a list of name under the format name, pass line, name"""
	tmp = []
	with open(filename,'r') as f:
		for line in f:
			l = line.split()
			for item in l:
				try: int(item[0])
				except ValueError: tmp.append(item)
	with open(filename,'w') as f:
		for item in tmp: f.write(item+"\n")

if __name__=="__main__":	
	print(txt_to_set("Irish Name Dict with Number.txt"))
	print(cleaned_txt_to_set("Irish Name Dict with Number.txt"))
        
        
        
        
