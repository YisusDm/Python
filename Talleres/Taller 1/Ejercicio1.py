R = int(input("Digite la medida del radio de la figura: "))
H = int(input("Digite la medida de la hipotenusa : "))
co=R
PI=3.1416

AreaCirculo = PI*R**2
AreaSemicirculo = AreaCirculo/2

cav = (H**2)-(co**2) 
ca = cav**0.5

#A=(B*H)/2
AreaTriangulo =(ca*co)

AreaTotal= AreaTriangulo+AreaSemicirculo

#print("",AreaCirculo,"",AreaSemicirculo,"",ca,"",AreaTriangulo)
print("El areal total de la figura es: ",AreaTotal)