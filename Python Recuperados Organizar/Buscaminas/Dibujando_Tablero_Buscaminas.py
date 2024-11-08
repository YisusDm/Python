from tabulate import tabulate
from random import randint
import time
import os

matrizX = []
def matriz(x,y):
    
    for i in range (x):
        matrizY = []
        for ii in range (y):
            matrizY.append("[#]")
        matrizX.append(matrizY)    
    return matrizX
    

def Tablero():
    indice=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    print(tabulate(matriz(15,15), headers=indice, showindex=indice)) 
    # time.sleep(5)
    # limpiar()


def limpiar(): 
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)
Tablero()
#***********************************************************************************