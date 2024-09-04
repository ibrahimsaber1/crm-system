
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ibra157him'
    
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crmdb")

print("crmdb reated successfully :)")
