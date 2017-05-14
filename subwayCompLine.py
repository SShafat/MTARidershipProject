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
ax1.scatter(y_pos,a)
ax1.plot(y_pos,a, color = 'green')
plt.ylabel("Riders (in billions)")
plt.xticks(y_pos,year)
plt.title("Subway riders in the last five years")
a2 = []
for i in range(0,len(annualTot2)):
    a2.append(int(annualTot2[i]))

print(a2)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.scatter(y_pos,a2)
ax2.plot(y_pos, a2, color = 'red')
plt.ylabel("Riders (in hundread thousands)")
plt.xticks(y_pos,year)


#ax1.ylabel('Riders')
plt.title('Bus riders in the last five years')
plt.show()
