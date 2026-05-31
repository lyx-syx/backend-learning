# -*- coding: utf-8 -*-
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 6000))
    s.listen()
    print("Listening on 127.0.0.1:6000")
    c, addr = s.accept()
    with c:
        print(addr, "connected")
        while True:
            data = c.recv(1024)
            if not data:
                break
            c.sendall(data)