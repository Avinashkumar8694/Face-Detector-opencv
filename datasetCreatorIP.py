import cv2
import sqlite3
import urllib.request
import numpy as np

#cam = cv2.VideoCapture(0)

url='http://10.42.0.150:8055/shot.jpg'

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def inorup(id,Name):
    conn=sqlite3.connect('facebase')
    c=conn.cursor()
    cmd="SELECT * FROM people WHERE ID="+str(id)
    c=conn.execute(cmd)
    isRecordExist=0
    for row in c:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE people SET name="+str(Name)+" Where ID="+str(id)
    else:
        cmd="INSERT INTO people (id,name) VALUES("+str(Id)+","+str(Name)+")"
    conn.execute(cmd)    
    conn.commit()
    conn.close()
    
    
    
Id=input('enter your id')
name=input('name')
inorup(Id,name)
sampleNum=0
while(True):
    #ret, img = cam.read()
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img = cv2.flip(img,1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".png", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>100:
        break
#cam.release()
cv2.destroyAllWindows()
