from time import process_time_ns

import cv2
import time
import numpy as np
from torchvision.transforms.v2.functional import horizontal_flip

import handtrackingmodule as htm
import pyautogui

# Set the width and height of the webcam feed
wCam, hCam = 640, 480
frameR = 100
smooth = 5
plocx,plocy =0,0
cx,xy =0,0

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 320)  # Width
cap.set(4, 240)  # Height
cap.set(cv2.CAP_PROP_FPS, 30)  # Attempt to set FPS to 30
pTime = 0
detector = htm.handDetector(maxHands=1, detectionCon=0.5, trackCon=0.5)
wscreen,hscreen = pyautogui.size()
print(wscreen, hscreen)
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)


    if len(lmList) !=0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]

        #print(x1, y1,x2,y2)

        fingers = detector.fingersUp()
        print(fingers)

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 3)


        if fingers[1]==1 and  fingers[2] == 0:



            x3 = np.interp(x1,(frameR,wCam - frameR),(0,wscreen))
            y3 = np.interp(y1,(frameR,hCam- frameR),(0,hscreen))


            cx = plocx +(x3 - plocx)/smooth
            cy = plocy +(y3 - plocy)/smooth

            pyautogui.moveTo(   cx,cy)
            cv2.circle(img,(x1,y1),10,(255,255,0),cv2.FILLED)
            plocx,plocy = cx,cy

        if fingers[1] == 1 and fingers[2] == 1:
                length,img,line =  detector.findDistance(8,12,img)
                print(length)
                if length < 50 :
                     cv2.circle(img, (line[4], line[5]), 10, (0, 255, 255), cv2.FILLED)
                     pyautogui.click()



    if not success:
        break


    #frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,70),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,255),3)


    cv2.imshow("Image", img)

    # Wait for 1 millisecond and check if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
