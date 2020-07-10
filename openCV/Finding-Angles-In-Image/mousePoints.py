import cv2
import math


path = 'angle.png'
img = cv2.imread(path)
pointsList = []


def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pointsList.append([x,y])
        print(pointsList)


while True:

    cv2.setMouseCallback("Image", mousePoints)
    cv2.imshow('Image',img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)

