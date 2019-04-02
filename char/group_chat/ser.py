import socket
from threading import Thread

a = []

def conn_recv(conn, conn_addr, a):
    while 1:
        try:
            msg = conn.recv(65535)
            if not msg:
                break

            msg = msg.decode()
            return_msg = '收到{}的消息:{}'.format(conn_addr, msg)
            print(return_msg)

            # return_msg = "已经收到你的消息--->" + msg
            # sg = return_msg.encode()

            # a.append(return_msg)

            conn.send(return_msg.encode())
            print(type(a))
        except Exception:
            break

    conn.close()
    print('{}的链接已经断开'.format(conn_addr))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('127.0.0.1', 41902)
server.bind(server_addr)
print('服务器已经开启')

server.listen(10)

while 1:
    try:

        conn, conn_addr = server.accept()

    except Exception:
        break



    t = Thread(target=conn_recv,args=(conn,conn_addr, a == None))
    t.start()


server.close()
print('服务器已经结束')