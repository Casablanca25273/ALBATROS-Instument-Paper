import numpy as np
from matplotlib import pyplot as plt

N=1
#S=np.linspace(0.1,1000,10000)

smin=0.01
smax=10
S=np.exp(np.linspace(np.log(smin),np.log(smax),1000))

x=2.0/np.pi*np.arcsin(S/(S+N))

sigma_x=np.sqrt(1-x**2)
sigma_rho=np.pi/2*np.cos(np.pi/2*x)*sigma_x
sigma_s=(S+N)**2/N*sigma_rho

ref=S/(S+N)
corr_eff=(S+N)/sigma_s

plt.clf()
plt.plot(S,corr_eff, 'k-')
plt.xlabel('SNR')
plt.ylabel('$\epsilon_{corr}$')
#plt.loglog(S,corr_eff)


imin=(2*len(S))//3
pp=np.polyfit(np.log(S[imin:]),np.log(corr_eff[imin:]),1)
print(pp)

#pred=1.0/(S)**(1/4)

#pred=(S**pp[0])*np.exp(pp[1])
#pred=pred/pred[-1]*corr_eff[-1]
pred=(S**-0.25)/3

#plt.plot(S,pred)
#plt.plot(S,sigma_s/S)
plt.savefig('corr_efficiency.png')




