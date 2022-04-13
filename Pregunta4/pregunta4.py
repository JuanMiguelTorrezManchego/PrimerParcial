# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:23:06 2022

@author: Miguel
"""

from kanren import run, var, eq,  Relation, facts,conde
a = var()
b=var()
parent = Relation()
facts(parent, ("PaEmilio","Miguel"),("PaEmilio","Ivan"),("AbueMartin","PaEmilio"),("AbueMartin","TiaRosa"),("TiaRosa","Diego"))
print(parent.facts)




def grandparent (A, B):
    X =var()
    return conde((parent(A, X), parent(X, B)))

    
print("El abuelo de Ivan es: ",run(1,a,grandparent(a,"Ivan")))
print("Los hijos del Abuelo Martin son: ",run(2,b,parent("AbueMartin",b)))
print("El papa de Miguel es: ",run(1,a,parent(a,"Miguel")))
print("Los hijos de Emilio son:" ,run(2,b,parent("PaEmilio",b)))
print("La mama del primo Diego es: ",run(1,a,parent(a,"Diego")))
print("El Hijo de la Tia Rosa es: ",run(1,b,parent("TiaRosa",b)))
sol = run(1,a,grandparent(a,"Ivan"))
sol1 = run(2,a,grandparent(sol[0],a))
print ("El primo de Ivan es: ",sol1[1])


