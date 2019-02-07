from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.collocations import *
from nltk import bigrams
from nltk import ngrams
import nltk
import matplotlib.pyplot as plt


def ngram_coverage(l1,ngram_type,percent):
	ngram_list = ngrams(l1, ngram_type)
	
	freq_distribution = nltk.FreqDist(ngram_list)

	sum1=0
	l = freq_distribution.most_common(len(freq_distribution.values()))
	for i in l:
		sum1 = sum1 + i[1]

	print("Sum:",sum1)


	count=0
	temp_sum=0

	for i in l:
		if(temp_sum>=sum1*percent):
			break
		count = count + 1
		temp_sum = temp_sum + i[1]


	print(count)




#word_text = "My car is cars"
word_text = "Zipf's law is an empirical law formulated using mathematical statistics. The law is named after the linguist George Kingsley Zipf, who first proposed it.Zipf's law states that given a large sample of words used, the frequency of any word is inversely proportional to its rank in the frequency table. So word number n has a frequency proportional to 1/n.Thus the most frequent word will occur about twice as often as the second most frequent word, three times as often as the third most frequent word, etc. For example, in one sample of words in the English language, the most frequently occurring word, the, accounts for nearly 7% of all the words (69,971 out of slightly over 1 million). True to Zipf's Law, the second-place word of accounts for slightly over 3.5% of words (36,411 occurrences), followed by and (28,852). Only about 135 words are needed to account for half the sample of words in a large sample.[3] The same relationship occurs in many other rankings, unrelated to language, such as the population ranks of cities in various countries, corporation sizes, income rankings, etc. The appearance of the distribution in rankings of cities by population was first noticed by Felix Auerbach in 1913.[4]. It is not known why Zipf's law holds for most languages"


file = open("xaa", "r")

#word_tokenized_list = word_tokenize(word_text)
word_tokenized_list = word_tokenize(file.read())


########################################################################################
#UNIGRAMS TO COVER 90% CORPUS

ngram_coverage(word_tokenized_list,1,0.9)

########################################################################################
#BIGRAMS TO COVER 80% CORPUS

ngram_coverage(word_tokenized_list,2,0.8)

########################################################################################
#TRIGRAMS TO COVER 70% CORPUS

ngram_coverage(word_tokenized_list,3,0.7)

########################################################################################
#LEMMATIZER
lem = WordNetLemmatizer()
lem_list = []
for i in word_tokenized_list:
	lem_list.append(lem.lemmatize(i))

ngram_coverage(lem_list,1,0.9)
ngram_coverage(lem_list,2,0.8)
ngram_coverage(lem_list,3,0.7)



