import streamlit as st

st.title("Basic App")

num_feet = st.number_input("Your Height (Feet)")
num_inches = st.number_input("Your Height (Inches)")

num_weight = st.number_input("Your Weight (Pounds)")