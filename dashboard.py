import streamlit as st
import altair as alt
import pandas as pd

# Data for the Gantt Chart
data = [
    {"Task": "Define Project Scope and Objectives", "Start": "2024-05-21", "End": "2024-05-22"},
    {"Task": "Stakeholder Alignment and Communication Plan", "Start": "2024-05-23", "End": "2024-05-25"},
    {"Task": "Team Training and Tool Setup", "Start": "2024-05-26", "End": "2024-05-27"},
    {"Task": "Sprint 1 Planning", "Start": "2024-05-28", "End": "2024-05-28"},
    {"Task": "Sprint 1 Development and Testing", "Start": "2024-05-29", "End": "2024-06-09"},
    {"Task": "Sprint 1 Review and Retrospective", "Start": "2024-06-10", "End": "2024-06-10"},
    {"Task": "Sprint 2 Planning", "Start": "2024-06-11", "End": "2024-06-11"},
    {"Task": "Sprint 2 Development and Testing", "Start": "2024-06-12", "End": "2024-06-23"},
    {"Task": "Sprint 2 Review and Retrospective", "Start": "2024-06-24", "End": "2024-06-24"},
    {"Task": "Sprint 3 Planning", "Start": "2024-06-25", "End": "2024-06-25"},
    {"Task": "Sprint 3 Development and Testing", "Start": "2024-06-26", "End": "2024-07-07"},
    {"Task": "Sprint 3 Review and Retrospective", "Start": "2024-07-08", "End": "2024-07-08"},
    {"Task": "Co-creation Workshops", "Start": "2024-06-01", "End": "2024-06-01"},
    {"Task": "Co-creation Workshops", "Start": "2024-07-01", "End": "2024-07-01"},
    {"Task": "Beta Testing", "Start": "2024-06-15", "End": "2024-07-01"},
    {"Task": "In-app Feedback Setup", "Start": "2024-06-01", "End": "2024-07-08"},
    {"Task": "Post-Implementation Review", "Start": "2024-07-09", "End": "2024-07-10"},
    {"Task": "Adjustments Based on Feedback and Metrics", "Start": "2024-07-11", "End": "2024-07-15"},
]

# Create a DataFrame
df = pd.DataFrame(data)

# Convert Start and End dates to datetime
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Calculate Duration in days
df["Duration"] = (df["End"] - df["Start"]).dt.days + 1

# Streamlit app
st.set_page_config(layout="wide")
st.title("Macrohard Software Solutions Upgrade Project Gantt Chart")

# Create Gantt Chart using Altair
chart = alt.Chart(df).mark_bar().encode(
    x='Start:T',
    x2='End:T',
    y=alt.Y('Task:N', sort=alt.EncodingSortField(field="Start", order="ascending")),
    color='Task:N',
    tooltip=['Task', 'Start', 'End', 'Duration']
).properties(
    width=800,
    height=600
).interactive()

st.altair_chart(chart)
