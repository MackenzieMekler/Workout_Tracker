import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from datetime import datetime
# import plotly.express as px
import pandas as pd

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
    cnx = database()

    if len(name) > 0:
        try:
            df, df2 = cnx.search_exercise(name)
            set_df = pd.concat(df2)
            final_df = pd.DataFrame()
            names = []
            dates = []
            for row in set_df["exercise_id"]:
                names.append(df.loc[df['id'] == row, 'exercise_name'].iloc[0])
                dates.append(df.loc[df['id'] == row, 'exercise_date'].iloc[0])
            final_df['name'] = names
            final_df['weight'] = set_df['weight']
            final_df['reps'] = set_df['reps']
            final_df['date'] = dates
            st.dataframe(final_df)
        except:
            st.warning("Exercise is not found in records")

    num_sets = st.number_input("Number of Sets", step=1, min_value=0)
    col1, col2 = st.columns(2)
    with col1:
        rep_values = [st.number_input(f'Reps', key=f"rep_input_{i}", step=1)
            for i in range(num_sets)]
    with col2:
        weight_values = [st.number_input(f'Weight', key=f"weight_input_{i}", step=1)
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

        reps = []
        weight = []
        for i in range(num_sets):
            reps.append(exercise[f'{i+1}']['reps'])
            weight.append(exercise[f'{i+1}']["weight"])

        cnx.add_exercise(datetime.today().strftime("%Y-%m-%d"), exercise["name"], exercise["num_sets"], reps, weight)

        st.session_state.add = not st.session_state.add
        st.rerun()
else:
    status = st.radio("Any Pain?", ["No", "Yes"])
    where, scale = injury(status=status)

submit = st.button("Submit")
if submit:
    st.session_state.add = False
    st.session_state.previous = []
    switch_page("workout")
