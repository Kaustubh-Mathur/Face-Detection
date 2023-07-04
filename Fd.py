import os
import time
import uuid
import tensorflow as tf
import json
import numpy as np
from matplotlib import pyplot as plt
import os
import cv2

""""
images_path=os.path.join("Data",'images')
number_img=30

cap = cv2.VideoCapture(0)
for imgnum in range(number_img):
    print('Collecting image {}'.format(imgnum))
    ret, frame = cap.read()
    imgname = os.path.join(images_path,f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

"""


for folder in ['test','train','val']:
    for file in os.listdir(os.path.join('Data', 'images')):
        filename = file.split('.')[0]+'.json'
        existing_filepath = os.path.join('Data','labels')
        if os.path.exists(existing_filepath): 
            new_filepath = os.path.join('Data','labels')
            os.replace(existing_filepath, new_filepath)
            

