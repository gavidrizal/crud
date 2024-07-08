import mysql.connector

def lihat():
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kantor_kampus"
    )

    mycursor = mysb.cursor(buffered=True)

    sql = "SELECT * FROM staf_kantor"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    mycursor.close()
    mysb.close()

    # print(myresult)
    
    for value in myresult:
        print(value)