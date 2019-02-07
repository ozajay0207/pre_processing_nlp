import re

def custom_sentence_segmentation(para):
#	sent = re.split('\.|\?|\!', para)
	sent=[]
	start=0
	index=para.find('.',start)
	while(index!=-1):
		sent.append(para[start:index+1])	
		start=index+1
		index=para.find('.',start)
	if(start!=(len(para)-1)):
		sent.append(para[start:len(para)-1])
	
	
	sent1=[]
	for i in sent:
		start=0
		index=i.find('?',start)
		if(index!=-1):
			sent1.append(i[start:index+1])	
			if((index+1)!=(len(i))):				
				sent1.append(i[index+1:len(i)])
		else:
			sent1.append(i)


	sent2=[]
	for i in sent1:
		start=0
		index=i.find('!',start)
		if(index!=-1):
			sent2.append(i[start:index+1])					
			if((index+1)!=(len(i))):				
				sent2.append(i[index+1:len(i)])
		else:
			sent2.append(i)


	file1 = open("sentence_segmentation.txt","w")
	for i in sent2:

		i=i.strip()

		file1.write(i)
		file1.write('\n')

############################################### MAIN PROGRAM ###########################################

file = open("demo1.txt","r")
para=""
for i in file.read():
    para = para + i
  
custom_sentence_segmentation(para)




