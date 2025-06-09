import cv2
import serial
import time

serial_arduino = None

secs = .25 # adjust the delay between camera adjustments

cap = cv2.VideoCapture(1)

# establish connection with your arduino board
def estConn():
    serial_arduino = serial.Serial('COM3', 9600, timeout=2)
    time.sleep(3)
    serial_arduino.write('i'.encode())
    serial_arduino.readline().decode('utf-8')
    tmp = serial_arduino.readline().decode('utf-8')
    if tmp == 'hello\r\n': # if arduino send "hello" back the connection is successful
        print('Arduino is all set')
    return serial_arduino 
  
serial_arduino = estConn()

def sendData(byte):   
    serial_arduino.write(byte.encode())
    y = serial_arduino.readline().decode('utf-8')
    print(y)             
        
def main_loop():
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret, thresh_img = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
    
    contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in contours:
        #cv2.drawContours(frame, [c], -1, (255,0,0), 2)
        cnt = contours[-1]
        M = cv2.moments(cnt)
        cX = int(M['m10']/M['m00'])
        cY = int(M['m01']/M['m00'])
        if M["m00"] > 500:
            cenD = [cX,cY]
            cenC = [340,230]
            cv2.rectangle(frame, cX, cY, (255, 0, 0), 2)
            cv2.circle(frame, (cX,cY), 5, (255,0,0), 2)
            
            print(cenD) # for testing purposes
        
            if cenD[0] not in range(cenC[0]-10, cenC[0]+11) or cenD[1] not in range(cenC[1]-10, cenC[1]+11):
                print('you need to center the camera')
                time.sleep(secs)
                if cenD[0] in range(cenC[0]-10, cenC[0]+11) and cenD[1] not in range(cenC[1]-10,cenC[1]+11):
                    #need to move the camera right or left
                    if cenD[1] > cenC[1]+11:
                        print('up on camera/right irl')
                        sendData('r')
                        time.sleep(secs)
                    elif cenD[1] < cenC[1]-10:
                        print('down on camera/left irl')
                        sendData('l')
                        time.sleep(secs)
                elif cenD[1] in range(cenC[1]-10, cenC[1]+11) and cenD[0] not in range(cenC[0]-10, cenC[0]+11):
                    #need to move the camera up or down
                    if cenD[0] < cenC[0]-10:
                        print('right on vid/down irl')
                        sendData('d')
                        time.sleep(secs)
                    elif cenD[0] > cenC[0]+11:
                        print('left on video/up irl')
                        sendData('u')
                        time.sleep(secs)
                elif cenD[0] > cenC[0]+11 and cenD[1] not in range(cenC[1]-10, cenC[1]+11):
                    #needs to go up and right or left
                    if cenD[1] > cenC[1]+11:
                        print('move left and up/up irl and right irl')
                        sendData('a')
                        time.sleep(secs)
                    elif cenD[1] < cenC[1]-10:
                        print('move left and down/up irl and left irl')
                        sendData('b')
                        time.sleep(secs)
                elif cenD[0] < cenC[0]-10 and cenD[1] not in range(cenC[1]-10, cenC[1]+11):
                    #needs to go down and right or left
                    if cenD[1] > cenC[1]+11:
                        print('right and up/down irl and right irl')
                        sendData('e')
                        time.sleep(secs)
                    elif cenD[1] < cenC[1]-10:
                        print('right and down/down irl and left irl')
                        sendData('f')
                        time.sleep(secs)
            
            else:
                print('its centered')
                time.sleep(secs)
        else:
            print('Contour bigger than 10000 not found')  
            time.sleep(1)       
            
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()     
        serial_arduino.close()  

if __name__ == "__main__":
    main_loop()
