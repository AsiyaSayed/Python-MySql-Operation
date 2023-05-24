import mysql.connector

db = mysql.connector.connect(
    host="asiyademoserver123.mysql.database.azure.com",
    user="myadmin@asiyademoserver123",
    password="AsiyaSayed@123",
    database="employee",
)

cursor = db.cursor()
sql = "DELETE FROM customers WHERE customer_id=%s"
val = (4, )
cursor.execute(sql, val)

db.commit()

print("{} data deleted".format(cursor.rowcount))
