import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


subRiders = pd.read_csv('2015SubwayData.csv')

borough = []
riders = []
for i, row in subRiders.iterrows():
    
    borough.append(row['Borough'])

    riders.append(row['Riders'])


y_pos = np.arange(len(borough))


#plt.scatter(y_pos,riders)
#plt.plot(y_pos,riders)
barlist = plt.bar(y_pos,riders,align='center', alpha = 0.5, width = 0.3, color = 'red')

plt.xticks(y_pos,borough)
plt.ylabel('Riders (in hundread millions)')
plt.title("2015 Sub Ridership by Boroughs")

plt.show()
    
