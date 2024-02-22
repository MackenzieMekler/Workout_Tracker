import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from templates.sections import analyze_set, injury

## maybe make this page more like gym where you add a set and then when you submit the set it prints to the screen so there's less
## of a chance for it to get deleted or something and this would hopefully just look cleaner
## additionally this would be able to catch errors in formatting more quickly as they happen 

st.set_page_config(
    page_title="Swim"
)
st.title("Swimming Workout")

time = st.slider("Time Swimming", 0, 120, 0, 5)
type = st.multiselect("What type of swim was this?", ["Distance", "Mid-Distance", "Sprint", "Technique", "Stroke", "Other"])

num_sets = st.number_input("Number of Sets", step=1, min_value=0)

st.text("""Input format for the sets:
    'Number' x 'Amount of Yards' 'Type' on mm:ss; next; next; x 'num repeats'
Example:
    10 x 50 freestyle on 01:00; 4 x 25 variable speed on 00:40; x 4
""")

warmup = st.text_input("Warm Up")
warmup_components, warmup_yards = analyze_set(warmup)

sets = [st.text_input(f'Set {i+1}', key=f"text_input_{i}")
    for i in range(num_sets)]

warmdown = st.text_input("Warm Down")
warmdown_components, warmdown_yards = analyze_set(warmdown)

status = st.radio("Did you feel pain?", ["No", "Yes"])
where, scale = injury(status=status)

submit = st.button("Submit")
if submit:
    total_yards = warmup_yards + warmdown_yards
    ## code that will save data to my database and possibly show a message 
    for sett in sets:
        set_components, set_yards = analyze_set(sett)
        total_yards = total_yards + set_yards



    switch_page("workout")
# upon submit, save the current settings into a sql dataframe or a json object
# also reset page and return to homepage