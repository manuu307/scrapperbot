import requests
from bs4 import BeautifulSoup

print("Parser")

URL = "https://www.synergym.com.uy/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="info-gym")

print(results.prettify())

job_elements = results.find_all("div", class_="card-content")