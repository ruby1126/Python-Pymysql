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
print(data)
cursor.close()
conn.close()
