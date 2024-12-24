import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Hyderabad@09'
)

cursorObject = dataBase.cursor()

cursorObject.execute("Create Database registercrmco")

print("Database Created")