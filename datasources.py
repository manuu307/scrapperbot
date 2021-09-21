import sqlite3

class Datasource():
	"""docstring for DB"""
	db = "DB.db"
	con = 'dbconnection'
	cur = 'cursor'
	def __init__(self):
		self.con = sqlite3.connect(str(self.db))
		self.cur = self.con.cursor()
		
	def create_table(self):
		try:
			# Create table
			self.cur.execute('''CREATE TABLE property
               (id INTEGER PRIMARY KEY, date TEXT, price NUMBER, currency TEXT, rooms NUMBER, bath NUMBER, m2 NUMBER, name TEXT, description TEXT, location TEXT )''')
			print("Table created successfully")
		except Exception as e:
			print(e)
		
	def insert(self, table, data):
		try:
			# Insert a row of data
			self.cur.executemany("INSERT INTO {str(self.table)} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?), {str(self.data)}")
			# Save (commit) the changes
			self.con.commit()
		except Exception as e:
			print(e)
		
	def close_conn(self):
		self.con.close()






