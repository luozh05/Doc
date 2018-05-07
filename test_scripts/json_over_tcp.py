#!/usr/bin/env python
import socket
import sys
import json

#HOST="localhost"
HOST="172.20.1.11"
PORT=37568 

def send_and_receive_msg(msg):
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect host:port
    sock.connect((HOST, PORT))

    # Connect to server and send data
    sock.send(msg)

    # Receive data from the server and shut down
    recv_message = []
    time = 100
    while time > 0:
        time = time - 1
        d = sock.recv(1024)
        if d:
            recv_message.append(d)
        else:
            break

    sock.close()

    print "\n"
    print "Sent:     {}".format(msg)
    print "Received: {}".format(recv_message)
    
    json_recv = json.loads(recv_message[0])
    for key, value in json_recv.items():
        if cmp(json_recv[key], "succeed") == 0 :
            return True
        elif cmp(json_recv[key], "failed") == 0:
            return False



if __name__ == '__main__':
    #test get cases:right input, case 0
    cmd = {}
    cmd["cmd-set-parameters"] = {}
    cmd["cmd-set-parameters"]["evt-version"] = "evt-version-2.0"
    cmd["cmd-set-parameters"]["camera-name"] = "remote-camera-avm-synthesis"
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 0 failed!"
        exit()
    print "case 0 succeed!"
    
    #test get cases:right input, case 1
    cmd = {}
    cmd["cmd-get-parameters"] = {}
    cmd["cmd-get-parameters"]["camera-name"]="remote-camera-avm-synthesis"
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 1 failed!"
        exit()
    print "case 1 succeed!"
 
    #test get cases:right input, case 2
    cmd = {}
    cmd["cmd-set-parameters"]={}
    cmd["cmd-set-parameters"]["preview-format"]="preview-format-h264"
    cmd["cmd-set-parameters"]["preview-size"]="1280x800"
    cmd["cmd-set-parameters"]["preview-fps-values"]="30"
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 2 failed!"
        exit()
    print "case 2 succeed!"
