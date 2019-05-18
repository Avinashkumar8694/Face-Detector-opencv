#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:40:11 2018

@author: avinash
"""

import numpy as np
import cv2,os
import sqlite3
import urllib.request

url='http://10.42.0.150:8055/shot.jpg'  //ip-cam ip address
def getProfile(id):
    conn=sqlite3.connect("facebase")
    cmd="SELECT * FROM people WHERE id="+str(id)
    c=conn.cursor()
    cursor=conn.execute(cmd)
    for row in cursor:
        profile=row
    conn.close()
    return profile


faceDetector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);
rec=cv2.face.createLBPHFaceRecognizer();
rec.load("recognizer/trainningData.yml")
id=0
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 0)

while(True):
    #ret, img = cap.read()
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img = cv2.flip(img,1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile!=None):
            cv2.putText(img, profile[1], (x,y+h+30), font, fontscale, fontcolor)
            cv2.putText(img, profile[2], (x,y+h+60), font, fontscale, fontcolor)
            
            
        
        

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
