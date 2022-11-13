import streamlit as st
from vidProcess import *
import cv2 as cv
import tempfile

with st.sidebar:
    st.image("https://img.icons8.com/external-soft-fill-juicy-fish/100/null/external-machine-voice-technology-soft-fill-soft-fill-juicy-fish.png")
    st.title("AutoML")
    # control the navigation suing radio
    choice = st.radio("Navigation", [
                                    "Upload",
                                    "Process",
                                    "Download"])
    # some information to display about the app
    st.info("This application allows you to process a viode and extract individual frames.")

source_file = "source.mp4"

if choice == "Upload":
    st.title("Upload your data for modelling")
    file = st.file_uploader("Upload your dataset here")
    if file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())
        vf = cv.VideoCapture(tfile.name)

        stframe = st.empty()

        while vf.isOpened():
            # ret, frame = vf.read()
            # # if frame is read correctly ret is True
            # if not ret:
            #     print("Can't receive frame (stream end?). Exiting ...")
            #     break
            # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # stframe.image(gray)
            st.video(vf, format="video/mp4", start_time=0)