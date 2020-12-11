import pymyqsl
conn = pymysql.connect(
    host="localhost",
    user="root",
    passwod="",
    db="PythonDB"
)

cursor=conn.cursor()
cursor.execute("CREATE DATABASE PythonDB")

