#!/usr/bin/env python
import socket
import sys
import json
import json_over_tcp

from json_over_tcp import send_and_receive_msg

if __name__ == '__main__':
    cmd = {}
    cmd["cmd-control"] = "camera-name=remote-camera-avm-synthesis;scale=1.5;xshift=0;yshift=0;zrot=178;viewh=800;viewd=1000;HFOV=90;targetx=0;birdeyeV=1.0;SteeringAngle=0;TrajCtrl=1;CarCtrl=1;birdeyeV=1.0" 
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 0 failed!"
        exit()
    print "case 0 succeed!"
