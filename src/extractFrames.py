import cv2
import os
import sys
from sys import platform
from ast import Continue

# path of the video file
vidpath = sys.argv[1] if sys.argv[1] else 'sample.mp4'
vidcap = cv2.VideoCapture('sample.mp4')
success,image = vidcap.read()

# get path to store frames
framesPath = sys.argv[2] if sys.argv[2] else 'temp'
if os.path.exists(framesPath):
    Continue
else:
    os.mkdir(framesPath)
if platform == "linux" or platform =="linux2":
    framesPath = framesPath + '/'
elif platform == "win32" or platform =="win64":
    framesPath = framesPath + '\\'
count = 0
while success:
  cv2.imwrite("{}frame%d.jpg".format(framesPath) %count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1