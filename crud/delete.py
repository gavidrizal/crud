import mysql.connector

def delete_record(id):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kantor_kampus"
    )

    mycursor = mysb.cursor()

    sql = "DELETE FROM staf_kantor WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record(s) deleted")

    mycursor.close()
    mysb.close()
