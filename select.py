import mysql.connector

db = mysql.connector.connect(
    host="asiyademoserver123.mysql.database.azure.com",
    user="myadmin@asiyademoserver123",
    password="AsiyaSayed@123",
    database="employee",
)

cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)
