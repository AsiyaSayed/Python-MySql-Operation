import mysql.connector

db = mysql.connector.connect(
    host="asiyademoserver123.mysql.database.azure.com",
    user="myadmin@asiyademoserver123",
    password="AsiyaSayed@123"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE employee_data")

print("Database Created Successful !!!")
