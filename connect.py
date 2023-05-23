import mysql.connector

db = mysql.connector.connect(
    host="asiyademoserver123.mysql.database.azure.com",
    user="myadmin@asiyademoserver123",
    password="AsiyaSayed@123"
)

if db.is_connected():
    print("Database Connected")
    
    
    
