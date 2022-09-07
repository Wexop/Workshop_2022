import requests
from serpapi import GoogleSearch
import re

siteFiable = ["lefigaro.fr", "bfmtv.fr", "ouest-france", "lemonde.fr", "franceinfo.fr", "20minutes.fr",
              "leparisien.fr", "actu.fr",
              "ladepeche.fr", "lci.fr", "sudouest.fr", "bouserama.fr", "lepoint.fr", "francebleu.fr", "capital.fr",
              "franceinter.fr", "rfi.fr", "ladepeche.fr",
              "france24.com", "franceculture.fr", "letelegramme.fr"]

siteConnu = [".gouv.fr", ".asso.fr"]


def searchGoogle(question):
    search = GoogleSearch({
        "q": question,
        "location": "Paris,France",
        "api_key": "a19ab2cfa90d3c44726df8333a905109562e325cb8d669389da7adfc118cfb1a"
    })
    result = search.get_dict()

    resultTab = []

    for i in result["organic_results"]:
        link = i["link"]
        for y in siteFiable:
            if y in link:
                resultTab.append(link)

    for i in result["organic_results"]:
        link = i["link"]
        for y in siteConnu:
            if y in link:
                resultTab.append(link)

    return resultTab


def getSourceCode(url):
    cd = {'sessionid': '123..'}

    r = requests.get(url, cookies=cd)
    codeSource = r.content
    return str(codeSource)


def getSubject(codeSource: str):
    sub = codeSource

    x = re.findall("<h1(.*?)>(.*?)<", codeSource)
    return (x[0][1])


def fakeNewsAnalyse(url):
    codeSource = getSourceCode(url)
    fiability = 0
    analysePercent = 5
    authorPercent = 10
    urlIsSafe = UrlAnalyse(url)

    if site_fiable(url):
        fiability = 50

    if urlIsSafe:
        fiability += analysePercent

    authorAnalyse = AuthorAnalyse(codeSource)
    fiability += authorAnalyse * authorPercent
    authorLink = authorAnalyse == 1
    authorFound = authorAnalyse == 0.5 or authorLink

    subject = getSubject(codeSource)

    linkTab = searchGoogle(subject)
    print(linkTab)

    if len(linkTab) > 0:
        fiability += 30

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
    'https://www.lemonde.fr/idees/article/2022/09/07/le-peuple-ukrainien-a-montre-sa-capacite-a-s-autogouverner-autant-que-la-vigueur-de-ses-aspirations-democratiques_6140516_3232.html')
