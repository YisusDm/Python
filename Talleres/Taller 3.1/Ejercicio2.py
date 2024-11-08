import random
from playsound import playsound

musicales= ['DO','RE','MI','FA','SOL','LA','SI']
notas=random.choice(musicales)


if notas == musicales[0]:
    print(notas,end="  ")
    playsound("DO.mpeg")
    exit()

while (notas != musicales):
    print(notas,end="  ")
    if notas == musicales[2]:
        playsound("MI.mpeg")
        for i in range(2):
            print(musicales[0], end="  ")
            playsound("DO.mpeg")
            print(musicales[1], end="  ")
            playsound("RE.mpeg")
            print(musicales[2], end="  ")
            playsound("MI.mpeg")
        notas= random.choice(musicales)
    elif notas == musicales[1]:
        playsound("RE.mpeg")
        notas= random.choice(musicales)
        if notas == musicales[3]:
            continue

    elif notas == musicales[0]:
        playsound("DO.mpeg")
        notas= random.choice(musicales)
        if notas == musicales[-1]:
            print(notas,end="  ")
            playsound("SI.mpeg")
            break
    elif notas == musicales[3]:
        playsound("FA.mpeg")
        notas= random.choice(musicales)
        if notas == musicales[-3]:
            print(notas, end="  ")
            playsound("SOL.mpeg")
            break
    elif notas == musicales[-3]:
        playsound("SOL.mpeg")
        notas= random.choice(musicales)
    elif notas == musicales[-2]:
        playsound("LA.mpeg")
        notas= random.choice(musicales)
    elif notas == musicales [-1]:
        playsound("SI.mpeg")
        notas= random.choice(musicales)
        
    