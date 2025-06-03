import cv2
import serial
import numpy as np
from matplotlib import pyplot as plt
import time

cap = cv2.VideoCapture(1) 

secs = .1
    
counter = 0
    
while True:
    #Capture frame-by-frame
    ret, frame = cap.read()

    #Operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret, thresh_img = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)

    contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[-2]
    for c in contours:
       cv2.drawContours(frame, [c], -1, (255,0,0), 2) 
       
    cnt = contours[-1]

    #Draw the contour and center of the shape on the image
    for c in contours:
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print(M["m00"])
        cenD = [cX,cY]
        cenC = [340,230]
        cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)
        
        print(cenD)
        
        if cenD[0] not in range(cenC[0]-10, cenC[0]+11) or cenD[1] not in range(cenC[1]-10, cenC[1]+11):
            print('you need to center the camera')
            time.sleep(secs)
            if cenD[0] in range(cenC[0]-10, cenC[0]+11) and cenD[1] not in range(cenC[1]-10,cenC[1]+11):
                #need to move the camera right or left
                if cenD[1] > cenC[1]+11:
                    print('up on camera/right irl')
                    time.sleep(secs)
                elif cenD[1] < cenC[1]-10:
                    print('down on camera/left irl')
                    time.sleep(secs)
            elif cenD[1] in range(cenC[1]-10, cenC[1]+11) and cenD[0] not in range(cenC[0]-10, cenC[0]+11):
                #need to move the camera up or down
                if cenD[0] < cenC[0]-10:
                    print('right on vid/down irl')
                    time.sleep(secs)
                elif cenD[0] > cenC[0]+11:
                    print('left on video/up irl')
                    time.sleep(secs)
            elif cenD[0] > cenC[0]+11 and cenD[1] not in range(cenC[1]-10, cenC[1]+11):
                #needs to go up and right or left
                if cenD[1] > cenC[1]+11:
                    print('move left and up/up irl and right irl')
                    time.sleep(secs)
                elif cenD[1] < cenC[1]-10:
                    print('move left and down/up irl and left irl')
                    time.sleep(secs)
            elif cenD[0] < cenC[0]-10 and cenD[1] not in range(cenC[1]-10, cenC[1]+11):
                #needs to go down and right or left
                if cenD[1] > cenC[1]+11:
                    print('right and up/down irl and right irl')
                    time.sleep(secs)
                elif cenD[1] < cenC[1]-10:
                    print('right and down/down irl and left irl')
                    time.sleep(secs)
        
        else:
            print('its centered')
                                               
        # if cenD != cenC:
        #     if cenD[0] == cenC[0] and cenD[1] == cenC[1]:
        #         print('Center, do nothing')
        #     elif cenD[0] > cenC[0] and cenD[1] == cenC[1]:
        #         print('just left')
        #         #sendData('l')
        #     elif cenD[0] < cenC[0] and cenD[1] == cenC[1]:
        #         print('just right')
        #         #sendData('r')
        #     elif cenD[1] > cenC[1] and cenD[0] == cenC[0]:
        #         print('just up')
        #         #sendData('u')
        #     elif cenD[1] < cenC[1] and cenD[0] == cenC[0]:
        #         print('just down')
        #         #sendData('d')
        #     elif cenD[0] > cenC[0] and cenD[1] > cenC[1]:
        #         print('left and up')
        #         #sendData('a')
        #     elif cenD[0] > cenC[0] and cenD[1] < cenC[1]:
        #         print('left and down')
        #         #sendData('b')
        #     elif cenD[0] < cenC[0] and cenD[1] > cenC[1]:
        #         print('right and up')
        #         #sendData('e')
        #     elif cenD[0] < cenC[0] and cenD[1] < cenC[1]:
        #         print('right and down')
        #         #sendData('f')
        #     else:
        #         print('error') 



    #Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break  
          


