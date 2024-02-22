import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Volleyball"
)

st.title("Volleyball Workout")

st.slider("Hours Played", min_value=0.5, max_value=6.5, step=0.5)
playtype = st.selectbox("Type of Play", ["Enter Here", "Games", "Practice"])

if playtype == "Games": 
    st.text_input("Partners:")
    st.slider(
        "Number of Matches",
        1,
        10
    )
if playtype == "Practice":
    st.multiselect("Focuses", ["Hitting", "Setting", "Defense", "Optioning", "Serving"])

submit = st.button("Submit")
if submit:
    ## code that will save data to my database and possibly show a message 
    switch_page("workout")
# upon submit, save the current settings into a sql dataframe or a json object
# also reset page and return to homepage