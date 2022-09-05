import requests

url='https://thewebdev.info/2022/04/03/how-to-pass-variables-from-python-flask-to-javascript/'

# in case you need a session
cd = { 'sessionid': '123..'}

r = requests.get(url, cookies=cd)
# or without a session: r = requests.get(url)
print(r.content)