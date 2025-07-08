import streamlit as st # type: ignore
import cv2 
from gaze_tracking import GazeTracking
import   speech_recognition as sr
from concurrent.futures import ThreadPoolExecutor
import time
import csv
from datetime import datetime
import pandas as pd 
import matplotlib as plt


