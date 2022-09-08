import requests
from serpapi import GoogleSearch
import re

siteFiable = ["lefigaro.fr", "bfmtv.fr", "ouest-france", "lemonde.fr", "franceinfo.fr", "20minutes.fr",
              "leparisien.fr", "actu.fr",
              "ladepeche.fr", "lci.fr", "sudouest.fr", "bouserama.fr", "lepoint.fr", "francebleu.fr", "capital.fr",
              "franceinter.fr", "rfi.fr", "ladepeche.fr",
              "france24.com", "franceculture.fr", "letelegramme.fr", "bfmtv.com", "francetvinfo", "leparisien",
              "ladepeche.fr", "voici.fr", "sudouest.fr", "midilibre.fr", "lindependant.fr", "lepoint.fr", "cnews"]

siteConnu = [".gouv.fr", ".asso.fr"]


def searchGoogle(question, url):
    search = GoogleSearch({
        "q": question,
        "location": "Paris,France",
        "api_key": "a19ab2cfa90d3c44726df8333a905109562e325cb8d669389da7adfc118cfb1a",
        "lr": "https://serpapi.com/locations.json?q=Paris&limit=5",
        "google_domain": "google.com",
        "hl": "fr",
        "gl": "fr",
        "num": 40
    })

    result = search.get_dict()

    resultTab = []
    for i in result["organic_results"]:
        link = i["link"]
        for y in siteFiable:
            if y in link and link != url:
                resultTab.append(link)

    for i in result["organic_results"]:
        link = i["link"]
        for y in siteConnu:
            if y in link and link != url:
                resultTab.append(link)

    return resultTab


import regex


def getSourceCode(url):
    cd = {'sessionid': '123..'}

    r = requests.get(url, cookies=cd)
    codeSource = r.content
    return str(codeSource)


def getSubject(codeSource: str):
    sub = codeSource

    x = re.findall("<h1(.*?)>(.*?)<", codeSource)
    return (x[0][1])


def getSubjectByUlr(url: str):
    subject = url.replace("-", " ").split("/")

    if len(subject[-1]) > 0:
        return subject[-1]
    else:
        return subject[-2]


def fakeNewsAnalyse(url):
    codeSource = getSourceCode(url)
    fiability = 0
    analysePercent = 5
    authorPercent = 10
    urlIsSafe = UrlAnalyse(url)

    if site_fiable(url):
        fiability = 15

    if urlIsSafe:
        fiability += analysePercent

    authorAnalyse = AuthorAnalyse(codeSource)
    fiability += authorAnalyse * authorPercent
    authorLink = authorAnalyse == 1
    authorFound = authorAnalyse == 0.5 or authorLink

    subject = getSubjectByUlr(url)

    linkTab = searchGoogle(subject, url)
    print(linkTab)

    if len(linkTab) > 0:
        fiability += 15
        fiability += 15 * len(linkTab)

    for i in linkTab:
        print(comparaisonTexte(url, linkTab[i]))

    if site_reconnu(url) or fiability > 99:
        fiability = 99.99

    siteInformations = {
        "fiability": str(int(fiability)) + "%",
        "info": {
            "urlIsSafe": urlIsSafe,
            "authorFound": authorFound,
            "authorLink": authorLink,
            "webLink": linkTab,
            "subjectFound": subject
        }
    }

    print("FINAL RESULT FIABILITY : ", fiability, "%")
    return siteInformations


def UrlAnalyse(url):
    if "https" in url:
        print("UrlAnalyse : Ok !")
        return True
    else:
        print("UrlAnalyse : not ok")
        return False


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




def MotsClés(listeMots):
    motsClés = []
    for mot in listeMots:
        if len(mot) > 4 and len(mot) < 15:
            motsClés.append(mot)
    return motsClés


def comparaisonTexte(Url1, Url2):
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
    reponse = "Le premier texte de l'article contient {len1} mots et le deuxième contient {len2} mots. Il y a {cpt} itérations de mots clés.".format(
        len1=len(listeMots1), len2=len(listeMots2), cpt=cpt)
    return reponse


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
    for i in siteConnu:
        if i in url:
            return True


def site_fiable(url):
    for i in siteFiable:
        if i in url:
            return True


fakeNewsAnalyse(
    'https://www.futura-sciences.com/tech/definitions/informatique-fake-news-17092/')
