from os import system

def instalarRequisitos():
    pythonVersion = system("py --version")
    if pythonVersion == 0:
        system("py -m pip install tabulate")
    else:
        requisito = system("python -m pip install tabulate")
        if requisito == 1:
            system("python3 -m pip install tabulate")

