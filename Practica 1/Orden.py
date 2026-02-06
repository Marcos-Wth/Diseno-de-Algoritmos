import time

class Orden:


    def __init__(self,):
        self.tinic=0
        self.tfinal=0

    #Este es el que más tarda de media, aunque a veces da menos que alguno de los otros
    def insercion (self, lista):
        self.tinic=time.time()
        for i in range(1,len(lista)):
            v=lista[i]
            j=i-1
            while j>=0 and lista[j]>v:
                lista[j+1]=lista[j]
                j= j-1
            lista[j+1]=v
        self.tfinal=time.time()
        print(lista)
        print("Insercion ha tardado:",(self.tfinal-self.tinic)," segundos")
        return lista


    #Este es el segundo que menos tarda de media.
    def seleccion(self,lista):
        self.tinic=time.time()
        n=len(lista)
        for i in range(n):
            min=i
            for j in range(i+1,n):
                if lista[j]<lista[min] :
                    min=j
            lista[i], lista[min] = lista[min],lista[i]
        self.tfinal=time.time()
        print(lista)
        print("Seleccion ha tardado:",(self.tfinal-self.tinic)," segundos")
        return lista


    #Este es el que menos tarda, creo que se puede hacer mejor
    def burbuja(self, lista):
        self.tinic=time.time()
        n=len(lista)
        parar=False
        while parar==False:
            parar = True
            for i in range(n-1):
                if lista[i+1]<lista[i]:
                    aux=lista[i+1]
                    lista[i+1]=lista[i]
                    lista[i]=aux
                    cont+=1
                    parar=False
        self.tfinal=time.time()
        print(lista)
        print("Burbuja ha tardado:",(self.tfinal-self.tinic)," segundos")
        return lista



    #Este esta mal hecho pq llamo a burbuja en lugar de llamar a la aplicación de manera recuriva 

    def quicksort(self,lista):
        orden=Orden()
        self.tinic=time.time()
        peq=[]
        gran=[]
        n=len(lista)
        for i in range(n):
            if lista[i]<=lista[0]:
                peq.append(lista[i])
            else:
                gran.append(lista[i])
        peq=orden.burbuja(peq)
        gran=orden.burbuja(gran)
        peq.extend(gran)
        self.tfinal=time.time()
        print(peq)
        print("Quicksort ha tardado:",(self.tfinal-self.tinic)," segundos")
        return peq
        

a=[1,6,0,5,8,9,3,4,53,1000,10,19,2,7,13,89]
orden=Orden()
orden.insercion(a)
orden.seleccion(a)
orden.burbuja(a)
orden.quicksort(a)
