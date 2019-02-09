import re

def custom_sentence_segmentation(para):
#	sent = re.split('\.|\?|\!', para)
	ignore_list=[".Mr",".Jr",".Phd"," Mr"," Jr","Phd"]
	sent=[]
	start=0
	index=para.find('.',start)
	temp=""
	temp1=""
	flag=0
	temp_ind=0
	while(index!=-1):
		if(index+1 != len(para)):
			if(para[index-1].isdigit() and para[index+1].isdigit()):				
				flag=1
				temp=temp+para[start:index+1]		
				start=index+1
				index=para.find('.',start)
				continue

		if(para[index-1].isupper()):			
			flag=1
			temp=temp+para[start:index+1]		
			start=index+1
			index=para.find('.',start)
			continue
		if(para[index-1].islower()):				
			temp1=para[index-3:index]
			if(temp1 in ignore_list):
				flag=1
				temp=temp+para[start:index+1]		
				start=index+1
				index=para.find('.',start)
				continue	
			elif(index+1!=len(para)):
				if(para[index+1]==" " and para[index+2].isupper()==False):				
					flag=1
					temp=temp+para[start:index+1]		
					start=index+1
					index=para.find('.',start)
					continue	
				else:
					if(flag==1):
						temp=temp+para[start:index+1]
						sent.append(temp)
						temp=""
						temp1=""
						flag=0			
						start=index+1
						index=para.find('.',start)
						continue

					sent.append(para[start:index+1])	
					start=index+1
					index=para.find('.',start)
		else:
			if(flag==1):
				temp=temp+para[start:index+1]
				sent.append(temp)
				temp=""
				temp1=""
				flag=0			
				start=index+1
				index=para.find('.',start)
				continue
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

file = open("xaa","r")
para=""
for i in file.read():
    para = para + i
  
custom_sentence_segmentation(para)




