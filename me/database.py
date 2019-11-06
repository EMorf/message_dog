import mysql.connector
import config
from datetime import datetime


class Database():
	def __init__(self):
		try:
		  self.cnx = mysql.connector.connect(user=config.user, password=config.pwd,
									  host=config.host,
									  database=config.db)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")

	def query(self, query):
		cursor = self.cnx.cursor()
		cursor.execute(query)
		res = []
		for item in cursor:
			res.append(item)
		return item
	
	def close(self):
		self.cnx.close()
		
	def insert(self, user, msg):
		timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		data = ("INSERT INTO message "
               "(user, msg, time) "
               "VALUES (%s, %s,%s)")
		self.cnx.cursor().execute(data, (user, msg, timestamp))
		self.cnx.commit()
		
		
if __name__ == "__main__":
	x = Database()
	print(x.query("SELECT * FROM message"))
	x.insert(user, msg)
	x.close()