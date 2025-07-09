import streamlit as st # type: ignore
import cv2  # type: ignore
from GazeTracking.gaze_tracking import GazeTracking
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

def capture_gaze (duration = 15):
    gaze = GazeTracking()
    cam = cv2.VideoCapture(0)
    gaze_list = []
    start = time.time()

    while time.time()-start < duration:
       ret,frame = cam.read()
       if not ret:
               break
               
       gaze.refresh(frame)
       if gaze.is_blinking():gaze_list.append("Blinking")
       elif gaze.is_right():gaze_list.append("Right")   
       elif gaze.is_left():gaze_list.append("left")
       elif gaze.is_center():gaze_list.append("center")
       else:gaze_list.append("Unknown")

    cam.release()
    return gaze_list
          
def record_voice(duration=15,passage=""):
        recog = sr.Recognizer()
        expected_words = passage.lower().replace('.',"").replaceeplace(',', '').split()
        said_text = " "

        with sr.Microphone() as source:
          recog.adjust_for_ambient_noise(source)
          try:
               audio = recog.listen(source,timeout=duration,phrase_time_limit=duration)
               said_text = recog.recognize_google(audio)
               spoken = said_text.lower().replace('.',"").replace('.',"").split()
               score = sum(1 for word in expected_words if any(word in w for w in spoken ))
          except Exception as e:
               said_text = f"Error:{str(e)}"
               score = 0

        return said_text,score
def save_csv(text,score,gaze_summary,risk_level):
                    with open("dyslexia_results.csv","a",newline="",encoding="utf-8") as f:
                      writer = csv.writer(f)
                      writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text, score, gaze_summary, risk_level]) 

st.subheader("Pick a passage to Read")
passages = {
          "EASY":"The cat sat on the mat.It was a sunny day.",
          "MEDIUM":"Reading books is a great way to learn and grow your mind.",
          "HARD":"Despite difficulties,perseverance and hard work lead to success."}
level = st.selectbox("choose Level",list(passages.keys()))
st.success(passages[level])
if st.button ("Start test"):
     st.warning("Test running for 15s Read aloud and look at the screen!")
     with ThreadPoolExecutor() as executor:
                       gaze_result=executor.submit(capture_gaze,15)
                       voice_result=executor.submit(record_voice, 15, passages[level])
                       gaze_data =gaze_result.result()
                       spoken_text,voice_score = voice_result.result()
     st.divider()
     st.header("✅  Test Results")
     gaze_counts = {d: gaze_data.count(d) for d in ["Center", "Left", "Right", "Blinking"]}


col1, col2 = st.columns(2)
with col1:
     for key, val in gaze_counts.items():
          st.metric(f"(key) Looks", val)

with col2:
     total_words = len(passages[level].split())
     st.metric("Voice Score", f"(voice_score)/(total_words)")
     st.write("You said:", spoken_text)

st.subheader("🔍 Your Reading Level")
if voice_score >= total_words * 0.6 and gaze_counts["center"] > 10:
     risk = "✅ Low Risk - Clear reading."
     st.success(risk)
elif voice_score >= total_words * 0.4 or (gaze_counts["Left"] + gaze_counts["Right"]) > 10:
     risk = "🟡 Medium Risk - Some struggle."
     st.warning(risk)
else:
 risk = "🔴 High Risk - Possible reading difficulty."
st.error(risk)
save_csv(spoken_text, voice_score, gaze_counts, risk)

st.subheader("👁 Eye Movement Summary")
fig, ax = plt.subplots()
ax.pie(gaze_counts.values(), labels=gaze_counts.keys(), autopct='%1.1f%%', colors=['#4CAF50', '#2196F3', '#FF9800', '#9E9E9E'])
st.pyplot(fig)

df = pd.DataFrame([{
     "Timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
     "Voice Text":spoken_text,
     "Score": voice_score,
     "Gaze Summary": gaze_counts,
     "Risk Level": risk
}])
st.download_button("📥 Download Results", df.to_csv(index=False).encode("utf-8"), "dyslexia_test_result.csv", "text/csv")
st.divider()
st.caption("🚨 For learning/demo only. Not a diagnosis.")



                                               

                          


               

     
     
