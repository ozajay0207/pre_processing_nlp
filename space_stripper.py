import re
para = "Mr.Hello how are you?I am fine. How about you!"
file = open("demo.txt","r")
#para=""
#for i in file.read():
#    para = para+ i
    
#para.strip()
sent = re.split('\.|\?|\!', para)

for i in sent:
    print(i)
#print(sent)
#print(re.split('.|?|!',para))


#for i in a.split('.') or a.split:
#    print(i.lower())



