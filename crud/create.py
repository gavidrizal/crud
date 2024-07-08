import mysql.connector

def create_record(id, nama, agama):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kantor_kampus"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO staf_kantor (id, nama, agama) VALUES (%s, %s, %s)"
    val = (id, nama, agama)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()
