import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Brazilian Jiu Jitsu"
)

st.title("Brazilian Jiu Jitsu")

st.slider("Hours Practiced", min_value=0.25, max_value=2.5, step=0.25)
playtype = st.selectbox("Type of Practice", ["Enter Here", "Practice", "Rolling"])

if playtype == "Practice": 
    st.multiselect("Focuses", ["Takedowns", "Guards", "Guard Escape", "Chokes", "Arm Submissions", "Leg Submissions"])
    st.text_input("Specifics: ")
if playtype == "Rolling":
    st.text_input("Partners: ")


submit = st.button("Submit")
if submit:
    ## code that will save data to my database and possibly show a message 
    switch_page("workout")