
PII_Scanner is a small programm to scan text file and remplace the persons names, email adresses and phone numbers in it by ***.

For this programm to work you need Python 3.5 and the Nltk library.

#-------------------------------------------------------------------------

WHAT PII_Scanner DOES:

- replace all proper nouns in a text file (function replace_proper_names in PII_Scanner.py)
or:
- replace persons names in a text file with between 80% and 90% of efficiency (replace_person_names_version2 in PII_Scanner.py)
or:
- replace persons names (80-90% efficency) and email adresses in a text file (replace_person_mail_names in PII_Scanner.py)


WHAT PII_Scanner WILL DO (eventually):

- replace phone numbers
- have a better replacement efficiency for persons names
- replace persons names written without uppercase first letter
- replace adresses

#-------------------------------------------------------------------------

ALGORITHM SUMMARY:

The text file is read.
The resulting string is cut into words and punctuation tokens
The tokens are tagged by Named Entity Recognition packages from nltk to identify proper names/persons/email/... in the text
The tokens are written one by one in a text file, the one having the targeted tag being replace by ***.

#-------------------------------------------------------------------------

FILES:

- PII_Scanner.py:
	main file. Included the replacement functions. To use it, modify the script after the "__name__ == "__main__"" line and run "python PII_Scanner" in a terminal
	
- POS Tagging.py
- POS Tagging_Updated.py
- pos_tagging_final.py
	files including the work in progress. POS Tagging.py is the oldest file and pos_tagging_final.py the newest. Included leads to improve the efficiency of persons names replacement
	
- input_text.txt
- Input_text2.txt
- test_data_long.txt
	input test text files
	
- namelist.py
	file containing some functions to transform a text file into a list of names (one lead to improve the efficiency of persons names replacement)

- Irish Name Dict with Number.txt
	non cleaned text file including a list of Irish names

#------------------------------------------------------------------------


