import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Gym"
)

st.title("Gym Workout")

add_exercise = st.button("Add Exercise")

if "add" not in st.session_state:
    st.session_state.add = False

if add_exercise: 
    st.session_state.add = not st.session_state.add

# currently I am having issues with this feature because everytime you hit a button within the nested if statements, the code 
# reruns and returns the previous statement to false. There's a way to do caching that I might have to explore. 
if st.session_state.add: 
    name = st.text_input("Exercise Name:")
    ## I want to add code that will search the exercise name and display past workout values for that exercise but 
    ## I need to do this in the other envionrment so I can interact with the database 
    ## will probably need to search text input against database
    
    num_sets = st.number_input("Number of Sets", step=1, min_value=0)
    col1, col2 = st.columns(2)
    with col1:
        rep_values = [st.number_input(f'Reps', key=f"text_input_{i}", step=1)
            for i in range(num_sets)]
    with col2:
        weight_values = [st.number_input(f'Weight', key=f"text_input_{i+10}", step=1)
            for i in range(num_sets)]
    finish_add = st.button("Finish Exercise")
    if finish_add:
        ## save the exercise name, reps, and weights and then display on the page until the final workout is saved when this will be 
        ## placed into the database (again cannot do on this computer)
        st.session_state.add = not st.session_state.add

submit = st.button("Submit")
if submit:
    ## code that will save data to my database and possibly show a message 
    switch_page("workout")