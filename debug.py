import pandas as pd
import streamlit as st

# Debug: Check if the invalid option is set
st.write("Pandas Options:", pd.options)

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("university_student_dashboard_data.csv")
    return data

data = load_data()

# Display the first few rows of the dataset
st.write("Dataset Preview:", data.head())
