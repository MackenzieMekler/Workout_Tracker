import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="New Workout"
)

st.title("What type of workout will this be?")
st.title("\n")
col1, col2, col3, col4 = st.columns(4)
gym = col1.button("Gym")
swim = col2.button("Swimming")
volley = col3.button("Volleyball")
bjj = col4.button("Brazilian Jiu Jitsu")

if gym:
    switch_page("gym")
if swim:
    switch_page("swim")
if volley:
    switch_page("volley")
if bjj:
    switch_page("bjj")