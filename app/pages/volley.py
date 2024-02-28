import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from scripts.database import database
from datetime import datetime

st.set_page_config(
    page_title="Volleyball"
)

st.title("Volleyball Workout")

time = st.slider("Minutes Played", min_value=0, max_value=400, step=15)
playtype = st.selectbox("Type of Play", ["Enter Here", "Games", "Practice"])

if playtype == "Games":
    matches = st.slider(
        "Number of Matches",
        0,
        10
    )
else:
    matches = 0
# if playtype == "Practice":
#     st.multiselect("Focuses", ["Hitting", "Setting", "Defense", "Optioning", "Serving"])

submit = st.button("Submit")
if submit:
    cnx = database()
    cnx.add_volley(datetime.today().strftime("%Y-%m-%d"), time, int(playtype == "Games"), int(playtype == "Practice"), matches)

    switch_page("workout")

