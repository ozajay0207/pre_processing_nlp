from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.collocations import *
from nltk import FreqDist
import nltk

f = open("demo.txt", "r")
f1 = open("word_tokenize.txt", "a")
list1 = []
for i in word_tokenize(f.read()):
	list1.append(i)

fdist = FreqDist(list1)	
fdist1 = FreqDist(fdist.most_common(10))

fdist1.plot()
