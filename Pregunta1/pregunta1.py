# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:49:08 2022

@author: Miguel
"""

listAge= [22,15,16,27,20,15,35,28,19,32,33,17,15,15,16,33,26,23,15,26,22,19,26,25,17,27,24,15,34,20,
38,23,48,24,33,34,41,29,22,45,22,35,34,49,19,21,26,51,19,38,36,52,49,23,45,54,47,53,56,27,47,19,33,15,17,29,27,51,35,47,43,15,33,51,45,47,18,
46,43,28,30,16,42,15,53,40,38,46,32,23]

listTime=[2.25,3,10.5,4.5,8,5,9.75,7.5,6,12,6.25,5.75,1.75,5.5,10,9.25,7.75,7.5,6.5,6.75,1.25,2.25,10.5,
5.75,11.25,5,4.75,11,11.5,7.75,2.5,3,10.25,4.25,8,5,11,8.75,8.5,11.25,8.25,8.75,8.5,4.5,11,8,
7.75,8.75,7.75,12,1.75,2.25,9,5.75,10,7.5,5.25,10,11.75,11.25,3.75,2.25,8,4,8.5,5,11.75,6,6.75,10.75,8,4,1.75,4,
6.5,9.25,11.75,7.75,11,11,1,2,8.75,8,7.25,5.5,7.5,11.5,12,6.75]

listNumWart= [14,2,2,9,6,3,2,4,2,6,2,12,1,12,7,2,
6,10,19,2,3,2,6,2,4,2,10,6,12,18,1,2,7,1,3,
7,11,3,5,4,9,10,1,2,5,3,13,2,6,14,10,5,
4,2,8,13,3,1,7,3,14,8,5,12,2,12,8,6,4,8,1,4,7,1,9,
13,5,8,7,3,2,11,8,1,6,8,8,4,9,6]

listType = [3,3,1,3,1,3,2,1,1,3,1,3,2,1,1,2,2,2,
1,1,3,1,1,1,3,1,3,1,1,3,3,3,1,1,1,3,2,1,1,1,
1,2,2,1,2,1,2,2,1,1,3,1,2,1,1,3,3,2,1,2,2,
2,1,1,1,3,1,1,3,1,1,3,2,1,2,2,2,1,1,3,
1,1,2,1,1,3,2,1,1,1]

listArea = [51,900,100,80,45,84,8,9,225,35,30,25,49,48,143,150,6,43,56,6,47,
60,50,300,70,20,30,30,25,45,43,87,50,174,502,64,21,504,99,72,352,69,
163,33,51,17,13,57,32,87,45,63,14,43,58,43,23,30,31,37,67,42,
63,72,44,75,208,80,41,57,59,25,379,65,49,367,13,40,507,91,88,
47,73,55,81,69,56,91,43,19]

listInduDia = [50,70,25,30,8,7,6,2,8,5,3,7,7,7,6,8,5,3,7,6,3,7,9,7,7,5,
45,25,50,2,50,70,25,30,8,7,6,2,8,5,3,7,7,7,6,8,5,3,7,6,3,
7,9,7,7,5,45,25,50,2,50,70,25,30,8,7,6,2,8,5,3,7,7,7,6,8,5,
3,7,6,3,7,9,7,7,5,45,25,50,2]

#a)

listAge.sort()
listTime.sort()
listNumWart.sort()
listType.sort()
listArea.sort()
listInduDia.sort()

print ("Inciso a)")
print ("--------Primer Cuartil--------")

print("El 25% de las personas sometidas al trataminento de inmunoterapia tienen una edad de anios: ",listAge[22]+ 0.25*(listAge[23]-listAge[22]))
print("El 25% de las personas estuvieron con berrugas antes de su tratamiento meses: ",listTime[22]+ 0.25*(listTime[23]-listTime[22]))
print("El 25% de las personas tuvo verrugas: ",listNumWart[22]+ 0.25*(listNumWart[23]-listNumWart[22]))
print("El 25% de las personas tuvieron verrugas del tipo: ",listType[22]+ 0.25*(listType[23]-listType[22]))
print("El 25% de las personas tuvo la verruga mas grande con un area de (mm2): ",listArea[22]+ 0.25*(listArea[23]-listArea[22]))
print("El 25% de las personas tuvo en la prueba inicial el diametro de induracion(mm): ",listInduDia[22]+ 0.25*(listInduDia[23]-listInduDia[22]))

print ("--------Percentil 50--------")

print("El 50% de las personas sometidas al trataminento de inmunoterapia tienen una edad de anios: ",(listAge[45]+listAge[44])/2)
print("El 50% de las personas estuvieron con berrugas antes de su tratamiento meses : ",(listTime[45]+listTime[44])/2)
print("El 50% de las personas tuvo verrugas: ",(listNumWart[45]+listNumWart[44])/2)
print("El 50% de las personas tuvieron verrugas del tipo: ",(listType[45]+listType[44])/2)
print("El 50% de las personas tuvo la verruga mas grande con un area de (mm2): ",(listArea[45]+listArea[44])/2)
print("El 50% de las personas tuvo en la prueba inicial el diametro de induracion(mm): ",(listInduDia[45]+listInduDia[44])/2)

#b)

import pandas as pd
import numpy as np

data = pd.read_csv("inmunoterapia.csv")

print ("Inciso b)")
print ("--------Primer Cuartil--------")
print ("Edad Q1 = ",np.quantile(data["age"], 0.25))
print ("Tiempo Q1 = ",np.quantile(data["Time"], 0.25))
print ("Numero de Berrugas Q1 = ",np.quantile(data["Number_of_Warts"], 0.25))
print ("Tipo Q1 = ",np.quantile(data["Type"], 0.25))
print ("Area Q1 = ",np.quantile(data["Area"], 0.25))
print ("Diamero de induracion Q1 = ",np.quantile(data["induration_diameter"], 0.25))
print ("--------Percentil 50--------")

print ("Edad P50 = ",np.percentile(data["age"], 50))
print ("Tiempo P50 = ",np.percentile(data["Time"], 50))
print ("Numero de Berrugas P50 = ",np.percentile(data["Number_of_Warts"], 50))
print ("Tipo P50 = ",np.percentile(data["Type"], 50))
print ("Area P50 = ",np.percentile(data["Area"], 50))
print ("Diamero de induracion P50 = ",np.percentile(data["induration_diameter"], 50))

#c)


import matplotlib.pyplot as plt
df = pd.DataFrame(data)


x_values = df['age'].unique()
y_values = df['age'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.xlabel("Edad (anios)") 
plt.ylabel("Numero Personas")
plt.text(30, 8, "La edad de las personas que tuvieron verrugas\n es al rededor de los 22 anio")
plt.show()

x_values = df['Time'].unique()
y_values = df['Time'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.xlabel("Tiempo (meses)") 
plt.ylabel("Numero Personas")
plt.text(4, 6, "Se muestra el tiempo transcurrido antes del tratamiento \nSe nota que el punto maximo es de 2 meses")
plt.show()

x_values = df['Number_of_Warts'].unique()
y_values = df['Number_of_Warts'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.xlabel("Numero de Berrugas") 
plt.ylabel("Numero Personas")
plt.text(1, 16, "Se muestra el numero de berrugas con las que empezaron el tratamiento\nEl numero mas comun de verrugas es de 15 que \nsufrieron 16 personas")
plt.show()

x_values = df['Type'].unique()
y_values = df['Type'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.xlabel("Tipo de Berrugas") 
plt.ylabel("Numero Personas")
plt.text(1, 48, "Se muestra el tipo de verruga siendo el de tipo 3 mas recurrente\n1. Comun \n2. Plantar \n3. Ambos")
plt.show()

x_values = df['Area'].unique()
y_values = df['Area'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.xlabel("Area (mm2)") 
plt.ylabel("Numero Personas")
plt.text(1, 5, "Se muestra el area de una verruga expresada en mm2 \n")
plt.show()

x_values = df['induration_diameter'].unique()
y_values = df['induration_diameter'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.xlabel("Diametro de induracion (mm)") 
plt.ylabel("Numero Personas")
plt.text(1, 25, "Muestra el diametro de induracion alrededor de la verruga\ndonde el diametro comun es de 50 mm ")
plt.show()

x_values = df['Result_of_Treatment'].unique()
y_values = df['Result_of_Treatment'].value_counts().tolist()
plt.bar(x_values,y_values)
plt.xlabel("Resultado de Tratamiento") 
plt.ylabel("Numero Personas")
plt.text(0.5, 70, "Muestra el resultado del tratamiento para desaparecer las verrugas \nDonde existe una mayoria de eficacia en el tratamiento")
plt.show()

#serie_Time = df.Time.value_counts()
#serie_Time = serie_Time.sort_index(ascending = True)
#serie_Time.plot.bar()
#plt.xlabel("Tiempo") 
#plt.ylabel("Numero Personas")
