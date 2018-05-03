import numpy as np
import matplotlib.pyplot as plt

pl=np.ones(30)/30

def pxl(x,l):
	return np.exp(-x/l)/(l*(np.exp(-1.0/l)-np.exp(-20.0/l)))

x=np.array([1.2,2.5,2.8,5.0])

lam=np.linspace(0.1,30,100)
p=np.ones(100)
suma=0.0
for i in range(0,len(p)):
	for j in range(0,4):
		p[i] = p[i]*pxl(x[j],lam[i])
	suma+=p[i]
	
p=p/suma
plt.plot(lam,p)
plt.xlabel('lambda')
plt.ylabel('p(lambda|x)')
plt.savefig('grafica.png')
