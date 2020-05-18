import numpy as np
import scipy as sp
import matplotlib.pyplot as plt




filename ="fftnumpy.txt"
a=np.loadtxt(filename,usecols=0)
b=np.loadtxt(filename,usecols=1)
plt.plot(a,b,".",label="FourierTransform of sinc(x) using numpy")
a=np.loadtxt(filename,usecols=2)
b=np.loadtxt(filename,usecols=3)
plt.plot(a,b,"-",label="Analytic FourierTransform of sinc(x)")

filename ="fftdata.txt"
a=np.loadtxt(filename,usecols=0)
b=np.loadtxt(filename,usecols=1)

plt.plot(a,b,".",label="FourierTransform of sinc(x) using FFTW")

filename ="fftgsl.txt"
a=np.loadtxt(filename,usecols=0)
b=np.loadtxt(filename,usecols=1)

plt.plot(a,b,".",label="FourierTransform of sinc(x) using GSL")
plt.xlabel("k",fontsize=15)
plt.ylabel("F(k)",fontsize=15)
plt.title("N=1024,Xmax=500,Xmin=-500")
plt.legend(fontsize=15)
plt.show()
