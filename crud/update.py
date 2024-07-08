import mysql.connector

def update_record(id,  nama, agama ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kantor_kampus"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE staf_kantor SET id = %s, nama = %s, agama = %s WHERE id = %s"
        val = (id, nama, agama, id)
        print("Executing SQL:", sql % val)  # Debug statement
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()

# Example usage
