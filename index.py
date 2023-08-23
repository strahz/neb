import pyodbc
import pandas as pd

db_driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
db_path = r"C:\Users\.accdb"
conn_str = (rf'DRIVER={db_driver};'
            rf'DBQ={db_path};')

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

df = pd.read_sql(sql="select * from Documents", con=conn)

cursor.execute("CREATE TABLE QA (name VARCHAR(255), address VARCHAR(255))")
cursor.commit()
for i in cursor.tables(tableType='TABLE'):
    print(i.table_name)

for i in cursor.tables(tableType='VIEW'):
    print(i.table_name)

conn.close()
