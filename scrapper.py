#import requests
#from bs4 import BeautifulSoup
print("Parser")

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# SETTINGS
site= "https://www.infocasas.com.uy/venta/inmuebles/montevideo"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, "html.parser")

# GET ALL ELEMENTS PRETTIFY
elements = soup.findAll(True, class_="property-card")
number = 0

for x in elements:
	number =+1
	
# PARSE
	items = x.select("div.ant-typography.ant-typography-ellipsis.ant-typography-ellipsis-single-line")
	for y in items:
		print(number, ":", y.prettify())


#URL = "https://www.infocasas.com.uy/venta/inmuebles/montevideo"
#page = requests.get(URL)
#soup = BeautifulSoup(page.content, "html.parser")
#print("SOUP:", soup)
#results = soup.find(class_="property-card")

#print(results.prettify())

#elements = results.find_all("div", class_="card-content")