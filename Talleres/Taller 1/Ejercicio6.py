Menu="""("Bienvenido a la tienda.")
("1 - Insertar producto")
("2 - Ver todos")
("3 - Actualizar")
("4 - Eliminar")
("5 - Salir")
("")"""
Mientras = True
while(Mientras):
    print(Menu)
    x = int(input("Elige: "))
    if(x==1):
        print("**Insertar productos**")
        input("**Enter para volver**")
    elif(x==2):
        print("**Ver todos**")
        input("**Enter para volver**")
    elif(x==3):
        print("**Actualizar**")
        input("**Enter para volver**")    
    elif(x==4):
        print("**Eliminar**")
        input("**Enter para volver**")
    elif(x==5):
        print("Salir")
        Mientras = False            
