import socket
from threading import Thread, RLock
ip_list = list()
lock = RLock()
def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 15653))
    s.listen()
    print('服务器已经启动----->')
    acct(s)
def acct(s):
    while 1:

        conn,dder = s.accept()
        print('有新的连接{}进来'.format(dder))
        ip_list.append(conn)
        header = Thread(target=sends, args=(conn,dder))
        header.start()

def sends(coon,dder):
    while 1:

        news = coon.recv(65535)
        return_news = '地址{}:{}'.format(dder, news.decode())

        print(return_news)
        for coon in ip_list:
            coon.send(return_news.encode())














if __name__ == '__main__':
    start()