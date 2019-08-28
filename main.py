import pymysql

dbname = "db"
table_name = "table"
conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="password",
            db=dbname)
cursor = conn.cursor()
data = cursor.execute("SELECT * FROM "+table_name)
print(cursor.fetchone())

# cursor.execute("Insert Into "+table_name + "(content) values (%s)", "content~")
# new_id = cursor.lastrowid

conn.commit()
cursor.close()
conn.close()
