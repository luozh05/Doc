#!/usr/bin/env python
import socket
import sys
import json
import data_over_tcp

from data_over_tcp import take_a_pic

def capture(x):
    cmd = {}
    cmd["cmd-take-picture"] = "picture-size=1280x800;preview-format=preview-format-h264"
    cmd_string = json.dumps(cmd)
    take_a_pic(cmd_string)
    print "case 0 succeed!"

if __name__ == "__main__":
    capture()
else:
    pass

