import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from datetime import datetime
# import plotly.express as px
import pandas as pd
import json

from templates.sections import injury
from scripts.database import database

st.set_page_config(
    page_title="Gym"
)

with open("/app/json/gym.json", "r") as file:
     try:
         data = json.load(file)
     except:
         print("File Empty")
         data = {}


st.title("Gym Workout")

###### Load all session states and update according to the gym.json temporary save file #######

if "previous" not in st.session_state:
    if 'previous' in data.keys():
        st.session_state.previous = data['previous']
    else:
        st.session_state.previous = []

if "add" not in st.session_state:
    if 'add' in data.keys():
        st.session_state.add = data["add"]
    else:
        st.session_state.add = False

if "name" not in st.session_state:
    if 'name' in data.keys():
        st.session_state.name = data["name"]
    else:
        st.session_state.name = ""

if "num_sets" not in st.session_state:
    if 'num_sets' in data.keys():
        st.session_state.num_sets = data["num_sets"]
    else:
        st.session_state.num_sets = 0

if "new_set" not in st.session_state:
    if 'new_set' in data.keys():
        st.session_state.new_set = data["new_set"]
    else:
        st.session_state.new_set = False

if "rep_values" not in st.session_state:
    if 'rep_values' in data.keys():
        st.session_state.rep_values = data["rep_values"]
    else:
        st.session_state.rep_values = []

if "weight_values" not in st.session_state:
    if 'weight_values' in data.keys():
        st.session_state.weight_values = data["weight_values"]
    else:
        st.session_state.weight_values = []



for item in st.session_state.previous:
    st.text(item["name"])
    for i in range(item['num_sets']):
        st.text(f'- {item[f"{i+1}"]["reps"]} x {item[f"{i+1}"]["weight"]}')

add_exercise = st.button("Add Exercise")


if add_exercise:
    st.session_state.add = not st.session_state.add


if st.session_state.add:
    # Get the current exercise name and save to session state
    name = st.text_input("Exercise Name:")
    if len(name) > 0:
        st.session_state.name = name
    cnx = database()
    # search database for exercise feature
    if len(st.session_state.name) > 0:
        st.success(st.session_state.name)
        try:
            df, df2 = cnx.search_exercise(st.session_state.name)
            st.dataframe(df)
            # set_df = pd.concat(df2)
            final_df = pd.DataFrame()
            names = []
            dates = []
            weights = []
            reps = []
            for dataframe in df2:
                for row in dataframe["exercise_id"]:
                    names.append(df.loc[df['id'] == row, 'exercise_name'].iloc[0])
                    dates.append(df.loc[df['id'] == row, 'exercise_date'].iloc[0])
                weights.extend(dataframe['weight'].tolist())
                reps.extend(dataframe['reps'].tolist())
            final_df['name'] = names
            final_df['weight'] = weights
            final_df['reps'] = reps
            final_df['date'] = dates
            st.dataframe(final_df.tail(4))
        except Exception as error:
            # st.warning(error)
            st.warning("Exercise is not found in records")

    new_set = st.button("New Set")
    if new_set:
        st.session_state.new_set = not st.session_state.new_set

    if st.session_state.new_set:
        col1, col2 = st.columns(2)

        with col1:
            rep_value = st.number_input("Reps", step=1)
        with col2:
            weight_value = st.number_input('Weight', step=1)
        finish_set = st.button("Submit Set")
        if finish_set:
            st.session_state.rep_values.append(rep_value)
            st.session_state.weight_values.append(weight_value)
            st.session_state.num_sets += 1
            st.session_state.new_set = False
            st.session_state.name = ""
            st.rerun()
    finish_add = st.button("Finish Exercise")
    if finish_add:
        exercise = {
            "name": st.session_state.name,
            "num_sets": st.session_state.num_sets,
        }
        for i in range(st.session_state.num_sets):
            exercise[f'{i+1}'] = {
                "reps": st.session_state.rep_values[i],
                "weight": st.session_state.weight_values[i]
            }

        st.session_state.previous.append(exercise)

        cnx.add_exercise(datetime.today().strftime("%Y-%m-%d"), exercise["name"], st.session_state.num_sets, st.session_state.rep_values, st.session_state.weight_values)
        st.session_state.name = ''
        st.session_state.add = not st.session_state.add
        st.session_state.weight_values = []
        st.session_state.rep_values = []
        st.session_state.num_sets = 0
        st.rerun()
else:
    status = st.radio("Any Pain?", ["No", "Yes"])
    where, scale = injury(status=status)

submit = st.button("Submit")
if submit:
    st.session_state.add = False
    st.session_state.previous = []
    st.session_state.name = ""
    st.session_state.num_sets = 0
    st.session_state.rep_values = []
    st.session_state.weight_values = []
    data = {}
    with open("/app/json/gym.json", 'w') as file:
        json.dump(data, file)
    switch_page("workout")


with open("/app/json/gym.json", 'w') as file:
    data['add'] = st.session_state.add
    data['previous'] = st.session_state.previous
    data['name'] = st.session_state.name
    data['num_sets'] = st.session_state.num_sets
    data['rep_values'] = st.session_state.rep_values
    data['weight_values'] = st.session_state.weight_values
    json.dump(data, file)
