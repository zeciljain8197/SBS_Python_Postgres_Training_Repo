import psycopg2

conn = psycopg2.connect(database='zinu_db', user='zinu', password='8197', host='localhost', port='5432')
cr = conn.cursor()
cr.execute("select * from product;")
res = cr.fetchall()
print(res)
conn.commit()
cr.close()
conn.close()