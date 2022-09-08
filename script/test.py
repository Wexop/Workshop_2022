import regex
import csv

t = ["Je <div class='vedbe'> \n\nzevzev"]

def writeTxt(nom, sourceCode):
    file = open(nom + ".txt", "w+")
    file.write(sourceCode)
    file.close()

def readtxt(nom):
    file = open(nom + ".txt", "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        contenu = line.split()
    return contenu

def delAntiSlash(contenu):
    n = 0
    for element in contenu:
        print(element)
        for char in element:
            print(char)
            while len(element) < n:
                if char[n] + char[n+1] == '\\':
                    contenu.pop(element.index())
            n+=1
    return contenu

def MotsClés(listeMots):
    for mot in listeMots:
        print(len(mot))

print(readtxt("test"))
MotsClés(readtxt("test"))

