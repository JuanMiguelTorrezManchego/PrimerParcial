# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:14:48 2022

@author: Miguel
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler

#1_
data = pd.read_csv("inmunoterapia.csv")
df = pd.DataFrame(data)
df.at[1,'Time'] = None
df.at[14,'Time'] = None
df.at[58,'Time'] = None
df.at[27,'Time'] = None
df.at[17,'Number_of_Warts'] = None
df.at[31,'Number_of_Warts'] = None
df.at[71,'Number_of_Warts'] = None
df.at[64,'Number_of_Warts'] = None
df.at[7,'induration_diameter'] = None
df.at[41,'induration_diameter'] = None
df.at[12,'Result_of_Treatment'] = np.nan
df.at[22,'Result_of_Treatment'] = np.nan
df.at[0,'Result_of_Treatment'] = np.nan
print ("Datos incompletos")
print (df)

prepro = SimpleImputer(missing_values = np.nan, strategy = "mean")
df[['age','Time','Number_of_Warts','induration_diameter']] = prepro.fit_transform(df[['age','Time','Number_of_Warts','induration_diameter']])

prepro = SimpleImputer(missing_values = np.nan, strategy = "most_frequent")
df[['Result_of_Treatment']] = prepro.fit_transform(df[['Result_of_Treatment']])
print ("Datos completos ")
print(df)


#2)
min_max_scaler = MinMaxScaler()
tiempo = df[['Time']]
scaled_value = min_max_scaler.fit(tiempo)
print ("Columna de Tiempo Normalizada ")
print(min_max_scaler.transform(tiempo)[0:10])

#3)

from sklearn.preprocessing import KBinsDiscretizer
prepro = KBinsDiscretizer(n_bins=9, encode='ordinal', strategy='quantile')
df[['age','Time','Number_of_Warts','Type','Area','induration_diameter']]=prepro.fit_transform(df[['age','Time','Number_of_Warts','Type','Area','induration_diameter']])
print ("Datos Discretizados por cuartiles para que cada intervalo tenga el mismo numero de valores")
print (df)











