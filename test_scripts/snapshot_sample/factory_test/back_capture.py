#!/usr/bin/env python
import socket
import sys
import json
import Image
import struct
import time

HOST="172.20.1.11"
PORT=37568 

def take_a_pic(msg):
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect host:port
    sock.connect((HOST, PORT))

    # Connect to server and send data
    sock.send(msg)

    # Receive data from the server and shut down
    buf = ''
    while len(buf)<16:
            buf += sock.recv(16-len(buf))
    print len(buf)
    size = struct.unpack('iiii', buf)
    print repr(size)

    file_name = "back"
    name = "./Picture/" + file_name + time.strftime('-%Y%m%d(%H:%M:%S)') + ".jpg"
    print "name=",name
    with open(name, 'wb') as img:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            img.write(data)
    print 'received back img!'
    sock.close()

    image = Image.open(name)
    image.show()

if __name__ == "__main__":
    cmd = {}
    cmd["cmd-take-picture"] = "picture-size=1280x800;preview-format=preview-format-h264"
    cmd_string = json.dumps(cmd)
    take_a_pic(cmd_string)
    print "case 0 succeed!"

