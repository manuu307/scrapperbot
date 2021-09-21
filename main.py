from scrapper import *
from datasources import *
datasource = Datasource()

properties = Scrapper(
	site= "https://www.infocasas.com.uy/venta/inmuebles/montevideo"
	).scrapping(
	prop_title = "h4.property-title", 
	prop_price = "span.price", 
	prop_rooms = "ant-typography ant-typography-ellipsis", 
	prop_desc = "property-description", 
	prop_loc = "span.property-location-tag",
	)


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

data = json.loads(properties)
for obj in data:
	data = [obj['p_title'], obj['p_price'], obj['p_currency'], obj['p_rooms'], obj['p_restroom'], obj['p_size'], obj['p_description'], obj['p_local']]
	print(data)
	datasource.insert(table="property", data=data)
datasource.close_conn()
	