import socket
from threading import Thread

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(('127.0.0.1', 15653))

def cli_send(ss):
    while 1:
        news = input('请输入')
        try:
            ss.send(news.encode())
        except Exception:
            break
        print('发送结束')
def cli_recv(ss):
    while 1:
        return_news = ss.recv(65535)
        if not return_news:
            break
        print(return_news.decode())
        print('    ')
        print('接收完毕....')
t1 = Thread(target=cli_recv, args=(ss,))
t2 = Thread(target=cli_send, args=(ss,))

t1.start()
t2.start()
t1.join()
t2.join()
print('聊天客户端结束')