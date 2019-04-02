import os
import socket

dir_name = os.path.dirname(__file__)

png_name = os.path.join(dir_name, 'vim.png')
png_name1 = os.path.join(dir_name, 'vim1.png')


with open(png_name, 'rb') as f:
    b_file = f.read()

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('127.0.0.1', 11111)

ss.connect(addr)

ss.send(b_file)

ss.close()

with open(png_name1,'wb') as f:
    f.write(b_file)