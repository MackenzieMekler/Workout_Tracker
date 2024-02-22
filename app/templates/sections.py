import streamlit as st

def analyze_set(st_text_input):
    if len(st_text_input) == 0:
        return "none", 0
    try:
        parts = []
        total_yards = 0
        string_splice = st_text_input
        while not string_splice.find(";") == -1:
            current = string_splice[:string_splice.find(';')].strip()
            parts.append(current)
            num = int(current[:current.find('x')].strip())
            yards = int(current[current.find('x')+2:current.find(' ', current.find('x')+2)].strip())
            total_yards = total_yards + num * yards
            string_splice = string_splice[string_splice.find(';')+1:].strip()
        final_modifier = int(string_splice[2:])
        total_yards = total_yards * final_modifier
        return parts, total_yards
    except:
        st.error("An error occurred!! The above set may not be formatted properly")

def injury(status):
    if status == "Yes":
        where = st.multiselect("Where?", [
            "Head/Neck",
            "Upper Back",
            "Lower Back",
            "Shoulders",
            "Arms",
            "Elbows",
            "Chest/Stomach",
            "Waist",
            "Legs",
            "Knees",
            "Ankles",
            "Feet"
        ])
        scale = st.slider("On a Scale From 1 to 10", min_value=1.0, max_value=10.0, step=0.5)
    else:
        where = ["None"]
        scale = 0
    return where, scale
