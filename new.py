# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
from imutils import resize
import time
import cv2
from collections import deque

vs = cv2.VideoCapture("~/PycharmProjects/track-object-movement/MVI_4294doneOutOfFLedsvisible_01.mp4")

ap=argparse.ArgumentParser()
ap.add_argument("-v", "--video")
ap.add_argument("-b", "--buffer", type=int, default=32, help="max buffer size")
args=vars(ap.parse_args())

greenL=(123,50,76)
pinkU=(355,57,70)

pts=deque(maxlen=args["buffer"])
counter=0
(dX, dY)=(0,0)
direction=""

while True:
    frame=vs.read()
    frame=frame[1] if args.get("video", False) else frame
    if frame is None:
        break

    frame=imutils.resize(frame, width=600)
    blurred=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    hsv=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)


    mask=cv2.inRange(hsv,greenL, pinkU)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask, None, iterations=2)

    cnts=cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab(contours(ctnts))

if len(cnts)>0:
    c=max(cnts, key=cv2.contourArea)
    ((x,y), radius)=cv2.minEnclosingCircle(c)
    M=cv2.moments(c)
    center=(int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))

    if radius>10:
        cv2.circle(frame(int(x), int(y), int(radius), 0,255,255),2)
        cv2.circle(frame, center, 5,(0,0,255),-1)
        pts.appendleft(center)

for i in np.arange(1, len(pts)):
    if pts[i-1] is None or pts[i] is None:
        continue

    if counter>=10 and i==1 and pts[-10] is not None:
        dX=pts[-10][0]-pts[i][0]
        dY=pts[-10][1]-pts[i][1]
        (dirX, dirY)=("","")

    if np.abs(dX)>20:
        dirY="East" if np.sign(dX)==1 else "West"

    if np.abs(dY)>20:
        dirY="North" if np.sign(dY)==1 else "South"

    if dirX !="" and dirY !="":
        direction="{}-{}".format(dirX, dirY)

    else:
        direction=dirX if dirX !="" else dirY
        thickness=int(np.sqrt(args["buffer"]/float(i+1))*2.5)
        cv2.line(frame,pts[i-1], pts[i],(0,0,255), thickness)

cv2.putText()

