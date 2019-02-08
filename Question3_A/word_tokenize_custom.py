import re


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

def remove_punctuations(words1):
	print("Processing Punctuations")
	flag=0
	words2=[]
	for i in words1:
		if(i!=''):
			index=i.find('.')
			if(index!=-1):
				flag=1
				words2.append(i[0:index])
				words2.append(i[index:index+1])
				if(index+1 != len(i)):
					words2.append(i[index+1:])
			index=i.find(',')
			if(flag==0 and index!=-1):
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
			index=i.find('%')
			if(flag==0 and index!=-1):
				flag=1
				words2.append(i[0:index])
				words2.append(i[index:index+1])
				if(index+1 != len(i)):
					words2.append(i[index+1:])
			index=i.find('-')
			if(flag==0 and index!=-1):
				flag=1
				words2.append(i[0:index])
				words2.append(i[index:index+1])
				if(index+1 != len(i)):
					words2.append(i[index+1:])
			if(flag==0):
				words2.append(i)
			flag=0
	return words2

def custom_word_tokenize(para):
	words = re.split(' |\n',para)

	file1 = open('word_tokenize.txt',"w")

	print("here")
	'''for i in words:
		if(i == ''):
			words.remove(i)
	'''
	
	words1 = remove_doubles('(',')',words)
	words1 = remove_doubles('{','}',words1)
	words1 = remove_doubles('[',']',words1)	
	words1 = remove_punctuations(words1)			

	print("writing to file")
	for i in words1:
		file1.write(i)
		file1.write('\n')

############################################### MAIN PROGRAM ###########################################

file = open("xad","r")
para=""
for i in file.read():
    para = para + i
  

custom_word_tokenize(para)


