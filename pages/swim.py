import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Swim"
)

time = st.slider("Time Swimming", 0, 120, 0, 5)
num_sets = st.number_input("Number of Sets", step=1, min_value=0)

warmup = st.text_input("Warm Up")

input_values = [st.text_input(f'Set {i+1}', key=f"text_input_{i}")
    for i in range(num_sets)]

warmdown = st.text_input("Warm Down")

submit = st.button("Submit")
if submit:
    ## code that will save data to my database and possibly show a message 
    switch_page("workout")
# upon submit, save the current settings into a sql dataframe or a json object
# also reset page and return to homepage