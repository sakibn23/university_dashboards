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

# Trends Over Time
st.header("Trends Over Time")

# Aggregate data for trends
trend_data = data.groupby(['Year', 'Term']).agg({
    'Applications': 'sum',
    'Admitted': 'sum',
    'Enrolled': 'sum',
    'Retention Rate (%)': 'mean',
    'Student Satisfaction (%)': 'mean'
}).reset_index()

# Applications, Admissions, and Enrollments Trends
st.subheader("Applications, Admissions, and Enrollments")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=trend_data, x='Year', y='Applications', hue='Term', ax=ax, marker='o', label='Applications')
sns.lineplot(data=trend_data, x='Year', y='Admitted', hue='Term', ax=ax, marker='o', label='Admitted')
sns.lineplot(data=trend_data, x='Year', y='Enrolled', hue='Term', ax=ax, marker='o', label='Enrolled')
ax.set_title("Trends Over Time")
ax.set_ylabel("Count")
ax.legend()  # Add legend to differentiate lines
st.pyplot(fig)

# Retention Rate and Satisfaction Trends
st.subheader("Retention Rate and Satisfaction Trends")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=trend_data, x='Year', y='Retention Rate (%)', hue='Term', ax=ax, marker='o', label='Retention Rate (%)')
sns.lineplot(data=trend_data, x='Year', y='Student Satisfaction (%)', hue='Term', ax=ax, marker='o', label='Student Satisfaction (%)')
ax.set_title("Retention and Satisfaction Trends")
ax.set_ylabel("Percentage")
ax.legend()  # Add legend to differentiate lines
st.pyplot(fig)

# Department-wise Trends
st.header("Department-wise Trends")
department_trends = data.groupby('Year').agg({
    'Engineering Enrolled': 'sum',
    'Business Enrolled': 'sum',
    'Arts Enrolled': 'sum',
    'Science Enrolled': 'sum'
}).reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=department_trends, x='Year', y='Engineering Enrolled', ax=ax, label='Engineering', marker='o')
sns.lineplot(data=department_trends, x='Year', y='Business Enrolled', ax=ax, label='Business', marker='o')
sns.lineplot(data=department_trends, x='Year', y='Arts Enrolled', ax=ax, label='Arts', marker='o')
sns.lineplot(data=department_trends, x='Year', y='Science Enrolled', ax=ax, label='Science', marker='o')
ax.set_title("Department-wise Enrollment Trends")
ax.set_ylabel("Enrollment Count")
ax.legend()  # Add legend to differentiate lines
st.pyplot(fig)

# Spring vs. Fall Comparison
st.header("Spring vs. Fall Comparison")

# Applications, Admissions, and Enrollments Comparison
st.subheader("Applications, Admissions, and Enrollments Comparison")
spring_data = data[data['Term'] == 'Spring']
fall_data = data[data['Term'] == 'Fall']

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=spring_data, x='Year', y='Applications', ax=ax, label='Spring Applications', marker='o')
sns.lineplot(data=fall_data, x='Year', y='Applications', ax=ax, label='Fall Applications', marker='o')
ax.set_title("Applications: Spring vs. Fall")
ax.set_ylabel("Count")
ax.legend()
st.pyplot(fig)

# Retention Rate Comparison
st.subheader("Retention Rate Comparison")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=spring_data, x='Year', y='Retention Rate (%)', ax=ax, label='Spring Retention Rate (%)', marker='o')
sns.lineplot(data=fall_data, x='Year', y='Retention Rate (%)', ax=ax, label='Fall Retention Rate (%)', marker='o')
ax.set_title("Retention Rate: Spring vs. Fall")
ax.set_ylabel("Percentage")
ax.legend()
st.pyplot(fig)

# Satisfaction Comparison
st.subheader("Satisfaction Comparison")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=spring_data, x='Year', y='Student Satisfaction (%)', ax=ax, label='Spring Satisfaction (%)', marker='o')
sns.lineplot(data=fall_data, x='Year', y='Student Satisfaction (%)', ax=ax, label='Fall Satisfaction (%)', marker='o')
ax.set_title("Satisfaction: Spring vs. Fall")
ax.set_ylabel("Percentage")
ax.legend()
st.pyplot(fig)

# Key Findings and Insights
st.header("Key Findings and Insights")
st.write("""
1. **Applications, Admissions, and Enrollments**: Applications have steadily increased over the years, with a noticeable spike in 2024.
2. **Retention Rate**: Retention rates have consistently improved, reaching 90% in 2024.
3. **Student Satisfaction**: Satisfaction scores have also shown a steady increase, peaking at 88% in 2024.
4. **Department-wise Trends**: Engineering has the highest enrollment, while Science has seen a decline in recent years.
5. **Spring vs. Fall**: Both terms show similar trends, but Fall terms tend to have slightly higher enrollments.
""")
