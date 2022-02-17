import psycopg2

conn = psycopg2.connect(database='zinu_db', user='zinu', password='8197', host='localhost', port='5432')

cr = conn.cursor()
cr.execute("create table product (id serial PRIMARY KEY, name varchar(64) NULL,cost_price float, sale_price float, CHECK(cost_price < sale_price));")
conn.commit()
cr.close()
conn.close()