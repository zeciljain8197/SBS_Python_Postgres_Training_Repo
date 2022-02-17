import socket

host = socket.gethostname()
port = 9999
s = socket.socket()
s.bind((host, port))

s.listen(2)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


while True:
    conn, addr = s.accept()
    print("Connected by ", addr)
    data = conn.recv(1024)
    print(conn)
    if data:
        print("Data Received", data)
        dt1 = data.decode('utf-8')
        print("DT", dt1)
        d1 = dt1.split(",")
        print("Data Received string", d1)
        data_add = add(int(d1[0]), int(d1[1]))
        data_mul = mul(int(d1[0]), int(d1[1]))
        data_sub = sub(int(d1[0]), int(d1[1]))
        data_div = div(int(d1[0]), int(d1[1]))

        conn.send(str(data_add).encode('utf-8'))
        conn.send(str(data_mul).encode('utf-8'))
        conn.send(str(data_sub).encode('utf-8'))
        conn.send(str(data_div).encode('utf-8'))

s.close()