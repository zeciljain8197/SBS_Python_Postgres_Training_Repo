import psycopg2
conn = psycopg2.connect(database='zinu_db', user='zinu', password='8197', host='localhost', port='5432')
cr = conn.cursor()
cr.execute("select p.id, p.name, p.sale_price, p.cost_price, c.code, c.name from product p INNER JOIN category c ON p.id=c.id")
res = cr.fetchall()
print(res)
conn.commit()
cr.close()
conn.close()