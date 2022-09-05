import requests


def getSourceCode(url):
    cd = {'sessionid': '123..'}

    r = requests.get(url, cookies=cd)
    codeSource = r.content
    return codeSource


def fakeNewsAnalyse(url):
    codeSource = getSourceCode(url)

    fiability = 0

    if UrlAnalyse(url):
        fiability += 5
        print("UrlAnalyse : Ok !")
    else:
        print("UrlAnalyse : not ok")

    print("FINAL RESULT FIABILITY : ", fiability, "%")


def UrlAnalyse(url):
    return "https" in url


fakeNewsAnalyse('https://thewebdev.info/2022/04/03/how-to-pass-variables-from-python-flask-to-javascript/')