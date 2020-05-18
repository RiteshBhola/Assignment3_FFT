import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def gaus(k):
  return(np.exp((-k*k)/4)/np.sqrt(2))

filename ="fftgauss.txt"
a=np.loadtxt(filename,usecols=0)
b=np.loadtxt(filename,usecols=1)
k=np.linspace(a.min(),a.max(),a.size,endpoint=True)
plt.plot(k,gaus(k),"-r",label="Analytic FourierTransform of gaussian")
plt.plot(a,b,".k",label="FourierTransform of gaussian using FFTW")



plt.xlabel("k",fontsize=17)
plt.ylabel("F(k)",fontsize=17)
plt.title("N=800,Xmax=100,Xmin=-100",fontsize=17)
plt.legend(fontsize=15)
plt.show()
