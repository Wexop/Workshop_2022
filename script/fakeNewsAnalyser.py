import requests


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

    if site_reconnu(url) :
        fiability = 99.99


    print("FINAL RESULT FIABILITY : ", fiability, "%")

    return str(int(fiability)) + "%"


def UrlAnalyse(url):
    if "https" in url:
        print("UrlAnalyse : Ok !")
        return True
    else:
        print("UrlAnalyse : not ok")

def SupprHeaderFooter(url):
    sourceCode = str(getSourceCode(url))
    sourceCode = sourceCode.split("</header>")
    sourceCode = str(sourceCode[-1])
    sourceCode = sourceCode.split("<footer>")
    sourceCode = str(sourceCode[0])
    return sourceCode

def supprBalise(sourceCode):
    tmp = ""
    for char in sourceCode:
        if char == "<":
            sourceCodeTmp = sourceCode.split("<", 1)[1]
            while sourceCodeTmp[0] != ">":
                for tmp in sourceCodeTmp:
                    sourceCodeTmp.remove


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


def site_reconnu(url):

    siteConnu = [".gouv.fr", ".asso.fr", ".org"]

    for i in siteConnu:
        if i in url:
            return True


fakeNewsAnalyse('https://thewebdev.info/2022/04/03/how-to-pass-variables-from-python-flask-to-javascript/')
