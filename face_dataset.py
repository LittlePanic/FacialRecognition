import cv2
import os
from face_training import *

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class Dataset():
    def data_set(self):
        # For each person, enter one numeric face id
        list = []
        x = 0
        name = input("please input data name:")
        file = open("data.txt")
        while 1:
            x = x + 1
            line = file.readline()
            if not line:
                break
            list.append(line)  # do something
        file.close()
        list.append(name)
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(str(list[int(x - 1)]) + '\n')
            print('input success')
            f.close()
        face_id = x
        print("\n [INFO] Initializing face capture. Look the camera and wait ...")
        # Initialize individual sampling face count
        count = 0

        while(True):

            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

                cv2.imshow('image', img)

            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 30: # Take 30 face sample and stop video
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()

if __name__=="__main()":
    dataset = Dataset()
    dataset.data_set()
    train = Training()
    train.training()
    print("OK!!!")





