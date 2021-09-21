from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import base64
class Scrapper():
	hdr = 'headers'
	req = 'request'
	page = 'page'
	soup = 'soup'
	def __init__(self, site):
		print("Init... ...")
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
		elements_array = []
		for x in elements:
			number = number + 1
			
		# PARSE

			#Title
			self.prop_title = x.select(prop_title)
			for title in self.prop_title:
				##print(number, ":", title.text)
				title = title.text

			#Price
			self.prop_price = x.select(prop_price)
			for price in self.prop_price:
				#print(number, ":", price.text)
				price = price.text

			#Curency
			self.prop_currency = x.select(prop_price)
			for currency in self.prop_currency:
				if "U$S" in currency.text:
					#print(number, ":", "Dolar")
					currency = "U$S"
				else:
					#print(number, ":", "Peso")
					currency = "$"

			#Caracteristics
			self.prop_rooms = x.findAll(class_= prop_rooms) 
			for caracteristic in self.prop_rooms:

				#Rooms
				if "Mono" in caracteristic.text:
					#print(number, ":", caracteristic.text)
					rooms = caracteristic.text
				if "Dorm" in caracteristic.text:
					#print(number, ":", caracteristic.text)
					rooms = caracteristic.text

				#RestRoom
				if "Baño" in caracteristic.text:
					#print(number, ":", caracteristic.text)
					restroom = caracteristic.text

				#M2
				if "m²" in caracteristic.text:
					#print(number, ":", caracteristic.text)
					size = caracteristic.text

			#Description
			self.prop_desc = x.find(class_= prop_desc)
			for desc in self.prop_desc:
				if desc:
					#print(number, ":", desc.text)
					description = desc.text
				else:
					#print(number, ":", "Sin descripcion")
					description = "Sin descripcion"
			#Location
			self.prop_loc = x.select(prop_loc)
			##print(prop_loc.text)
			for loc in self.prop_loc:
				loc = loc.find(text=True, class_= "ant-typography").getText()
				#print(number, ":", loc.find(text=True, class_= "ant-typography").getText())

			elements_array.append({
				"p_title":title,
				"p_price":price,
				"p_currency":currency,
				"p_rooms":rooms,
				"p_restroom":restroom,
				"p_size":size,
				"p_description":description,
				"p_local":loc,
				})
		
		json_string = json.dumps(elements_array) 
		return json_string 

	
