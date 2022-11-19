import tkinter as tk
import cv2
import os
from sys import platform
from ast import Continue
import sys
import tkinter.filedialog
from tkinter.filedialog import askopenfile

# path of the video file
vidpath = 'sample.mp4'
vidcap = cv2.VideoCapture('sample.mp4')

my_w = tk.Tk()
my_w.geometry("1280x720")  

# def pathdir():
    # get path to store frames
# framesPath = sys.argv[2] if sys.argv[2] else 'temp'
framesPath = 'temp'
if os.path.exists(framesPath):
    Continue
else:
    os.mkdir(framesPath)
if platform == "linux" or platform =="linux2":
    framesPath = framesPath + '/'
elif platform == "win32" or platform =="win64":
    framesPath = framesPath + '\\'
# return framesPath

def stream_vid():
    while(vidcap.isOpened()):
       # Capture frame-by-frame
        ret, frame = vidcap.read()
        if ret == True:
    
            # Display the resulting frame
            cv2.imshow('Frame',frame)
    
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    
        # Break the loop
        else: 
            break
    vidcap.release()
    cv2.destroyAllWindows()

def extract_frames():
    # framesPath = extract_frames()
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("{}frame%d.jpg".format(framesPath) %count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1
    print(f'{count} frames are exported')

def browseFiles():
    filename = tkinter.filedialog.askopenfilename(initialdir = "/",
                    title = "Select a File",
                    filetypes = (("Text files",
                    "*.txt*"),
                    ("all files",
                    "*.*")))

    # Change label contents
    # label_file_explorer.configure(text="File Opened: "+filename)

def upload_file():
    file = tk.filedialog.askopenfilename()
    # fob = open(file,'r')
    # print(fob.read())

# Create a File Explorer label
# label_file_explorer = tk.Label(my_w, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue")
button_explore = tk.Button(my_w, text = "Browse Files", command = lambda: browseFiles())
button_explore.grid(row=1, column=1)

b1 = tk.Button(my_w, text='Play Video', width=50,bg='green', command=lambda: stream_vid())
b1.grid(row=2,column=2) 

b2 = tk.Button(my_w, text='Close App', width=20, bg='red' ,command=my_w.destroy)
b2.grid(row=2,column=3) 

b3 = tk.Button(my_w, text='Extract Frames', width=20, bg='yellow', command=lambda: extract_frames())
b3.grid(row=3,column=2) 

my_w.mainloop()