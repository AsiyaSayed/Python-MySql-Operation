import mysql.connector

db = mysql.connector.connect(
    host="asiyademoserver123.mysql.database.azure.com",
    user="myadmin@asiyademoserver123",
    password="AsiyaSayed@123",
    database="employee",
)

cursor = db.cursor()
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
val = ("ShakibAL", "Dhaka", 2)
cursor.execute(sql, val)

db.commit()

print("{} data changed".format(cursor.rowcount))
