import tkinter as tk
import cv2
import os
from sys import platform
from ast import Continue
from tkinter.filedialog import askopenfile

class App:
    def __init__(self, vidpath):
        self.vidpath = vidpath
        self.vidcap = cv2.VideoCapture(self.vidpath)
        self.framesPath = os.path.splitext(self.vidpath)[0]
        print(self.framesPath)
        if os.path.exists(self.framesPath):
            Continue
        else:
            os.mkdir(self.framesPath)
        if platform == "linux" or platform =="linux2":
            self.framesPath = self.framesPath + '/'
        elif platform == "win32" or platform =="win64":
            self.framesPath = self.framesPath + '\\'
        self.fps = self.vidcap.get(cv2.CAP_PROP_FPS)
        self.my_w = tk.Tk()
        self.my_w.title("Frames")
        self.my_w.geometry("370x345")
        self.frap = tk.StringVar()

    def stream_vid(self):
        while(self.vidcap.isOpened()):
        # Capture frame-by-frame
            ret, frame = self.vidcap.read()
            if ret == True:
        
                # Display the resulting frame
                cv2.imshow('Frame',frame)
        
                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
        
            # Break the loop
            else: 
                break
        cv2.destroyAllWindows()

    def extract_frames(self):
        time_skips = int(self.frap.get())
        print(f'Skipping {time_skips} frames')
        success,image = self.vidcap.read()
        count = 0
        jump = 0
        while success:
            cv2.imwrite("{}frame%d.jpg".format(self.framesPath) %count, image)     # save frame as JPEG file       
            success,image = self.vidcap.read()
            jump += time_skips
            self.vidcap.set(1, jump)
            count += 1
        print(f'{count} frames are exported')

    def structure(self):
        self.vidpath = tk.filedialog.askopenfilename(initialdir = "/home/Desktop/", title = "Select a File", filetypes = (("Video files", "*.mp4*"),("all files", "*.*")))

        button_explore = tk.Button(self.my_w, width=20, text = "Browse Files", bg='pink', command = self.vidpath, padx=10, pady=10)
        button_explore.grid(row=1, columnspan=2)

        b1 = tk.Button(self.my_w, text='Play Video', width=20,bg='green', command=lambda: App.stream_vid(self), padx=10, pady=10)
        b1.grid(row=2,columnspan=2) 

        labelFrap = tk.Label(self.my_w, text="Skip Frames", padx=10, pady=10).grid(row=4, column=0)
        entryFrap = tk.Entry(self.my_w, textvariable=self.frap, width=10).grid(row=4, column=1)
        tk.Label(self.my_w)

        b2a = tk.Label(self.my_w, text=f'FPS of video is: {self.fps}', width=20, padx=10, pady=10)
        b2a.grid(row=3, columnspan=2)

        b2 = tk.Button(self.my_w, text='Extract Frames', width=20, bg='yellow', command=lambda: App.extract_frames(self), padx=10, pady=10)
        b2.grid(row=5,columnspan=2) 
        b3 = tk.Button(self.my_w, text='Close App', width=20, bg='red' ,command=self.my_w.destroy, padx=10, pady=10)
        b3.grid(row=6,columnspan=2) 
        self.my_w.mainloop()

if __name__ == "__main__":
    obj = App('sample.mp4')
    obj.structure().mainloop()