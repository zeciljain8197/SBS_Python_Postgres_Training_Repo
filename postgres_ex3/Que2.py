import psycopg2

conn = psycopg2.connect(database='zinu_db', user='zinu', password='8197', host='localhost', port='5432')
print(conn)

cr = conn.cursor()
print(cr)
cr.close()
conn.close()
