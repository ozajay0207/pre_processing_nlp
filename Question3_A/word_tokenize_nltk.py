from nltk.tokenize import sent_tokenize,word_tokenize
import nltk

f = open("xad", "r")
f1 = open("word_tokenize_nltk.txt", "a")

for i in word_tokenize(f.read()):
	f1.write(i)
	f1.write('\n')



