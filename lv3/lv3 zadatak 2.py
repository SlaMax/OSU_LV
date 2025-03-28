import pandas as pd
import matplotlib . pyplot as plt

data = pd.read_csv ('data_C02_emission.csv')


'''
data['CO2 Emissions (g/km)'].plot(kind='hist', bins = 20)
plt.show()
'''

'''
najmanje automobila ima od 400 do 600 a najviše ima 200 od 300 do
'''

'''
data['Fuel Type'] = data['Fuel Type'].astype('category')
colors = {'Z': 'red', 'X': 'yellow', 'E': 'blue', 'D': 'purple', 'N':'green'}
data.plot.scatter(x="Fuel Consumption City (L/100km)", y="CO2 Emissions (g/km)", c=data["Fuel Type"].map(colors), s=50)
plt.show()
'''


'''
najmanje ima natural gas odnosno nema ga, zatim dizel pa ethanol pa premium i regular gasoline
najmanje iispustanje co2 ima regular gasoline pa premium itd
'''


'''
data.boxplot(column=['Fuel Consumption Hwy (L/100km)'], by='Fuel Type')
plt.show()
'''


'''
premium gasoline ima najviše odstupanja iznad, ethanol i regular nemaji nekih ekstrema a za dizel imamo i oni koji su manji i veci
'''


'''
fuel_counts = data.groupby("Fuel Type").size()
plt.figure()
plt.bar(fuel_counts.index, fuel_counts.values)
plt.show()

'''

'''
imamo najmanje ethanola i dizela(oko 50 od svakog) a gasoline imamo puno vise (oko 1000), natural gas nemamo
'''

cylinder_grouped = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
cylinder_grouped.plot(kind='bar', x=cylinder_grouped.index, y=cylinder_grouped.values, xlabel='Cylinders', ylabel='CO2 emissions (g/km)', title='CO2 emissions by number of cylinders')
plt.show()
