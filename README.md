# <b> Dyslexia_screener</b>
 It is  a web app that combines eye tracking and voice recognition to simulate a reading clarity test 
 using Streamlit, Opencv, SpeechRecognition and Gazetracking 

# Features 
*eye tracking using webcam with the help of gazetraking and opencv*
*Voice recognition using speechrecognition*
*help in real time reading difficulty*
*user friendly ui with streamlit*
*pie chart for visual summary of eye movement*
*saves your result to CSV and allow downloading*

# Setup
pip install Opencv-python stramlit SpeechRecognition matplotlib pandas 
install dlib
git clone https://github.com/antoinelame/GazeTracking.git 
it has gaze tracking and pretrained model [face landmark detect - shape_predictor_68_face_landmarks.dat]


# How it works 
In terminal type streamlit run main.py
click start test -webcam and microphone will activated
for 15 seconds 
Read the passage loud 
keep your eyes on screen
get instant result showing 
a reading clarity and score risk in csv file 


