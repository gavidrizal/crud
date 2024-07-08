import mysql.connector

mysb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="unidayan"
)

mycursor = mysb.cursor(buffered=True)

sql = "INSERT INTO matakuliah (id, nama, kode) VALUES (%s, %s, %s)"
values = ("1111", "sinta", "5555")
mycursor.execute(sql, values)

#myresult = mycursor.fetchall()

mycursor.close()
mysb.close()

#print(myresult)