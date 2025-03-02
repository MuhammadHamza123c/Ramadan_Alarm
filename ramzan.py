import requests
import streamlit as st
import pygame
from datetime import datetime
pygame.mixer.init()
st.markdown("### RAMADAN ALARM SYSTEM!!")

hour = st.slider("Select Hour:", min_value=1, max_value=12, value=1)
mins = st.slider("Select Minutes:", min_value=0, max_value=59, value=0)
state=st.radio("Choose Time of day",
               ("Choose one","AM","PM"),
               index=0)
if state and mins and hour:
  
 hour_str = f"{hour:02d}"  
 mins_str = f"{mins:02d}"
 user=f"{hour_str}:{mins_str}{state}"
 if user and state!="Choose one":
  st.write(user)
  while True: 
 
   current=datetime.now().strftime("%I:%M%p")
   print(current)
   if user==current:
    
    url="https://blynk.cloud/external/api/update?token=rWrw3M-TKFWyLy_uEnFDV7IdxZ5LUFzc&V1=1"
    response=requests.get(url)
    pygame.mixer.music.load("Main Hoon na.wav")  
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
      pass
  

#  elif user=="off":
#   url="https://blynk.cloud/external/api/update?token=rWrw3M-TKFWyLy_uEnFDV7IdxZ5LUFzc&V1=0"
#   response=requests.get(url)
  

 
 