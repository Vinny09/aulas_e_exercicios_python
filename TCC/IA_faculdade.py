import numpy as np
import cv2
import time
from datetime import datetime

# color=(255,0,0)
color = (0, 255, 0)
thickness = 2
kernel = np.ones((2, 2), np.uint8)  # added 01/07/2021
picflag = 0  # set value to 1 once picture is taken

# function to take still picture when water level goes beyond threshold
def takepicture(frame):
        currentTime = datetime.now()
        # Create file name for our picture
        picTime = currentTime.strftime("%d.%m.%Y-%H%M%S")
        text = currentTime.strftime("%d.%m.%Y-%H:%M:%S")
        font = cv2.FONT_HERSHEY_SIMPLEX  # font
        org = (5, 20)  # org
        fontScale = 0.5  # fontScale
        color = (0, 0, 255)  # Red color in BGR
        thickness = 1  # Line thickness of 2 px
        picName = picTime + '.png'
        image = cv2.putText(frame, text, org, font, fontScale,
                            color, thickness, cv2.LINE_AA, False)
        cv2.imwrite(picName, image)
        global picflag
        picflag = 1
        return 

cap = './aulas_e_exercicios_python/img/Bottle-Gray-1024x845.png'

while (True):
    frame = cv2.imread(cap)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(21,21),0)
    gray = cv2.medianBlur(gray, 3)  # to remove salt and paper noise

    ret,thresh = cv2.threshold(gray,10,20,cv2.THRESH_BINARY_INV)
    ret, thresh = cv2.threshold(gray, 127, 127, cv2.THRESH_BINARY_INV)
    # get outer boundaries only added 01/07/2021
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
    # strengthen weak pixels added 01/07/2021
    thresh = cv2.dilate(thresh, kernel, iterations=5)
    img1, contours = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    img1,contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #added 01/07/2021
    cv2.line(frame, pt1=(0, 375), pt2=(800, 375), color=(
        0, 0, 255), thickness=2)  # added 01/07/2021
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if contours is not None and len(contours) != 0:
        c = max(contours, key=cv2.contourArea)  # find the largest contour
        x,y,w,h = cv2.boundingRect(c)          # get bounding box of largest contour
        # draw largest contour
        img2 = cv2.drawContours(frame, c, -1, color, thickness)
        img2=cv2.drawContours(frame, contours, -1, color, thickness) # draw all contours
        img3 = cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),2)  # draw red bounding box in img
        center = (x, y)
        print(center)
        left = tuple(c[c[:, :, 0].argmin()][0])
        right = tuple(c[c[:, :, 0].argmax()][0])
        top = tuple(c[c[:, :, 1].argmin()][0])
        bottom = tuple(c[c[:, :, 1].argmax()][0])
        # Draw dots onto frame
        cv2.drawContours(frame, [c], -1, (36, 255, 12), 2)
        cv2.circle(frame, left, 8, (0, 50, 255), -1)
        cv2.circle(frame, right, 8, (0, 255, 255), -1)
        cv2.circle(frame, top, 8, (255, 50, 0), -1)
        cv2.circle(frame, bottom, 8, (255, 255, 0), -1)

        print('left: {}'.format(left))
        print('right: {}'.format(right))
        print(format(top))
        top_countour_point = top[1]
        print(top_countour_point)
        print('bottom: {}'.format(bottom))
        if ((top_countour_point <= 375) and (picflag == 0)):   #checking if contour top point is above line
            takepicture(frame)
            continue
        if ((top_countour_point > 375) and (picflag == 0)) :
            picflag = 0
            continue
        # Display the resulting image
        cv2.line(frame, pt1=(0,375), pt2=(800,375), color=(0,0,255), thickness=2) # added 01/07/2021
        cv2.imshow('Contour',img3)
        cv2.imshow('thresh' ,thresh)
        cv2.imshow('Contour', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break

    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
