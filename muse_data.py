#!/usr/bin/env python
# coding: utf-8

# In[83]:





# In[84]:


	import numpy as np
	import matplotlib.pyplot as plt
	from scipy.fftpack import fft, ifft
	import pandas as pd
	import pylab

data = np.genfromtxt(r'C:\Users\usman\EEG_recording_Rest_90s.csv', delimiter = ',')
x = data[:, 0]
y = data[:, 4]

# plt.plot(x,y);
# pylab.xlim([0, 60])
# pylab.ylim([0, 100000])

#FFT
#number of sample points
N = len(data)
# #frequency of signal
T = 253.2
#freq res
res = T/N

# #perform FFT on signal
yf = abs(fft(y))
print(N);

# #create new x-axis: frequency from signal
xf = np.linspace(0.0, T, num = N)

# #plot results
plt.plot(xf, yf)
pylab.xlim([0, 50])
pylab.ylim([0, 50000])
plt.grid()
plt.show()

#delta waves = 4-8 Hz
#c_find = 
d_ = yf[1015:2031]
d = sum(d_)
d_num = 1050
d_av = d/d_num
print("d = ", d_av)

#alpha waves = 8-12 Hz
a_ = yf[2030:3045]
a = sum(a_)
a_num = 1050
a_av = a/a_num
print("a = ", a_av)

#beta waves = 12-30 Hz
b_ = yf[3045:7597]
b = sum(b_)
b_num = 7597-(3045)
b_av = b/b_num
print("b = ", b_av)

#gamma waves = 30 Hz +
g_ = yf[7597:10130]
g = sum(g_)
g_num = 10130-7597
g_av = c/c_num
print("g = ", g_av)



# In[ ]:





# In[ ]:




