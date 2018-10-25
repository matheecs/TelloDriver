#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import time

server_address = '0.0.0.0'
server_port = 11111

addr = 'udp://' + server_address + ':' + str(server_port)
cap = cv2.VideoCapture(addr)

print(cap.isOpened())

while(cap.isOpened()):
    for i in range(0,10):
        ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Flame", frame)
        cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()