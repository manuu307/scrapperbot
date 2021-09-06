import requests

URL = "https://www.synergym.com.uy/"
r = requests.get(URL)

print(r.headers)
print(r.encoding)
#print(r.text)
print(r.json())