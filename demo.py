import streamlit as st

st.snow()

# Title
st.title("Streamlit Session Demo")

# Text input
name = st.text_input("Enter your name:")

# Slider input for age
age = st.slider("Select your age:", 18, 60)

# Display a message
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")
