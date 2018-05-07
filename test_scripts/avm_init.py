#!/usr/bin/env python
import socket
import sys
import json
import json_over_tcp

from json_over_tcp import send_and_receive_msg

if __name__ == '__main__':
    #test set parameters:right input, case 0
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

    #test init device:right input, case 1
    cmd = {}
    cmd["cmd-init-device"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 1 failed!"
        exit()
    print "case 1 succeed!"
