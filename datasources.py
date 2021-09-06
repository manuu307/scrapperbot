import sqlite3

class Datasource():
	"""docstring for DB"""
	con = 'dbconnection'
	cur = con.cursor()
	def __init__(self, db):
		self.db = db
		self.con = sqlite3.connect(str(self.db))
		print(self.con)
		
	def create_table(self):
		try:
			# Create table
			self.cur.execute('''CREATE TABLE property
               (id INTEGER PRIMARY KEY, date TEXT, price NUMBER, currency TEXT, rooms NUMBER, bath NUMBER, m2 NUMBER, name TEXT, description TEXT, location TEXT )''')
			print("Table created successfully")
		except Exception as e:
			print(e)
		
	def insert (self, table, data):
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
		try:
			# Insert a row of data
			self.cur.executemany("INSERT INTO str(self.table) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?), self.data")
			# Save (commit) the changes
			self.con.commit()
		except Exception as e:
			print(e)
		
	def close_conn (self):
		self.con.close()

datasource = Datasource("DB.db")
datasource.create_table()



