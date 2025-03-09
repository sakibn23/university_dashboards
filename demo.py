# Load necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("university_student_dashboard_data.csv")
    return data

data = load_data()

# Title of the dashboard
st.title("University Admissions, Retention, and Satisfaction Dashboard")

# Sidebar for filters
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", data['Year'].unique())
selected_term = st.sidebar.selectbox("Select Term", data['Term'].unique())

# Filter data based on selections
filtered_data = data[(data['Year'] == selected_year) & (data['Term'] == selected_term)]

# Display key metrics
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Applications", filtered_data['Applications'].values[0])
with col2:
    st.metric("Total Admitted", filtered_data['Admitted'].values[0])
with col3:
    st.metric("Total Enrolled", filtered_data['Enrolled'].values[0])

# Retention Rate and Satisfaction Score
st.header("Retention and Satisfaction")
col1, col2 = st.columns(2)
with col1:
    st.metric("Retention Rate (%)", filtered_data['Retention Rate (%)'].values[0])
with col2:
    st.metric("Student Satisfaction (%)", filtered_data['Student Satisfaction (%)'].values[0])

# Enrollment Breakdown by Department
st.header("Enrollment Breakdown by Department")
department_data = filtered_data[['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']]
st.bar_chart(department_data.T)
