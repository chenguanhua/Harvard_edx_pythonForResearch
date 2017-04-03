import numpy as np
import pandas as pd
whisky=pd.read_csv('whiskies.txt')
whisky['Region']=pd.read_csv('regions.txt')

flavors=whisky.iloc[:,2:14]
corr_flavors=pd.DataFrame.corr(flavors)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.show()

corr_whisky=pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()
plt.show()

#print(corr_flavors)
print(corr_whisky)

