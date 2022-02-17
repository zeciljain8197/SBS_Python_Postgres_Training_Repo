import psycopg2

conn = psycopg2.connect(database='zinu_db', user='zinu', password='8197', host='localhost', port='5432')
cr = conn.cursor()
cr.execute("create table category (id int PRIMARY KEY, code int UNIQUE, name varchar(64) NOT NULL);")
conn.commit()
cr.close()
conn.close()