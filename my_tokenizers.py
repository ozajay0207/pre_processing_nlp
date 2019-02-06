import re
#para = "Mr.Hello how are you?I am fine. How about you!"
file = open("demo1.txt","r")
para=""
for i in file.read():
    para = para + i

#print(para)
    
sent = re.split('\.|\?|\!', para)

file1 = open("sentences.txt","w")
for i in sent:
	file1.write(i)
	file1.write('\n')

words = re.split(' |\n',para)
#words1 = words[:]

file1 = open('word_tokenize.txt',"w")
'''for i in words:
	if(i == ''):
		words.remove(i)
	else:
		index=i.find('.')
		if(index!=-1):
			words1.append(i[0:index])
			words1.append(i[index:index+1])
			if(index+1 != len(i)):
				words1.append(i[index+1:])
		else:
			index=i.find(',')
			if(index!=-1):
				words1.append(i[0:index])
				words1.append(i[index:index+1])
				if(index+1 != len(i)):
					words1.append(i[index+1:])			
			else:
				index=i.find('?')
				if(index!=-1):
					words1.append(i[0:index])
					words1.append(i[index:index+1])
					if(index+1 != len(i)):
						words1.append(i[index+1:])			
				else:
					index=i.find('!')
					if(index!=-1):
						words1.append(i[0:index])
						words1.append(i[index:index+1])
						if(index+1 != len(i)):
							words1.append(i[index+1:])			
					else:
						words1.append(i)
'''


for i in words:
	if(i == ''):
		words.remove(i)
	
words1=[]
for i in words:
	index=i.find('(')
	if(index==0):
		index=i.find(')')
		if(index!=-1):
			words1.append(i[0])
			words1.append(i[1:index])
			words1.append(i[index])
			if(index!=len(i)):
				words1.append(i[index:-1])
		else:
			words1.append(i[0])
			words1.append(i[1:-1])
	elif(index!=-1):
		index1=i.find(')')
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
			words1.append(i[index+1:-1])
	else:
		index=i.find(')')
		if(index!=-1):
			words1.append(i[0:index])
			words1.append(i[index])
			if(index+1 != len(i)):
				words1.append(i[index+1:-1])
		else:
			words1.append(i)
		
for i in words1:
	if(i == ''):
		words1.remove(i)		
		
flag=0
words2=[]
for i in words1:
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
	if(flag==0):
		words2.append(i)
	flag=0
	
for i in words2:
	file1.write(i)
	file1.write('\n')



