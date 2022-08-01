import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

figure(num=None,figsize=(10,4),dpi=80,facecolor='w',edgecolor='k')

size1,len1=np.loadtxt('D:\WKU\WKU2021 Spring\CPS3410\Final\GA.txt',delimiter=' ',unpack=True)
size2,len2=np.loadtxt('D:\WKU\WKU2021 Spring\CPS3410\Final\Tabu.txt',delimiter=' ',unpack=True)
# size3,len3=np.loadtxt('D:\WKU\WKU2021 Spring\CPS3410\Final\VNS.txt',delimiter='\t',unpack=True)

plt.plot(size1,len1, label='GA')
plt.plot(size2,len2,label='Tabu',color='red')
# plt.plot(size3,len3,label='VNS',color='green')

plt.xlabel('Iteration Times')
plt.ylabel('Length')
plt.title('Convergence Graph for lu980.tsp')
plt.legend()
plt.show()