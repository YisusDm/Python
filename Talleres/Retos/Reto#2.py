# 2)Desarrolla una aplicacion que genere una carta de naipe 
import random
Color = ["Negro","Rojo"]
Asignacion = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
Figura = ["Tréboles","Diamantes","Corazones","Picas"]

C=random.choice(Color)
F=random.choice(Figura)
A=random.choice(Asignacion)

print(f"La carta obtenida de la baraja es: < [{A}]  {C} de {F} >")