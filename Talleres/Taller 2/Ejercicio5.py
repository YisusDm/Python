Parcial1 = float(input('Ingrese la nota del parcial #1: '))
Parcial2 = float(input('Ingrese la nota del parcial #2: '))

NotaDef = 0
PromExams = (Parcial1 + Parcial2)/2

if PromExams >= 2.0:
    print('Usted puede presentar el examen final, ya que su promedio fue: ', PromExams)
    ExF = float(input('Digite la nota de su examen final: '))   
else:
    print('Su promedio no fue suficiente para poder realizar el examen final.')


if ExF < 2.0:
    NotaDef = ExF
else:
    NotaDef = (Parcial1*0.3)+(Parcial2*0.2)+(ExF*0.4)

if NotaDef >= 3.0:
    print('Aprobaste la asignatura con una nota de ', NotaDef)
else:
    if ExF >= 2.0:
        print('Puedes recuperar la materia y la nota definitiva será la que obtengas en esta habilitación.')





