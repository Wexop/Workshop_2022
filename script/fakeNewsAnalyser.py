import requests
import regex

def getSourceCode(url):
    cd = {'sessionid': '123..'}

    r = requests.get(url, cookies=cd)
    codeSource = r.content
    return codeSource


def fakeNewsAnalyse(url):
    codeSource = getSourceCode(url)

    fiability = 0
    analysePercent = 5
    authorPercent = 10

    if UrlAnalyse(url):
        fiability += analysePercent
    fiability += AuthorAnalyse(codeSource) * authorPercent


    print("FINAL RESULT FIABILITY : ", fiability, "%")

    return str(int(fiability)) + "%"


def UrlAnalyse(url):
    if "https" in url:
        print("UrlAnalyse : Ok !")
        return True
    else:
        print("UrlAnalyse : not ok")

def delHeaderFooter(url):
    sourceCode = str(getSourceCode(url))
    sourceCode = sourceCode.split("</header>")
    sourceCode = str(sourceCode[-1])
    sourceCode = sourceCode.split("<footer>")
    sourceCode = str(sourceCode[0])
    return sourceCode

def delBalise(sourceCode):
     sourceCode = regex.sub('<.+?>', '', sourceCode)
     return sourceCode

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

sourcecode = delHeaderFooter("https://thewebdev.info/2022/04/03/how-to-pass-variables-from-python-flask-to-javascript/")
writeTxt("sourcecode1", delBalise(sourcecode))
listeMots = readtxt("sourcecode1")

def MotsClés(listeMots):
    motsClés = []
    for mot in listeMots:
        if len(mot) > 4 and len(mot) < 15:
            motsClés.append(mot)
    return motsClés

def comparaisonTexte(Url1, Url2 ):
    sourceCode1 = delBalise(delHeaderFooter(Url1))
    sourceCode2 = delBalise(delHeaderFooter(Url2))
    writeTxt("sourcecode1", delBalise(sourceCode1))
    writeTxt("sourcecode2", delBalise(sourceCode2))
    listeMots1 = readtxt("sourcecode1")
    listeMots2 = readtxt("sourcecode2")
    listeMots1 = MotsClés(listeMots1)
    listeMots2 = MotsClés(listeMots2)
    cpt = 0
    for mot in listeMots1:
        for mot2 in listeMots2:
            if mot == mot2:
                cpt += 1
    reponse = "Le premier texte de l'article contient {len1} mots et le deuxième contient {len2} mots. Il y a {cpt} itérations de mots clés.".format(len1 = len(listeMots1), len2 = len(listeMots2), cpt = cpt)
    return reponse

print(comparaisonTexte("https://www.francetvinfo.fr/monde/europe/manifestations-en-ukraine/direct-guerre-en-ukraine-l-onu-juge-credibles-les-accusations-d-enfants-transferes-de-force-en-russie-moscou-denonce-une-legende_5349115.html", "https://www.20minutes.fr/monde/3347107-20220907-guerre-ukraine-direct-malgre-rapport-inquietant-aiea-tirs-visent-encore-centrale-zaporojie"))













def AuthorAnalyse(code):
    tab = str(code).split("<")
    author = False
    href = False
    fiabilty = 0

    for i in range(len(tab)):
        test = tab[i].lower()
        if "author" in str(test):
            if "author" in tab[i]:
                author = True
            if "author" in tab[i] and "href" in tab[i]:
                href = True
    if author:
        fiabilty += 0.5
        print("Author is there !")
    else:
        print("No author found...")
    if href:
        print("Author have a link !")
        fiabilty += 0.5
    else:
        print("No author link found...")

    return fiabilty




fakeNewsAnalyse('https://thewebdev.info/2022/04/03/how-to-pass-variables-from-python-flask-to-javascript/')
