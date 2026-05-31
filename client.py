# -*- coding: utf-8 -*-
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 6000))
    #连接服务器，参数是服务器的地址和端口号 
    s.sendall(b"Hello, world")
    #调用sendall方法发送数据给服务器，参数加上b表示这是一个字节序列，因为sendall方法要求参数必须是字节序列  
    data = s.recv(1024)
    print("Received", repr(data))
