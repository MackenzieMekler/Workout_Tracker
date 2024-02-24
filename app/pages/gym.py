import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from templates.sections import injury
from scripts.database import database

st.set_page_config(
    page_title="Gym"
)

st.title("Gym Workout")

if "previous" not in st.session_state:
    st.session_state.previous = []

for item in st.session_state.previous:
    st.text(item["name"])
    for i in range(item['num_sets']):
        st.text(f'- {item[f"{i+1}"]["reps"]} x {item[f"{i+1}"]["weight"]}')

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
        exercise = {
            "name": name,
            "num_sets": num_sets,
        }
        for i in range(num_sets):
            exercise[f'{i+1}'] = {
                "reps": rep_values[i],
                "weight": weight_values[i]
            }

        st.session_state.previous.append(exercise)

        st.session_state.add = not st.session_state.add
        st.rerun()
else:
    status = st.radio("Any Pain?", ["No", "Yes"])
    where, scale = injury(status=status)

submit = st.button("Submit")
if submit:
    cnx = database()
    exercise = st.session_state.previous[0]
    cnx.add_exercise("2024-02-22", exercise["name"], exercise["num_sets"], [exercise["1"]["reps"]], [exercise["1"]["weight"]])
    st.session_state.add = False
    st.session_state.previous = []
    switch_page("workout")
