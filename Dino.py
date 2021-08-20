import cv2
import pyautogui
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
on=False

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        if(totalFingers==0):
            if(on==False):
                on=True
                pyautogui.press('down')
                
        elif(totalFingers==5):
            if(on==True):
                on=False
                pyautogui.press('up')
                
            
    img = cv2.flip(img,1)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if(key==27):
        break
        
cap.release()
cv2.destroyAllWindows()
