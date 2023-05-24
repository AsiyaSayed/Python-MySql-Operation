import mysql.connector

db = mysql.connector.connect(
    host="asiyademoserver123.mysql.database.azure.com",
    user="myadmin@asiyademoserver123",
    password="AsiyaSayed@123",
    database="employee",
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
  ("Shakib", "Magura"),
  ("Tamin", "Ctg"),
  ("Taskin", "Dhaka"),
  ("Mushfiq", "Rajshahi")
]

for val in values:
  cursor.execute(sql, val)

db.commit()

print("{} data added".format(cursor.rowcount))
