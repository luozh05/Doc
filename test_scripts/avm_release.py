#!/usr/bin/env python
import socket
import sys
import json
import json_over_tcp

from json_over_tcp import send_and_receive_msg

if __name__ == '__main__':

    #test init device:right input, case 4
    cmd = {}
    cmd["cmd-release-device"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 4 failed!"
        exit()
    print "case 4 succeed!"
