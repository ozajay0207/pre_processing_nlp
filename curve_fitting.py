import matplotlib.pyplot as plt
import numpy as np
import math

#plt.plot(x,y)
#plt.show()

file = open("frequence_1.txt","r")
data = [line.rstrip('\n') for line in file]
x=[]
y=[]
for i in data:
	y.append(math.log(int(i)))
for i in range(len(data)):
	x.append(math.log(i+1))
#	y.append(i+1)

p = np.polyfit(x,y,1)
y_fit = np.polyval(p,x)

summ=[]
for i in range(500):
	summ.append(math.exp(x[i]+y_fit[i]))

print(x)
print(y_fit)
#print(summ)
plt.plot(x,y,color="blue")
plt.plot(x,y_fit,color="red")
plt.show()

