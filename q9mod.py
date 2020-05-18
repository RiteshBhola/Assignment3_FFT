import numpy as np
np.set_printoptions(threshold=np.inf)
import scipy as sp
import matplotlib.pyplot as plt

def f(x):
  if(x>1):
    return 0
  elif(x<-1):
    return 0
  else:
    return 1
    
def g(x):
  return np.exp(-x*x)
  
def anal(x):
  return (np.sqrt(np.pi/5)*np.exp((-4*x*x)/5))
  
def h(x):
  return np.exp(-4*x*x)

n=128
data1=np.zeros(2*n,dtype=np.complex_)
data2=np.zeros(2*n,dtype=np.complex_)
x=np.zeros(2*n,dtype=np.complex_)
xmin=-5
xmax=5
p=np.zeros(2*n,dtype=np.complex_)
dx=(xmax-xmin)/(n-1)
for i in range(n):
  p[i]=i
  x[i]=xmin + i*dx
  data1[i]=g(x[i])
  data2[i]=h(x[i])
  
for i in range(2*n):
  p[i]=i

dft1=np.fft.fft(data1,norm='ortho')
dft2=np.fft.fft(data2,norm='ortho')
dft=dft1*dft2


conv=(np.fft.ifft(dft,norm='ortho'))
conv=conv*dx*np.sqrt(2*n)

xx=x[:n]
data1=data1[:n]
data2=data2[:n]
print(x)
print(conv)
conv=conv[int(n/2):int(3*n/2)]

conv=np.fft.ifftshift(conv)
plt.plot(xx.real,conv.real,".",label="convolution of Box function with itself")
plt.plot(xx.real,data1.real,"-",label="data1")

plt.plot(xx.real,anal(xx.real),"-",label="Analytic convolution of Box function with itself")
plt.legend(fontsize=17)
plt.xlabel("$x$",fontsize=15)
plt.ylabel("$f(x)$",fontsize=15)
plt.show()
