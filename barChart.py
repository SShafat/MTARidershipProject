
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

worldSubway = pd.read_csv('worldSubway.csv')

cities = [0,0,0,0,0,0,0,0,0,0]
riders = [0,0,0,0,0,0,0,0,0,0]
for i, row in worldSubway.iterrows():
    print(i)
    cities[i] = row['City']

    riders[i] = row['Ridership']

print(cities)
y_pos = np.arange(len(cities))
print(riders)



barlist = plt.bar(y_pos,riders,align='center', alpha = 1)
#highlights NYC in the ranking
barlist[6].set_color('r')
plt.xticks(y_pos,cities)
plt.ylabel('Riders (in billions)')
plt.title("Transit's Rank Among the World's Subway Systems")

plt.show()
    
    
   
    



