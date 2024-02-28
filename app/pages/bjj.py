import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from scripts.database import database
from datetime import datetime

st.set_page_config(
    page_title="Brazilian Jiu Jitsu"
)

st.title("Brazilian Jiu Jitsu")

time = st.slider("Hours Practiced", min_value=0, max_value=180, step=5)
playtype = st.selectbox("Type of Practice", ["Enter Here", "Practice", "Rolling"])

submit = st.button("Submit")
if submit:
    cnx = database()
    cnx.add_bjj(datetime.today().strftime("%Y-%m-%d"), time, int(playtype=="Practice"), int(playtype=="Rolling"))

    switch_page("workout")
