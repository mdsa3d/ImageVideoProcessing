import streamlit as st
import cv2 as cv
from PIL import Image
import shutil
import pathlib
import os
from ast import Continue

# STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
# DOWNLOADS_PATH = (STREAMLIT_STATIC_PATH / "downloads")
# if not DOWNLOADS_PATH.is_dir():
#     DOWNLOADS_PATH.mkdir()
framesPath = "frames"
if os.path.exists(framesPath):
    Continue
else:
    os.mkdir(framesPath)
framesPath = "frames" + '/' 
with st.sidebar:
    st.image("https://img.icons8.com/external-soft-fill-juicy-fish/100/null/external-machine-voice-technology-soft-fill-soft-fill-juicy-fish.png")
    st.title("Extract Frames from a Video")# some information to display about the app
    # some information to display about the app
    st.info("This application allows you to process a viode and extract individual frames.")


file = st.file_uploader("Upload your dataset here")

with st.expander("Preview Video"):
    st.video(file)

frap = st.number_input('Enter how many frames you want to skip', step=1, value=1)
button = st.button('Extract Frames')
if button:
    time_skips = int(frap)
    # path of the video file
    vidcap = cv.VideoCapture(file.name)
    success,image = vidcap.read()
    count = 0
    jump = 0
    while success:
        cv.imwrite("{}frame%d.jpg".format(framesPath) %count, image)     # save frame as JPEG file       
        success,image = vidcap.read()
        jump += time_skips
        vidcap.set(1, jump)
        count += 1
    print(f'{count} frames are exported')
    st.write(f'{count} frames are exported')

with st.expander('Preview of Extracted Images'):
    images = [i for i in (os.path.join(framesPath, f) for f in os.listdir(framesPath)) if os.path.isfile(i)]
    print(images)
    index= 0 #st.number_input('Index', step=1, value=0)
    col1, col2 = st.columns([1,1])

    with col1:
        prev = st.button('Prev')
    with col2:
        next = st.button('Next')
        
    if next:
        index+=1

    if prev:
        if index > 0:
            index -= 1

    image = Image.open(images[int(index)])
    st.image(image, use_column_width=True)

shutil.make_archive('frames', 'zip', framesPath)
with open('frames.zip', 'rb') as f:
   st.download_button('Download', f, 
   file_name=f'archive.zip')