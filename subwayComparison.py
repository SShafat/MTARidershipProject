import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



subwayRidership = pd.read_csv('subwayridership.csv')

year = [0,0,0,0,0,0]
annualTotRow = [0,0,0,0,0,0]

for i, row in subwayRidership.iterrows():
    year[i] = row['Year']

    annualTotRow[i] =row ['Annual Total']

#this is to remove the commas from the number read_csv is picking up
def removeComma(array):
    noComma = []
##    print("This is the array with comma")
##    print(array)
##    print("Lenght of array is: " , len(array))
    for i in range(0, len(array)):
        noComma.append(array[i].replace(',',''))
        
    return noComma

annualTot = removeComma(annualTotRow)
#print(annualTot)

y_pos = np.arange(len(year))   
busRiderShip = pd.read_csv('busridership.csv')

year2 = [0,0,0,0,0,0]
annualTotRow2 = [0,0,0,0,0,0]

for i, row in busRiderShip.iterrows():
    year2[i] = row['Year']
    annualTotRow2[i] = row ['Annual Total']

annualTot2 = removeComma(annualTotRow2)

a = []
for i in range(0,len(annualTot)):
    a.append(int(annualTot[i]))

print(a)
    

fig = plt.figure()

ax1 = fig.add_subplot(111)
bar1 = ax1.bar(y_pos,a, align = 'center', color = "blue", label = 'Subway', width = 0.5)

plt.ylabel("Riders (in billions)")
plt.xticks(y_pos,year)

a2 = []
for i in range(0,len(annualTot2)):
    a2.append(int(annualTot2[i]))


ax2 = fig.add_subplot(111)
bar2 = ax2.bar(y_pos, a2, align = 'center', color = 'yellow', label = 'Bus', width = 0.5)
plt.legend(handles = [bar1,bar2])

#ax1.ylabel('Riders')
plt.title('Subway and Bus riders from Years 2010 to 2015.')
plt.show()
