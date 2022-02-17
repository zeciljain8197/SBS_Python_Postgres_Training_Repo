import psycopg2

conn = psycopg2.connect(database='zinu_db', user='zinu', password='8197', host='localhost', port='5432')
cr = conn.cursor()
cr.execute("alter table product add constraint category_foreign_key FOREIGN KEY (id) references category (id);")
conn.commit()
cr.close()
conn.close()