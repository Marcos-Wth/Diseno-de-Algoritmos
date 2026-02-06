#######################################################
#######################################################
#                                                     #
#            Diseño de Algoritmos 2015-2017           #
#                                                     #
#            Práctica 1                               #
#                                                     #
#            sorting                                  #
#                                                     #
#######################################################

import matplotlib.pyplot as plt

import random
from time import time
import numpy as np
import numpy.polynomial as P


def Burbuja(a,n):
    for i in range(1,n):
        for j in range(0,n-i):
            if(a[j] > a[j+1]):
                k = a[j+1]
                a[j+1] = a[j]
                a[j] = k

def Insercion(a,n):
    for i in range(1,n):
        v=a[i]
        j=i-1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j=j-1
        a[j+1]=v

def Seleccion(a,n):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min=j
        aux=a[min]
        a[min]=a[i]
        a[i]=aux

def QuickSort(a,iz,de):
    i=iz
    j=de
    #
    # Selección del pivote
    # Elegir uno a descomentar
    #
    # Pivote en la mediana
    #x=a[int((iz + de)/2)]
    # Pivote en el lado izquierdo
    x=a[iz]
 
    while( i <= j ):
        while a[i]<x and j<=de:
            i=i+1
        while x<a[j] and j>iz:
            j=j-1
        if i<=j:
            aux = a[i]; a[i] = a[j]; a[j] = aux
            i=i+1;  j=j-1
 
    if iz < j:
        QuickSort( a, iz, j )
    if i < de:
        QuickSort( a, i, de )

def MergeSort(a,n):
    if n>1:
        m = n//2
        l = a[:m]
        r = a[m:]

        MergeSort(l,len(l))
        MergeSort(r,len(r))

        i=0; j=0; k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k]=l[i]
                i=i+1
            else:
                a[k]=r[j]
                j=j+1
            k=k+1

        while i < len(l):
            a[k]=l[i]
            i=i+1
            k=k+1

        while j < len(r):
            a[k]=r[j]
            j=j+1
            k=k+1

def GeneraR(n):
    a=[]
    for i in range(0,n):
        a.append(random.randrange(0, n, 1))
    return a
    
def GeneraD(n):
    a=[]
    for i in range(0,n):
        a.append(i)
    return a   

def GeneraI(n):
    a=[]
    for i in range(0,n):
        a.append(n-i)
    return a   
    
def imprime(a,n):
    for i in range(0,n):
        print (a[i])
        
def experimento(n):
    V1 =[] 
    V2 =[]  
    V3 =[] 

# Orden directo
    V2=GeneraD(n)
# Orden inverso
    V3=GeneraI(n)
# Experimento aleatorio
    tb = 0
    ti = 0
    ts = 0
    for i in range(1,10):
# Aleatorio. 10 experimentos
        V1=GeneraR(n)
        V0=V1[:]       
        t1=time()
        Insercion(V0,len(V0))
        t2=time()-t1
        ti = ti + t2    
        V0=V1[:]
        t1=time()
        Seleccion(V0,len(V0))
        t2=time()-t1
        ts = ts + t2
        V0=V1[:]
        t1=time()
        Burbuja(V0,len(V0))
        t2=time()-t1
        tb = tb + t2
    TI1.append(ti/10)   
    TS1.append(ts/10)  
    TB1.append(tb/10)  
# Experimento directo
    V0=V2[:]       
    t1=time()
    Insercion(V0,len(V0))
    t2=time()-t1    
    TI2.append(int(1000*t2))
    V0=V2[:]
    t1=time()
    Seleccion(V0,len(V0))
    t2=time()-t1
    TS2.append(int(1000*t2))
    V0=V2[:]
    t1=time()
    Burbuja(V0,len(V0))
    t2=time()-t1
    TB2.append(int(1000*t2))
    # Experimento inverso
    V0=V3[:]       
    t1=time()
    Insercion(V0,len(V0))
    t2=time()-t1    
    TI3.append(int(1000*t2))
    V0=V3[:]
    t1=time()
    Seleccion(V0,len(V0))
    t2=time()-t1
    TS3.append(int(1000*t2))
    V0=V3[:]
    t1=time()
    Burbuja(V0,len(V0))
    t2=time()-t1
    TB3.append(int(1000*t2))  

X  =[]
TI1=[]
TS1=[]  
TB1=[]  
TI2=[]
TS2=[]  
TB2=[] 
TI3=[]
TS3=[]  
TB3=[]  
for i in range(1,21):
    experimento(250*i)
    X.append(i*250)
v=GeneraD(500)
QuickSort(v,0,len(v)-1)
zi = np.polyfit(X, TI1, 2)
zs = np.polyfit(X, TS1, 2)
zb = np.polyfit(X, TB1, 2)

Tam=[1,2,3,4,5,6,7,8,9]

plt.plot(Tam,TI1,'r--',Tam,TS1,'bs',Tam,TB1,'g^')
plt.title('Burbuja') #Creo que que esto es tiempo con orden aleatorio
plt.ylabel('Tiempo (s)')
plt.xlabel('Nodos (x 100)')
plt.show()

plt.plot(Tam,TI2,'r--',Tam,TS2,'bs',Tam,TB2,'g^')
plt.title('Inserción') #Creo que que esto es tiempo con orden directo
plt.xlabel('Nodos (x 100)')
plt.show()

plt.plot(Tam,TI3,'r--',Tam,TS3,'bs',Tam,TB3,'g^')
plt.title('Selección') #Creo que que esto es tiempo con orden inverso
plt.ylabel('Tiempo (s)')
plt.xlabel('Nodos (x 100)')
plt.show()

print(TI1,Tam)