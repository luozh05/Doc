#!/usr/bin/env python
import socket
import sys
import json
import json_over_tcp

from json_over_tcp import send_and_receive_msg

if __name__ == '__main__':
    cmd = {}
    cmd["cmd-control"] = "camera-name=remote-camera-avm-synthesis;view_horizontal_rotation=no;view_height_rotation=no;view_distance_rotation=no" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 0 failed!"
        exit()
    print "case 0 succeed!"
