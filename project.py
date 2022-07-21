import numpy as np
import cv2

#change the file path from "devtown_Bootcamp_Project/Soldiers_Walking_Trim.mp4" to "Soldiers_Walking_Trim.mp4"
video = cv2.VideoCapture('devtown_Bootcamp_Project/Soldiers_Walking_Trim.mp4')
#chnage the path from 'devtown_Bootcamp_Project/gettyimages-1175506973-612x612.jpg' to 'gettyimages-1175506973-612x612.jpg'
image = cv2.imread('devtown_Bootcamp_Project/gettyimages-1175506973-612x612.jpg')

while True:
    ret, frame = video.read()
    if ret:
        frame = cv2.resize(frame, (640,480))
        image = cv2.resize(image, (640,480))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        l_g = np.array([32,94,132])
        u_g = np.array([150,255,255])
        mask = cv2.inRange(hsv, l_g, u_g)

        res = cv2.bitwise_and(frame,frame, mask=mask)
        f = frame-res
        green_screen = np.where(f==0, image,f)
        cv2.imshow("green_Screen", green_screen)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break
    else:
        # print("Something's wrong")
        break

video.release()
cv2.destroyAllWindows()
