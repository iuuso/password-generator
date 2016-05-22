#/usr/lib python3
import random, sys
from optparse import OptionParser
DEBUG = True

# Parameters: dictionary, special characters, complexity

password = ""

def read_file():
	dictionary = open("wordsEn.txt", "r")
	words = dictionary.read().split('\n')
	return words

def select_word_from_list(listofwords):
	numbOfWord = random.randrange(1, len(listofwords), 1)
	selectedWord = wordList[numbOfWord]
	return selectedWord

def main(options,password):
	#print(random.randrange(1, len(wordList),1))
	if options.num >= 0:
		for i in range(options.num):
			word = select_word_from_list(wordList)
			if i == 0:
				password += word
			else:
				password += " " + word
	else:
		print("The number you entered is zero or less. \nPlease use a bigger number.")

	print(password)


# Command line parameters parser
parser = OptionParser()
parser.add_option("-n", help="Numbers of words to use", type="int",
				metavar="NUMBER", dest="num")
(options, args) = parser.parse_args()

wordList = read_file()
main(options, password)