# 1)desarrolle una aplicacion en donde imprima las veces que sale cada uno de los lados de un dado, 
# si este se lanza 100veces
import random
cara1,cara2,cara3,cara4,cara5,cara6=0,0,0,0,0,0
cara=" "
dado = ["1","2","3","4","5","6"]

print("Lanzando dados...")

for i in range(100):
    cara = random.choice(dado)
    # print(cara,end="-")
    if (cara==dado[0]):
        cara1=cara1+1
    elif (cara==dado[1]):
        cara2+=1
    elif (cara==dado[2]):
        cara3+=1
    elif (cara==dado[3]):
        cara4+=1
    elif (cara==dado[4]):
        cara5+=1
    else:
        cara6+=1    

print("El numero de veces que salio cada cara en los 100 lanzamientos fue de:")
print("Cara #1: [",cara1,"]      ","Cara #2: [",cara2,"]")
print("Cara #3: [",cara3,"]      ","Cara #4: [",cara4,"]")
print("Cara #5: [",cara5,"]      ","Cara #6: [",cara6,"]")                    