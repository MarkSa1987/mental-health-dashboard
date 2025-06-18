
import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Mental Health in Tech Survey Dashboard")

# Load data
df = pd.read_csv("cleaned_survey.csv")

# Sidebar filters
st.sidebar.header("Filter the Data")
gender_filter = st.sidebar.multiselect("Select Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
age_range = st.sidebar.slider("Select Age Range", int(df['Age'].min()), int(df['Age'].max()), (20, 40))

# Filter data based on sidebar inputs
filtered_df = df[(df['Gender'].isin(gender_filter)) & (df['Age'].between(age_range[0], age_range[1]))]

# Show filtered data
st.subheader("Filtered Data Sample")
st.dataframe(filtered_df.head())

# Bar chart: Treatment by Gender
st.subheader("Mental Health Treatment by Gender")
treatment_chart = filtered_df.groupby(['Gender', 'treatment']).size().reset_index(name='count')
fig = px.bar(treatment_chart, x='Gender', y='count', color='treatment', barmode='group')
st.plotly_chart(fig)

# Pie chart: Work Interference
st.subheader("Work Interference Distribution")
interfere_counts = filtered_df['work_interfere'].value_counts().reset_index()
fig2 = px.pie(interfere_counts, names='index', values='work_interfere', title='How Mental Health Interferes with Work')
st.plotly_chart(fig2)

# Note
st.markdown("📌 This is an interactive dashboard built with Streamlit. Use the sidebar to filter the data.")
