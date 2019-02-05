from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk.collocations import *
#from nltk import bigrams
#from nltk import ngrams
#import nltk

'''word_text = "hello there how are you doing"
sent_text = "Hello Mr. Arun today we are gonna do some heavy lifting. Are you up for it?"


#print (word_tokenize(word_text))
#print (sent_tokenize(sent_text))


word_tokenized_string = word_tokenize(word_text)



#Printing Grams in corpus
unigram_string = ngrams(word_tokenized_string, 1)

print("Unigram_string:\n")

for grams in unigram_string:
    print(grams)
#    finder.ngram_fd(grams)


#fdist = nltk.FreqDist(unigram_string)
#for k,v in fdist.items():
 #   print (k,v)
#    finder.ngram_fd.viewitems()

print("\n")


#Printing Bigrams in corpus

bigram_string = ngrams(word_tokenized_string, 2)

#finder = BigramCollocationFinder.from_words(bigram_string)
#finder.items()[0:5]


print("Bigram_string:\n")

for grams in bigram_string:
    print(grams)

fdist = nltk.FreqDist(bigram_string)
for k,v in fdist.items():
    print (k,v)

for grams in bigram_string: 
    print(finder.ngram_fd.viewitems(grams))


print("\n")


#Priting Trigrams in corpus
trigram_string = ngrams(word_tokenized_string, 3)

print("Trigram_string:\n")

for grams in trigram_string:
    print(grams)





























'''
# Code to open corpus file, read it, tokenize it on basis of word and dump it in other file

file_1 = open("xab", "r+")
file_2 = open("word_tokenized.txt", "w")

#print (file.read())

for i in word_tokenize(file_1.read()):
	file_2.write(i)
