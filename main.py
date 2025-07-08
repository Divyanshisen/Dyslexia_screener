import streamlit as st # type: ignore
import cv2  # type: ignore
from gaze_tracking import GazeTracking # type: ignore
import   speech_recognition as sr
from concurrent.futures import ThreadPoolExecutor
import time
import csv
from datetime import datetime
import pandas as pd  # type: ignore
import matplotlib as plt # type: ignore

st.set_page_config(page_title ="Dyslexia Screener",page_icon="📖",layout ="centered")
st.title("🧠Dyslexia Eye and Reading Test")
st.caption("Track your reading and voice clarity. Not a medical tool!")
st.divider()

with st.expander("What's this?"):
    st.write ("""
         This is a little tool to:
         -Track your eye directions while reading .
         -Listen to what you read.
         -Show simple reading clarity.
         -Show a simple reading clarity score.
        Just for learning ,Not a daignosis !
    """)
