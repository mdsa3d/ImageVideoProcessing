import cv2
import os
import datetime
from sys import platform
from ast import Continue

class vidProcess:
    def __init__(self, vidPath):
        self.vidPath = vidPath if vidPath else 'sample.mp4'
        self.framesPath = 'Frames'
        if os.path.exists(self.framesPath):
            Continue
        else:
            os.mkdir(self.framesPath)     

    def extractFrames(self):
        # path of the video file
        vidcap = cv2.VideoCapture(self.vidpath)
        success,image = vidcap.read()
        stamp = str(datetime.datetime.now())
        if platform == "linux" or platform =="linux2":
            self.framesPath = self.framesPath + '/' + stamp + '/'
        elif platform == "win32" or platform =="win64":
            self.framesPath = self.framesPath + '\\' + stamp + '\\'
        count = 0
        while success:
            cv2.imwrite("{}frame%d.jpg".format(self.framesPath) %count, image)     # save frame as JPEG file      
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1