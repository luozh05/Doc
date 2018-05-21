#!/usr/bin/python 
#coding=utf-8
import sys
import json
import start_camera
from data_over_tcp import take_a_pic
from json_over_tcp import send_and_receive_msg

def open_camera(x):
    cmd = {}
    if x == '1':
        cmd["cmd-set-parameters"] = "evt-version=evt-version-2.0;camera-name=remote-camera-avm-front"
    if x == '2':
        cmd["cmd-set-parameters"] = "evt-version=evt-version-2.0;camera-name=remote-camera-avm-back"
    if x == '3':
        cmd["cmd-set-parameters"] = "evt-version=evt-version-2.0;camera-name=remote-camera-avm-left"
    if x == '4':
        cmd["cmd-set-parameters"] = "evt-version=evt-version-2.0;camera-name=remote-camera-avm-right"
    if x == '5':
        cmd["cmd-set-parameters"] = "evt-version=evt-version-2.0;camera-name=remote-camera-driver-monitor"
    if x == '6':
        cmd["cmd-set-parameters"] = "evt-version=evt-version-2.0;camera-name=remote-camera-avm-synthesis"

    print"cmd = ",cmd
    cmd_string = json.dumps(cmd)
    result = send_and_receive_msg(cmd_string)
    if result == False:
        print "case 0 failed!"
        exit()
    print "case 0 succeed!"
    
    start_camera.start()

def snapshot():
    file_name=raw_input("自定义文件名:")
    cmd = {}
    cmd["cmd-take-picture"] = "picture-size=1280x800;preview-format=preview-format-h264"
    cmd_string = json.dumps(cmd)

    take_a_pic(cmd_string,file_name)

def menu():
    print "需要拍照的摄像头:"
    print "front:   1"
    print "back:    2"
    print "left:    3"
    print "right:   4"
    print "monitor: 5"
    print "avm:     6"
    print "capture: c"
    print "exit:    q"

while True:
    str=['1','2','3','4','5','6','c','q']
    menu()
    x=raw_input("\n选择:")
    if x == 'c':
       snapshot()
    elif x == 'q':
        sys.exit()
    elif x not in str:
       print "\nERROR\n"
    else:
       open_camera(x)

