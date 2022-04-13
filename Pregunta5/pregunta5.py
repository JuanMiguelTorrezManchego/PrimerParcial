# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:43:21 2022

@author: Miguel
"""

import pandas as pd
from sklearn import tree
from IPython.display import Image
from six import StringIO
from sklearn.tree import export_graphviz
import pydot
import graphviz

clasificador = tree.DecisionTreeClassifier()
data = pd.read_csv("inmunoterapia.csv")
df = pd.DataFrame(data)
x = df[['age','Time','Number_of_Warts','Type','Area','induration_diameter']].values
df.loc[df.Result_of_Treatment=="yes", 'Result_of_Treatment'] = 1
df.loc[df.Result_of_Treatment=="no", 'Result_of_Treatment'] = 0
y= df['Result_of_Treatment'].values.astype('int64')
print(y)    
print(x)
clasificador=clasificador.fit(x,y)

features = ['age','Time','Number_of_Warts','Type','Area','induration_diameter']
dot_data = tree.export_graphviz(clasificador,out_file=None,feature_names= features,filled=True,rounded=True)
graph = graphviz.Source(dot_data)
print (graph)
Image(graph[0].create_png())

#dot_data = StringIO()
#export_graphviz(clasificador, out_file=dot_data, feature_names = features, filled = True, rounded = True)






