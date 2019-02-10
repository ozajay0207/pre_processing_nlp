import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.collocations import *
from nltk.corpus import stopwords 
from nltk import bigrams
from nltk import ngrams
import nltk
import matplotlib.pyplot as plt

#REMOVES TOKENS WHICH COMES IN PAIRS EXAMPLE : ALL TYPES OF BRACKETS
def remove_doubles(delimeter1,delimeter2,words):
	print("Processing Doubles:",delimeter1,delimeter2)	
	words1=[]
	for i in words:
		if(i!=''):
			index=i.find(delimeter1)
			if(index==0):
				index=i.find(delimeter2)
				if(index!=-1):
					words1.append(i[0])
					words1.append(i[1:index])
					words1.append(i[index])
					if(index!=len(i)):
						words1.append(i[index:-1])
				else:
					words1.append(i[0])
					words1.append(i[1:len(i)])
			elif(index!=-1):
				index1=i.find(delimeter2)
				if(index!=-1):
					words1.append(i[0:index])
					words1.append(i[index])
					words1.append(i[index+1:index1])
					words1.append(i[index1])
					if(index1+1 != len(i)):
						words1.append(i[index1+1:-1])
				else:
					words1.append(i[0:index])
					words1.append(i[index])
					words1.append(i[index+1:len(i)])
			else:
				index=i.find(delimeter2)
				if(index!=-1):
					words1.append(i[0:index])
					words1.append(i[index])
					if(index+1 != len(i)):
						words1.append(i[index+1:len(i)])
				else:
					words1.append(i)
						
	return words1

def remove_punctuation(words1):
	ignore_list=[".Mr",".Jr",".Phd"," Mr"," Jr","Phd"]
	print("Processing Punctuations")
	flag=0
	words2=[]
	for i in words1:
		if(i!=''):
			index=i.find('.')
			if(index!=-1):
				if(index+1!=len(i)):
					if(i[index-1].isdigit() and i[index+1].isdigit()):
						flag=0
					elif(i[index-1].isupper()):
						flag=0
					elif(i[index-3:index] in ignore_list):
						flag=0	
					elif(i[0].isupper()):
						flag=0
					else:
						flag=1
						words2.append(i[0:index])
						words2.append(i[index:index+1])
						if(index+1 != len(i)):
							words2.append(i[index+1:])
			index=i.find(',')
			if(flag==0 and index!=-1):
				temp=""
				if(i[index-1].isdigit()):
					if(index+1 != len(i)):
						if(i[index+1].isdigit()):
							flag=1							
							words2.append(i)
					else:
						flag=1
						words2.append(i[0:index])
						words2.append(i[index:index+1])
						if(index+1 != len(i)):
							words2.append(i[index+1:])
				else:
					flag=1
					words2.append(i[0:index])
					words2.append(i[index:index+1])
					if(index+1 != len(i)):
						words2.append(i[index+1:])			
			index=i.find('?')
			if(flag==0 and index!=-1):
				flag=1
				words2.append(i[0:index])
				words2.append(i[index:index+1])
				if(index+1 != len(i)):
					words2.append(i[index+1:])
			index=i.find('!')
			if(flag==0 and index!=-1):
				flag=1
				words2.append(i[0:index])
				words2.append(i[index:index+1])
				if(index+1 != len(i)):
					words2.append(i[index+1:])
			index=i.find('"')
			if(flag==0 and index!=-1):
				if(index==0):
					flag=1
					words2.append(i[0])
					index1=i.find('"',1)
					if(index1!=-1):
						words2.append(i[1:index1])
						words2.append(i[index1])
						if(index1!=len(i)):
							words2.append(i[index1+1:])						
					else:
						words2.append(i[1:len(i)])

		
				else:
					flag=1
					words2.append(i[0:index])
					words2.append(i[index])
					index1=i.find('"',index)
					if(index1!=-1):
						words2.append(i[index+1:index1])
						words2.append(i[index1])
						if(index1!=len(i)):
							words2.append(i[index1+1:])						
					else:
						words2.append(i[index+1:])

			index=i.find("'")
			if(flag==0 and index!=-1):
				if(index==0):
					flag=1
					words2.append(i[0])
					index1=i.find("'",1)
					if(index1!=-1):
						words2.append(i[1:index1])
						words2.append(i[index1])
						if(index1!=len(i)):
							words2.append(i[index+1:])						
					else:
						words2.append(i[1:len(i)])

		
				else:
					flag=0
			
			if(flag==0):
				words2.append(i)
			flag=0
	return words2

def custom_word_tokenize(para):
	words = re.split(' |\n',para)	
	
	'''words1 = remove_doubles('(',')',words)
	words1 = remove_doubles('{','}',words1)
	words1 = remove_doubles('[',']',words1)		
	words1 = remove_punctuation(words1)		
		
	
	file1 = open('word_tokenize.txt',"w")
	print("writing to file")
	for i in words1:
		file1.write(i)
		file1.write('\n')'''
	return words
	
	
############################################### QUESTION 2 PROGRAM ###########################################

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


##############################################################################################################

if __name__ == "__main__":
	#files = ["demo1.txt"]
	files = ["xaa","xab","xac","xad"]
	for f in files:
		print("\n\n*********************************************************************************")
		print("Using Corpus:",f)
		file = open(f, "r")

		print("Tokenizing...")
		para=""
		for i in file.read():
			para = para + i		  

		word_tokenized_list=[]
		word_tokenized_list=custom_word_tokenize(para)




		print("Removing Stop Words...")		
		word_tokenized_list = remove_stop_words(word_tokenized_list)
		print("Removing Punctuations...")		
		word_tokenized_list = remove_punctuations(word_tokenized_list)
		print("Calculating Coverage:")
		coverage(word_tokenized_list)
			
		############################################################################################	
		print("\n*********************************************************************************")

		print("Performing Lemmatization")
		#CREATING LEMMATIZER REFERENCE
		lem = WordNetLemmatizer()
		lem_list = []
		#PERFORMING LEMMATIZATION
		for i in word_tokenized_list:
			lem_list.append(lem.lemmatize(i))		

		print("Calculating Coverage:")
		coverage(lem_list)


