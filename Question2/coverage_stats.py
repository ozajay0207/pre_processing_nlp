from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.collocations import *
from nltk.corpus import stopwords 
from nltk import bigrams
from nltk import ngrams
import nltk
import matplotlib.pyplot as plt


def ngram_coverage(l1,ngram_type,percent):
	if(ngram_type==1):
		print("Forming Unigrams of tokens...")

	if(ngram_type==2):
		print("Forming Bigrams of tokens...")

	if(ngram_type==3):
		print("Forming Trigrams of tokens...")

	ngram_list = ngrams(l1, ngram_type)
	
	freq_distribution = nltk.FreqDist(ngram_list)

	sum1=0
	ngrams_count=0
	l = freq_distribution.most_common(len(freq_distribution.values()))
	for i in l:
		sum1 = sum1 + i[1]
		ngrams_count = ngrams_count + 1

	print("\tTotal Frequency Count: ",sum1)

	if(ngram_type==1):
		print("\tTotal number of Unigrams:",ngrams_count)

	if(ngram_type==2):
		print("\tTotal number of Bigrams:",ngrams_count)

	if(ngram_type==3):
		print("\tTotal number of Trigrams:",ngrams_count)


	count=0
	temp_sum=0

	for i in l:
		if(temp_sum>=sum1*percent):
			break
		count = count + 1
		temp_sum = temp_sum + i[1]

	if(ngram_type==1):
		print("\tUnigrams to cover 90% Corpus:",count)

	if(ngram_type==2):
		print("\tBigrams to cover 80% Corpus:",count)

	if(ngram_type==3):
		print("\tTrigrams to cover 70% Corpus:",count)

def coverage(l):

	########################################################################################
	#UNIGRAMS TO COVER 90% CORPUS

	ngram_coverage(l,1,0.9)

	########################################################################################
	#BIGRAMS TO COVER 80% CORPUS

	ngram_coverage(l,2,0.8)

	########################################################################################
	#TRIGRAMS TO COVER 70% CORPUS

	ngram_coverage(l,3,0.7)

def to_lower_case(l):
	l1 = [i.lower() for i in l]
	return l1

def remove_stop_words(l):
	stop_words = set(stopwords.words('english'))
	l1=[]
	l1 = [i for i in l if not i in stop_words]
	return l1

def remove_punctuations(l):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
	l1=[]
	l1 = [i for i in l if not i in punctuations]
	return l1

if __name__ == "__main__":

	#files = ["demo1.txt"]
	files = ["xaa","xab","xac","xad"]
	for f in files:
		print("\n\n*********************************************************************************")
		print("Using Corpus:",f)
		file = open(f, "r")		


		print("Tokenizing...")
		#word_tokenized_list = word_tokenize(word_text)
		word_tokenized_list = word_tokenize(file.read())		

		print("Converting to lower case...")
		word_tokenized_list = to_lower_case(word_tokenized_list)

		filtered_file="lower_case_"
		filtered_file=filtered_file+str(f)
		filtered_file=filtered_file+".txt"
		f1=open(filtered_file,"w")
		for i in word_tokenized_list:
			f1.write(i)
			f1.write("\n")

		print("Removing Stop Words...")		
		word_tokenized_list = remove_stop_words(word_tokenized_list)
		print("Removing Punctuations...")		
		word_tokenized_list = remove_punctuations(word_tokenized_list)


		
		#WRITING FILTERED TOKENS TO FILE		
		filtered_file="filtered_file_"
		filtered_file=filtered_file+str(f)
		filtered_file=filtered_file+".txt"
		f1=open(filtered_file,"w")
		for i in word_tokenized_list:
			f1.write(i)
			f1.write("\n")
		

		print("Calculating Coverage:")
		coverage(word_tokenized_list)
		

		########################################################################################	
		print("\n*********************************************************************************")

		print("Performing Lemmatization")
		#CREATING LEMMATIZER REFERENCE
		lem = WordNetLemmatizer()
		lem_list = []

		#PERFORMING LEMMATIZATION
		for i in word_tokenized_list:
			lem_list.append(lem.lemmatize(i))		

		
		#WRITING LEMMATIZED TOKENS TO FILE		
		filtered_file="lemmatized_file_"
		filtered_file=filtered_file+str(f)
		filtered_file=filtered_file+".txt"
		f1=open(filtered_file,"w")
		for i in lem_list:
			f1.write(i)
			f1.write("\n")
		

		print("Calculating Coverage:")
		coverage(lem_list)

	



