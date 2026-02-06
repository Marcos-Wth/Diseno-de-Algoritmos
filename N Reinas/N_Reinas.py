# Este programa resuelve el problema de las N-Reinas usando la búsqueda con vuelta atras (backtracking)

import time


def Crear_tablero(n):

    tablero=[]

    for i in range(n):
        fila=[]
        for j in range(n):
            fila.append(0)
        tablero.append(fila)

    return tablero

def Resolver_tablero(tablero,n=0):
    print('Resolviendo la fila ',n+1)
    if es_factible(tablero,n):
        return tablero
    
    fila_original=tablero[n][:]

    for i in range(len(tablero)):
        tablero[n][i]=1
        if es_prometedor(tablero):
            resultado=Resolver_tablero(tablero,n+1)
            if resultado:
                return resultado
        tablero[n]=fila_original[:]

    return False


def es_factible(tablero,n):

    # Compruebo si es completo
    if n < len(tablero):
        return False

    # No comprubo las filas, pues a la hora de crearlas nunca va a ver 2 reinas en una fila

    # Compruebo las columnas
    for c in range(len(tablero)):
        visto=False
        for f in range(len(tablero)):
            if tablero[f][c]==1:
                if visto==True:
                    return False
                visto=True

    #Comprueba las diagonales de izquierda a derecha, convirtiendolas primero a vectores, para hacerlo más facil
    diagonales_derecha=Convertir_diagonales_derecha(tablero)
    for diagonal in diagonales_derecha:
        visto=False
        for i in range(len(diagonal)):
            if diagonal[i]==1:
                if visto==True:
                    return False
                visto=True

    #Comprueba las diagonales de derecha a izquierda, convirtiendolas primero a vectores, para hacerlo más facil
    diagonales_izquierda=Covertir_diagonales_izquierda(tablero)
    for diagonal in diagonales_izquierda:
        visto=False
        for i in range(len(diagonal)):
            if diagonal[i]==1:
                if visto==True:
                    return False
                visto=True

    return True


def es_prometedor(tablero):

    # No comprubo las filas, pues a la hora de crearlas nunca va a ver 2 reinas en una fila

    # Compruebo las columnas
    for c in range(len(tablero)):
        visto=False
        for f in range(len(tablero)):
            if tablero[f][c]==1:
                if visto==True:
                    return False
                visto=True

    #Comprueba las diagonales de izquierda a derecha, convirtiendolas primero a vectores, para hacerlo más facil
    diagonales_derecha=Convertir_diagonales_derecha(tablero)
    for diagonal in diagonales_derecha:
        visto=False
        for i in range(len(diagonal)):
            if diagonal[i]==1:
                if visto==True:
                    return False
                visto=True

    #Comprueba las diagonales de derecha a izquierda, convirtiendolas primero a vectores, para hacerlo más facil
    diagonales_izquierda=Covertir_diagonales_izquierda(tablero)
    for diagonal in diagonales_izquierda:
        visto=False
        for i in range(len(diagonal)):
            if diagonal[i]==1:
                if visto==True:
                    return False
                visto=True

    return True



def Convertir_diagonales_derecha(matriz):
    

    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    # Recorrer diagonales comenzando desde el primer elemento hacia la derecha (desde fila 0 hasta la longitud de matriz)
    for k in range(filas):
        diagonal = []
        i, j = k, 0
        while i >= 0 and j < columnas:
            diagonal.append(matriz[i][j])
            i -= 1
            j += 1
        resultado.append(diagonal)

    # Recorrer diagonales comenzando desde el primer elemento de la segunda columna (desde columna hasta longitud) para no repetir la diagonal principal
    for k in range(1, columnas):
        diagonal = []
        i, j = filas - 1, k
        while i >= 0 and j < columnas:
            diagonal.append(matriz[i][j])
            i -= 1
            j += 1
        resultado.append(diagonal)

    return resultado

def Covertir_diagonales_izquierda(matriz):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    # Diagonales que comienzan en la primera fila (de derecha a izquierda)
    for k in range(columnas - 1, -1, -1):
        diagonal = []
        i, j = 0, k
        while i < filas and j < columnas:
            diagonal.append(matriz[i][j])
            i += 1
            j += 1
        resultado.append(diagonal)

    # Diagonales que comienzan en la última columna (sin repetir la principal)
    for k in range(1, filas):
        diagonal = []
        i, j = k, 0
        while i < filas and j < columnas:
            diagonal.append(matriz[i][j])
            i += 1
            j += 1
        resultado.append(diagonal)

    return resultado

def convertir_a_hms(segundos_totales):
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60
    return horas, minutos, segundos

    

tablero=Crear_tablero()
t=time.time()
resultado=Resolver_tablero(tablero)
t=time.time()-t

if resultado:
    for fila in resultado:
        print(fila)
else:
    print(resultado)

th,tm,ts=convertir_a_hms(t)
print("Ha tardado ",th,' horas, ',tm,' minutos y ',ts,' segundos')
print("O lo que es lo mismo, la friolera de ",t,' segundos')