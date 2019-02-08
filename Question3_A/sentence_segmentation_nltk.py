from nltk.tokenize import sent_tokenize,word_tokenize
import nltk

f = open("demo1.txt", "r")
f1 = open("sentence_tokenize_nltk.txt", "a")

for i in sent_tokenize(f.read()):
	f1.write(i)
	f1.write('\n')



