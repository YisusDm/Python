import random
musicales= ['DO','RE','MI','FA','SOL','LA','SI']
notas=random.choice(musicales)

if notas == musicales[0]:
    print(notas,end="  ")
    exit()

while (notas != musicales):
    print(notas,end="  ")
    if notas == musicales[2]:
        for i in range(2):
            print(musicales[0], end="  ")
            print(musicales[1], end="  ")
            print(musicales[2], end="  ")
        notas= random.choice(musicales)
    elif notas == musicales[1]:
        print("RE",end="  ")
        notas= random.choice(musicales)
        if notas == musicales[3]:
            continue

    elif notas == musicales[0]:
        print("DO",end="  ")
        notas= random.choice(musicales)
        if notas == musicales[-1]:
            print(notas,end="  ")
            break
    elif notas == musicales[3]:
        print("FA",end="  ")
        notas= random.choice(musicales)
        if notas == musicales[-3]:
            print(notas, end="  ")
            break
    elif notas == musicales[-3]:
        notas= random.choice(musicales)
    elif notas == musicales[-2]:
        notas= random.choice(musicales)
    elif notas == musicales [-1]:
        notas= random.choice(musicales)