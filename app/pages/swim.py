import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from datetime import datetime
from templates.sections import analyze_set, injury
from scripts.database import database
## maybe make this page more like gym where you add a set and then when you submit the set it prints to the screen so there's less
## of a chance for it to get deleted or something and this would hopefully just look cleaner
## additionally this would be able to catch errors in formatting more quickly as they happen 

st.set_page_config(
    page_title="Swim"
)
st.title("Swimming Workout")

time = st.slider("Time Swimming", 0, 120, 0, 5)
type = st.multiselect("What was the main focus?", ["Distance", "Mid-Distance", "Sprint", "Technique", "Stroke", "Other"])

total_yards = 0

num_sets = st.number_input("Number of Parts", step=1)
# add a few containers that will be used to help calculate total yards by giving 
# a few places for yards a few places for multipliers then totaling it. 

num_counters = st.number_input("Number of counters", step=1, min_value=0)
col1, col2 = st.columns(2)
calc = [(col1.number_input("Yards", key=f"yard_input_{i}", step=25), col2.number_input("Multiplier", key = f"multiply_input_{i}", step=1, min_value=1)) for i in range(num_counters)]

status = st.radio("Did you feel pain?", ["No", "Yes"])
where, scale = injury(status=status)

submit = st.button("Submit")
if submit:
    for comb in calc:
        total_yards += comb[0] * comb[1]

    distance = "Distance" in type
    mid_distance = "Mid-Distance" in type
    sprint = "Sprint" in type
    stroke = "Stroke" in type
    technique = "Technique" in type
    other = "Other" in type

    cnx = database()
    cnx.add_swim(datetime.today().strftime("%Y-%m-%d"), time, total_yards, int(distance), int(mid_distance), int(sprint), int(stroke), int(technique), int(other))
    switch_page("workout")
# upon submit, save the current settings into a sql dataframe or a json object
# also reset page and return to homepage
