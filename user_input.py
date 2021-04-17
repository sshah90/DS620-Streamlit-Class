import streamlit as st
import pandas as pd
import numpy as np

from datetime import time,datetime

"# In this section we will try to explore ways to interarate with users"

# Add interactivity with widgets
"Checkbox with `st.checkbox` command"
s = st.checkbox("Show dataframe")

if s:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    chart_data

# Use a selectbox with options
"Display a select widget with `st.selectbox`"

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    
option = st.selectbox("Which number do you like best?", ["DS-610","DS-620","DS-640"])

"You selected: ", option

# second_option = st.selectbox("Which number do you like best?", chart_data["a"])

# "You selected: ", second_option

"Display a multiselect widget with `st.multiselect`"

options = st.multiselect('What are your favorite colors',['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])
st.write('You selected:', options)

"Display a radio button widget with `st.radio`"

genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")


"Display a slider widget with `st.slider`. This supports int, float, date, time, and datetime types."
age = st.slider('How old are you?', 0, 130, 10,10,format="%d days")
st.write("I'm ", age, 'years old')

"Time slider example"
appointment = st.slider("Schedule your appointment:",value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

"Date slider example"
start_time = st.slider("When do you start?",datetime(2010, 1, 1, 0, 0),datetime(2020, 1, 1, 9, 30),value=datetime(2020, 1, 1, 9, 30),format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

"Display a slider widget to select items from a list using `st.select_slider`"
color = st.select_slider('Select a color of the rainbow',options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

"Display a single-line text input widget using `st.text_input`"
title = st.text_input('Movie title', 'Godzilla vs Kong')
st.write('The current movie title is', title)

"Display a multi-line text input widget using `st.text_area`"
txt = st.text_area('Text to analyze',"")
st.write('Sentiment:', txt)

"Display a button widget with `st.button`, returns bool"
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

"Display a date input widget with `st.date_input`"
d = st.date_input("When's your birthday", date(2019, 7, 6))
st.write("Your birthday is:", d)

"""
## **Explore following user input functionality our own**
- number_input
- time_input
- file_uploader
- color_picker
"""

