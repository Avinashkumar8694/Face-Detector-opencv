import os
import cv2
import numpy as np
from PIL import Image
recognizer=cv2.face.createLBPHFaceRecognizer();
path = 'dataSet'

def getImgWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagesPath in imagePaths:
        faceImg=Image.open(imagesPath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagesPath)[-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow("trainer",faceNp)
        cv2.waitKey(10)
    return IDs, faces

IDs, faces=getImgWithID(path)
recognizer.train(faces,np.array(IDs))
recognizer.save('recognizer/trainningData.yml') 
cv2.destroyAllWindows()  