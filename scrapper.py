print("Parser")

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class Scrapper():
	hdr = 'headers'
	req = 'request'
	page = 'page'
	soup = 'soup'
	def __init__(self, site):
		# SETTINGS
		self.site = site
		self.hdr = {'User-Agent': 'Mozilla/5.0'}
		self.req = Request(site, headers=self.hdr)
		self.page = urlopen(self.req)
		self.soup = BeautifulSoup(self.page, "html.parser")

	def scrapping(self, prop_title, prop_price, prop_rooms, prop_desc, prop_loc):
		# GET ALL ELEMENTS PRETTIFY
		elements = self.soup.findAll(True, class_="property-card")
		number = 0

		for x in elements:
			number = number + 1
		# PARSE

			#Title
			self.prop_title = x.select(prop_title)
			for title in self.prop_title:
				print(number, ":", title.text)

			#Price
			self.prop_price = x.select(prop_price)
			for price in self.prop_price:
				print(number, ":", price.text)

			#Curency
			self.prop_currency = x.select(prop_price)
			for currency in self.prop_currency:
				if "U$S" in currency.text:
					print(number, ":", "Dolar")
				else:
					print(number, ":", "Peso")

			#Caracteristics
			self.prop_rooms = x.findAll(class_= prop_rooms) 
			for caracteristic in self.prop_rooms:

				#Rooms
				if "Mono" in caracteristic.text:
					print(number, ":", caracteristic.text)
				if "Dorm" in caracteristic.text:
					print(number, ":", caracteristic.text)

				#RestRoom
				if "Baño" in caracteristic.text:
					print(number, ":", caracteristic.text)

				#M2
				if "m²" in caracteristic.text:
					print(number, ":", caracteristic.text)

			#Description
			self.prop_desc = x.find(class_= prop_desc)
			for desc in self.prop_desc:
				if desc:
					print(number, ":", desc.text)
				else:
					print(number, ":", "Sin descripcion")
			#Location
			self.prop_loc = x.select(prop_loc)
			#print(prop_loc.text)
			for loc in self.prop_loc:
				print(number, ":", loc.find(text=True, class_= "ant-typography").getText())
		


	"""
			Data Model array example:
			
			self.data = [
	    		("date", today),
	    		("price", 1000),
	    		("currency", $),
	    		("rooms", 3),
	    		("bath", 1),
	    		("m2", 100),
	    		("name", "Casa bonita"),
	    		("description", "Casa muy iluminada"),
	    		("location", "Montevideo, Uruguay"),	
					]

			"""
Scrapper("https://www.infocasas.com.uy/venta/inmuebles/montevideo").scrapping("h4.property-title", "span.price", "ant-typography ant-typography-ellipsis", "property-description", "span.property-location-tag")