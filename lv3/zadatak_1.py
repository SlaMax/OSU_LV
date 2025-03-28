import pandas as pd

data = pd.read_csv ('data_C02_emission.csv')

print('a')

print (f"Kolicna mjerenja: {len(data)}")
print(data.dtypes)
x=data.isnull().sum().sum()
if x<=0:
    print("Nema izostavljenih vrijednosti")
else:
    print(f"Ima izostavljenih vrijednosti i to njih: {x}")
    data.dropna(axis=0)
    data.dropna(axis=1)
    data = data.reset_index(drop=True)

print(f"Duplicirano elemenata: {data.duplicated().sum()}")
data.drop_duplicates()
data = data.reset_index(drop=True)

data["Make"] = data["Make"].astype("category")
data["Model"] = data["Model"].astype("category")
data["Vehicle Class"] = data["Vehicle Class"].astype("category")
data["Fuel Type"] = data["Fuel Type"].astype("category")
data["Transmission"] = data["Transmission"].astype("category")

print(data.dtypes)

print('b')

data_b=data.sort_values(by='Fuel Consumption City (L/100km)')
print("Najveća potrošnja \n",data_b[['Make','Model','Fuel Consumption City (L/100km)']].head(3))
print("Najmanja potrošnja \n",data_b[['Make','Model','Fuel Consumption City (L/100km)']].tail(3))



print('c')

data_c=data[(data['Engine Size (L)'] >= 2.5 ) & (data['Engine Size (L)'] < 3.5 )]
print("Broj vozila koje imaju velicinu motora izmedu 2.5 i 3.5 L: ",len(data_c))
print("Prosjek CO2 emisija ",data_c['CO2 Emissions (g/km)'].mean())



print('d')
data_d1=data[(data['Make']=='Audi')]
print("Broj vozila marke Audi: ",len(data_d1))
data_d2=data[(data['Make']=='Audi')&(data['Cylinders']==4)]
print("Prosječna potrošnja Audi-a s 4 cilindra: ",data_d2['CO2 Emissions (g/km)'].mean())



print('e')

data_e4=data[(data['Cylinders']==4)]
data_e6=data[(data['Cylinders']==6)]
data_e8=data[(data['Cylinders']==8)]
print("Broj vozila s 4 clinidra:",len(data_e4))
print("Broj vozila s 6 clinidra:",len(data_e6))
print("Broj vozila s 8 clinidra:",len(data_e8))
print("CO2 vozila s 4 clinidra",data_e4['CO2 Emissions (g/km)'].mean())
print("CO2 vozila s 6 clinidra",data_e6['CO2 Emissions (g/km)'].mean())
print("CO2 vozila s 8 clinidra",data_e8['CO2 Emissions (g/km)'].mean())



print('f')


data_fd=data[(data['Fuel Type']=='D')]
data_fb=data[(data['Fuel Type']=='X')]
print("Prosjacna podrosnja dizela u gradu",data_fd['Fuel Consumption City (L/100km)'].mean())
print("Prosjacna podrosnja regularni benzina u gradu",data_fb['Fuel Consumption City (L/100km)'].mean())
print("median dizela u gradu",data_fd['Fuel Consumption City (L/100km)'].median())
print("median podrosnja regularni benzina u gradu",data_fb['Fuel Consumption City (L/100km)'].median())


print('g')

data_g=data[(data['Fuel Type']=='D')&(data['Cylinders']==4)]
data_g.sort_values(by=['Fuel Consumption City (L/100km)'])
print(data_g[['Make','Model','Fuel Consumption City (L/100km)']].tail(1))



print('h')

data_h=data[(data['Transmission'].str[0] =='M')]
print("Broj vozila s manualnim mjenjacem: ",len(data_h))



print('i')

print(data.corr(numeric_only=True))