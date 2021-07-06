import cv2 as cv 
import numpy as np 

# set the number of indexes
circles = np.zeros((4,2), np.int)
counter = 0

# mouse event 
def mousePoints(event, x,y,flags,params):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,y)
        # adding into the list the values of x and y
        circles[counter] = x, y
        # iteration until circles limite
        counter = counter + 1 

# load image
img = cv.imread('cards.jpeg')
# resize image
img = cv.resize(img,(600,600))


while True: 

    if counter == 4:

        width, height = 250,350
        # points took from the list circles 
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        # image measurements 
        pts2 = np.float32([[0,0], [width,0], [0,height],[width,height]])
        matrix = cv.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv.warpPerspective(img,matrix,(width, height))
        # output
        cv.imshow("Output Image", imgOutput)

    # adding the circles in the original image
    for x in range(0,4):
        cv.circle(img,(circles[x][0],circles[x][1]),3,(255,0,0),cv.FILLED)

    cv.imshow("Original Image", img)
    cv.setMouseCallback("Original Image", mousePoints)

    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()