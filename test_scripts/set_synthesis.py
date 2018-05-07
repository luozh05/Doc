#!/usr/bin/env python
import socket
import sys
import json
import json_over_tcp

from json_over_tcp import send_and_receive_msg

HOST="localhost"
PORT=8888 

if __name__ == '__main__':
    #test set cases:right input, case 0
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
 
    #test set cases:right input, case 2
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

    #test check device:right input, case 3
    cmd = {}
    cmd["cmd-check-device"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 3 failed!"
        exit()
    print "case 3 succeed!"

    #test init device:right input, case 4
    cmd = {}
    cmd["cmd-init-device"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 4 failed!"
        exit()
    print "case 4 succeed!"

    #test release device:right input, case 5
    cmd = {}
    cmd["cmd-release-device"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 5 failed!"
        exit()
    print "case 5 succeed!"

    #test start device:right input, case 6
    cmd = {}
    cmd["cmd-start-stream"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 6 failed!"
        exit()
    print "case 6 succeed!"

    #test stop device:right input, case 7
    cmd = {}
    cmd["cmd-stop-stream"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 7 failed!"
        exit()
    print "case 7 succeed!"

    #test control device:right input, case 8
    cmd = {}
    cmd["cmd-control"] = "" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 8 failed!"
        exit()
    print "case 8 succeed!"
