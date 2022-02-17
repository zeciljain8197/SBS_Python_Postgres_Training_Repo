import psycopg2
conn = psycopg2.connect(database='zinu_db', user='zinu', password='8197', host='localhost', port='5432')
cr = conn.cursor()
cr.execute("update product set cost_price = 10 where id > 17;")
# res = cr.fetchall()
# print(res)
conn.commit()
cr.close()
conn.close()