# -*- coding: utf-8 -*-
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       #with:当代码离开with块时，自动调用s.close来销毁这个socket
       #socket.socket()调用模块(工具箱)中定义的类，命名为s，后面的s.connect()、s.sendall()、s.recv()都是这个类的方法
       #socket.AF_INET:使用IPv4地址，socket.SOCK_STREAM:使用TCP协议
    s.bind(("0.0.0.0", 1234))
    #将socket绑定到一个地址和端口上，
    s.listen()
    #监听连接请求，等待客户端连接
    c,addr = s.accept()
    #接受连接请求，返回一个新的socket对象c和客户端的地址信息addr
    #socket s用于监听，而socket c用于与客户端通信
    with c:
        print(addr, "connected.")
        #打印客户端的地址信息
        while True:
            data = c.recv(1024)
            #循环接收客户端发送的数据，1024是一次接收的最大字节数
            if not data:
                break
            c.sendall(data)
            #如果数据不为空，将接收到的数据原封不动地发送回客户端