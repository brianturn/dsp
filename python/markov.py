# !/usr/bin/env python

#  Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

#  ```bash
#  ./markov.py chains.txt 40
#  ```

#  A possible output would be:

#  > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

#  There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

# This Markov generator keeps punctuation and casing intact 

import string
import sys
import random
import pprint

def make_histogram(file):
	word_histogram = {} # create a word frequency histogram
	for line in file:
		words = line.split()
		for word in words:
			word_histogram[word] = word_histogram.get(word, 0) + 1
	return word_histogram

def markov(word_histogram):
	choices = [] # create a weighted list of choices - each word multiplied by it's frequency
	for word, freq in word_histogram.items(): 
		choices.extend([word] * freq)
	markov_list = [random.choice(choices) for word in range(len(word_histogram))] # markov-generated list equal in length to the original text
	pprint.pprint(' '.join(markov_list)) # pretty print the list as a string

file = open(sys.argv[1], 'r')

markov(make_histogram(file))
