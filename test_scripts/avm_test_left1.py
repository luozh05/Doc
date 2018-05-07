#!/usr/bin/env python
import socket
import sys
import json
import json_over_tcp

from json_over_tcp import send_and_receive_msg

if __name__ == '__main__':
    #test set cases:right input, case 0
    cmd = {}
    cmd["cmd-set-parameters"] = {}
    cmd["cmd-set-parameters"]["evt-version"] = "evt-version-2.0"
    cmd["cmd-set-parameters"]["camera-name"] = "remote-camera-avm-left"
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 0 failed!"
        exit()
    print "case 0 succeed!"

    #test set cases:right input, case 2
    cmd = {}
    cmd["cmd-set-parameters"]={}
    cmd["cmd-set-parameters"]["preview-format"]="preview-format-h264"
    cmd["cmd-set-parameters"]["preview-size"]="1280x800"
    cmd["cmd-set-parameters"]["preview-fps-values"]="20"
    cmd["cmd-set-parameters"]["receive-ip-address"]="172.20.1.1"
    cmd["cmd-set-parameters"]["receive-port"]=8554
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 2 failed!"
        exit()
    print "case 2 succeed!"

    #test init device:right input, case 4
    cmd = {}
    cmd["cmd-init-device"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 4 failed!"
        exit()
    print "case 4 succeed!"
