print("mi conexion ....")
import sqlite3 
#coneccion a la BBDD . 
conn= sqlite3.connect('contabilidad.sqlito3')
cursor=conn.cursor() # ejecuta codigo sql
def crear_tabla():
    cursor.execute("CREATE table cliente (nombre text, edad numeric)") # creo mi tabla 
clientes=(("gio",25),("rhony",18),("brandon",15))

for  nombre, edad in clientes:
    conn.execute("INSERT INTO cliente VALUES (?,?)", (nombre, edad))
conn.commit() #graba o ejecuta todo lo q fue ejecutando en la BBDD.

try:
    cursor.execute("SELECT * FROM cliente")
    micliente= cursor.fetchall() # todo los datos lo toma y se guarda
    print(micliente)
except sqlite3.OperationalError :
    print("mal de consulta")
conn.close() 


