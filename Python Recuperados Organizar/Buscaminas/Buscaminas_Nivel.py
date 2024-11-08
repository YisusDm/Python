import random

Diff = None  # dificultad
Cap = None
Diff1Alph = 'ABCDEFGH'  # primer renglon dificultad 1
Diff2Alph = 'ABCDEFGHI'  # primer renglon dificultad 2
Diff3Alph = 'ABCDEFGHIJ'  # primer renglon dificultad 3
Board = list()  # tablero visible
HiddenBoard = list()  # tablero no visible
Prob = list()
ProbMina1 = 1
ProbNoMina1 = 7
ProbMina2 = 2
ProbNoMina2 = 8
ProbMina3 = 3
ProbNoMina3 = 10


def Index():
    global Diff, Cap, Prob, Board, HiddenBoard, MineBoard, HintBoard, AuxiliarBoard  # dificultad, tablero, tablero oculto, tablero de minas, tablero de pistas
    print("""= = = = = = = = = = = = = = =
   Bienvenido al Buscaminas
= = = = = = = = = = = = = = =
   Niveles del Buscaminas
	> 1. Facil
	> 2. Medio
	> 3. Dificil""")
    DiffLvl = int(input("Ingrese el numero del nivel: "))  # Se ingresa la dificultad
    if DiffLvl == 1:
        Diff = 8
        Cap = Diff1Alph
        for times in range(ProbNoMina1): Prob.append(0)  # Se llena la lista probabilidad con las bombas y no bombas correspondientes al nivel
        for times in range(ProbMina1): Prob.append('@')  # 0 son no bombas y arroba son bombas
    elif DiffLvl == 2:
        Diff = 9
        Cap = Diff2Alph
        for times in range(ProbNoMina2): Prob.append(0)
        for times in range(ProbMina2): Prob.append('@')
    elif DiffLvl == 3:
        Diff = 10
        Cap = Diff3Alph
        for times in range(ProbNoMina3): Prob.append(0)
        for times in range(ProbMina3): Prob.append('@')
    else:
        print("Valor invalido. Intente de nuevo")
    Board = New_Board(Diff)
    HiddenBoard = Hidden_Board(Diff)
    MineBoard = Mine_Board(HiddenBoard)
    HintBoard = Hint_Board(MineBoard)
    AuxiliarBoard = HintBoard


def New_Board(Row):  # crea un tablero vacio
    Board1 = list()  # creo el tablero
    for Rows in range(Row):
        Line = list()  # creo la linea
        for Columns in range(Row):  # lleno la linea
            Line.append("*")
        Board1.append(Line)
    return Board1


def Hidden_Board(Row):  # Crea el tablero con las minas y no minas
    Board2 = list()
    for Rows in range(Row):
        Line = list()
        for Columns in range(Row):
            Line.append(random.choice(Prob))
        Board2.append(Line)
    return Board2


def Show_Board(BoardX):  # imprime un tablero
    print()
    Sup = list()
    for letter in Cap:
        Sup.append(letter)
    print(' ', end=' ')
    for element in range(len(Sup)):
        print(element + 1, end=' ')
    print()
    for i in range(len(Sup)):
        print(Sup[i], end=' ')
        for e in BoardX[i]: print(e, end=' ')
        print()


def Mine_Board(BoardX):  # pone las pistas
    MineBoard1 = list()
    for x in range(len(BoardX)):
        Line = list()
        for y in range(len(BoardX)):
            Line.append(BoardX[x][y])
        MineBoard1.append(Line)

    for x in range(len(MineBoard1)):
        for y in range(len(MineBoard1)):
            if HiddenBoard[x][y] == '@':
                for e in range(-1, 2, 1):
                    for k in range(-1, 2, 1):
                        try:
                            MineBoard1[abs(x + e)][abs(y + k)] += 1
                        except:
                            continue
            else:
                continue
    return (MineBoard1)


def Hint_Board(BoardX):  # Organiza el tablero oculto
    HintBoard1 = list()
    for x in range(len(BoardX)):
        Line = list()
        for y in range(len(BoardX)):
            if MineBoard[x][y] != '@':
                Line.append(MineBoard[x][y])
            else:
                Line.append('*')
        HintBoard1.append(Line)
    return HintBoard1


def Revealer(x, y):
    AuxiliarBoard[x][y] = '0'
    for k in [-1, 0, 1]:
        for e in [-1, 0, 1]:
            try:
                Board[abs(x + k)][abs(y + e)] = HintBoard[abs(x + k)][abs(y + e)]
                if AuxiliarBoard[abs(x + k)][abs(y + e)] == 0:
                    Revealer(abs(x + k), abs(y + e))
            except:
                pass


def InGame():
    CapN = list(Cap)
    print("""= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
Para jugar debes indicar de la siguiente manera: A1, B2, C3...
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =""")
    while True:
        if Board == HintBoard:
            print("Ganaste")
            break
        Show_Board(Board)
        Play = input("Indica tu siguiente jugada: ")
        Letter = Play[0]

        if len(Play) == 2:
            Number = Play[1]
        else:
            Number = Play[1:100]
        LetterN = int(CapN.index(Letter))
        NumberN = int(Number) - 1
        if MineBoard[LetterN][NumberN] == '@':
            Show_Board(MineBoard)
            print("Perdiste")
            break
        elif MineBoard[LetterN][NumberN] != 0:
            Board[LetterN][NumberN] = MineBoard[LetterN][NumberN]
            continue
        else:
            Board[LetterN][NumberN] = MineBoard[LetterN][NumberN]
            Revealer(LetterN, NumberN)


Index()
InGame()