import streamlit as st

st.title("Basic App")

st.sidebar.info("Choose Metric")
sel_metric = st.sidebar.selectbox(
    "Choose your metric",
    ("Kgs and Meters", "Pounds and Inches"))

if sel_metric == "Kgs and Meters":
    num_height = st.number_input("Your Height (meters)", 1.65)
    num_weight = st.number_input("Your Weight (Kgs)", 68)
    BMI = num_weight / (num_height ** 2)
else:
    num_height = st.number_input("Your Height (Inches)", 65)
    num_weight = st.number_input("Your Weight (Pounds)", 150)
    BMI = (num_weight / (num_height ** 2)) * 703

st.success('The output is {}'.format(BMI))