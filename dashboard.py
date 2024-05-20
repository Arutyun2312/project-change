
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Macrohard", layout="wide")

# Define the tasks for each phase
tasks = [
    {"Phase": "Phase 1: Planning and Preparation", "Task": "Finalize Detailed Project Scope and Objectives", "Start": "2024-05-21", "End": "2024-05-22"},
    {"Phase": "Phase 1: Planning and Preparation", "Task": "Stakeholder Alignment and Communication Plan", "Start": "2024-05-23", "End": "2024-05-25"},
    {"Phase": "Phase 1: Planning and Preparation", "Task": "Team Training and Tool Setup", "Start": "2024-05-26", "End": "2024-05-27"},
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 1 Planning", "Start": "2024-05-28", "End": "2024-05-29"},  # Extended to 2 days
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 1 Development and Testing", "Start": "2024-05-29", "End": "2024-06-09"},
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 1 Review and Retrospective", "Start": "2024-06-10", "End": "2024-06-11"},  # Extended to 2 days
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 2 Planning", "Start": "2024-06-11", "End": "2024-06-12"},  # Extended to 2 days
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 2 Development and Testing", "Start": "2024-06-12", "End": "2024-06-23"},
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 2 Review and Retrospective", "Start": "2024-06-24", "End": "2024-06-25"},  # Extended to 2 days
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 3 Planning", "Start": "2024-06-25", "End": "2024-06-26"},  # Extended to 2 days
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 3 Development and Testing", "Start": "2024-06-26", "End": "2024-07-07"},
    {"Phase": "Phase 2: Execution and Monitoring", "Task": "Sprint 3 Review and Retrospective", "Start": "2024-07-08", "End": "2024-07-09"},  # Extended to 2 days
    {"Phase": "Phase 3: Evaluation and Adjustment", "Task": "Post-Implementation Review", "Start": "2024-07-09", "End": "2024-07-10"},
    {"Phase": "Phase 3: Evaluation and Adjustment", "Task": "Adjustments Based on Feedback and Performance Metrics", "Start": "2024-07-11", "End": "2024-07-15"},
]

# Convert the tasks into a DataFrame
df = pd.DataFrame(tasks)

# Convert Start and End columns to datetime
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Custom color mapping for Phase 2 tasks
color_mapping = {
    'Sprint 1 Planning': '#1f77b4',
    'Sprint 1 Development and Testing': '#1f77b4',
    'Sprint 1 Review and Retrospective': '#003366',
    'Sprint 2 Planning': '#ff7f0e',
    'Sprint 2 Development and Testing': '#ff7f0e',
    'Sprint 2 Review and Retrospective': '#cc5800',
    'Sprint 3 Planning': '#2ca02c',
    'Sprint 3 Development and Testing': '#2ca02c',
    'Sprint 3 Review and Retrospective': '#196619',
}

# Custom color mapping for phases in the complete implementation plan
phase_color_mapping = {
    'Phase 1: Planning and Preparation': '#1f77b4',
    'Phase 2: Execution and Monitoring': '#ff7f0e',
    'Phase 3: Evaluation and Adjustment': '#2ca02c'
}

# Sidebar navigation
page = st.sidebar.radio(
    "Select a phase to view:",
    (
        "Phase 1: Planning and Preparation",
        "Phase 2: Execution and Monitoring",
        "Phase 3: Evaluation and Adjustment",
        "Complete Implementation Plan"
    )
)

# Function to create a Gantt chart for a specific phase
def create_gantt_chart(df, phase, color_mapping=None):
    if color_mapping:
        color_scale = alt.Scale(domain=list(color_mapping.keys()), range=list(color_mapping.values()))
        chart = alt.Chart(df[df['Phase'] == phase]).mark_bar().encode(
            x=alt.X('Start:T', title='Date'),
            x2='End:T',
            y=alt.Y('Task:N', title='Tasks', sort=alt.EncodingSortField(field='Start', order='ascending')),
            color=alt.Color('Task:N', scale=color_scale)
        ).properties(
            title=phase,
            width=900,  # Adjust width for better label visibility
            height=500  # Adjust height for better label visibility
        ).configure_axis(
            labelFontSize=14,
            titleFontSize=16
        ).configure_legend(
            labelFontSize=14,
            titleFontSize=16,
            labelLimit=500  # Increase the label limit to avoid truncation
        )
    else:
        chart = alt.Chart(df[df['Phase'] == phase]).mark_bar().encode(
            x=alt.X('Start:T', title='Date'),
            x2='End:T',
            y=alt.Y('Task:N', title='Tasks', sort=alt.EncodingSortField(field='Start', order='ascending')),
            color=alt.Color('Task:N', legend=None)
        ).properties(
            title=phase,
            width=900,  # Adjust width for better label visibility
            height=500  # Adjust height for better label visibility
        ).configure_axis(
            labelFontSize=14,
            titleFontSize=16
        ).configure_legend(
            labelFontSize=14,
            titleFontSize=16,
            labelLimit=500  # Increase the label limit to avoid truncation
        )
    return chart

# Explanatory text and chart based on the selected page
if page == "Phase 1: Planning and Preparation":
    st.title('Phase 1: Planning and Preparation (May 21 - May 27)')
    st.altair_chart(create_gantt_chart(df, "Phase 1: Planning and Preparation"), use_container_width=True)
    st.write("""
    **Finalize Detailed Project Scope and Objectives (May 21 - May 22)**
      - **Goals Refinement**:
        - Review and finalize the goals to ensure they are specific, measurable, achievable, relevant, and time-bound (SMART).
      - **Detailed Deliverables**:
        - Break down deliverables into more specific components.
        - Define success criteria for each deliverable.
      - **Scope Detailing**:
        - Outline detailed project scope to avoid scope creep.
        - Define boundaries and exclusions clearly.
      - **Stakeholder Alignment**:
        - Confirm objectives and scope with all key stakeholders.
        - Ensure that the project aligns with client needs and business objectives.
    """)
    st.write("""
    **Stakeholder Alignment and Communication Plan (May 23 - May 25)**
    - **Stakeholder Identification**:
      - Clients: 50 key clients representing various industries.
      - End-Users: 2000 active users from different client organizations.
      - Development Team: 3 scrum teams.
      - Management: Executive sponsors, product managers.
    - **Roles and Responsibilities**:
      - Project Sponsor: Reinhard Vock, VP of Product Development.
      - Project Manager: Timur Timerbaev.
      - Client Liaison: Arutyun Enfendzhyan.
      - Scrum Teams: Responsible for development and testing.
    - **Communication Plan**:
      - Weekly Status Reports: Sent every Friday using **Teams**.
      - Monthly Review Meetings: First Monday of each month via **Teams**.
      - Communication Channels: **Teams** & **Jira**.
      - Feedback Loops: Monthly surveys using **Teams**.
    """)
    st.write("""
    **Team Training and Tool Setup (May 26 - May 27)**
    - **Agile Training**: Conduct Agile training sessions for the teams.
    - **Tool Setup**: Set up Jira, Confluence, and Teams for project management and communication.
    """)

elif page == "Phase 2: Execution and Monitoring":
    st.title('Phase 2: Execution and Monitoring (May 28 - July 8)')
    st.altair_chart(create_gantt_chart(df, "Phase 2: Execution and Monitoring", color_mapping), use_container_width=True)
    st.write("""
    **Sprint 1 (May 28 - June 10)**
    - **Sprint Planning (May 28)**: Define sprint backlog, assign tasks in Jira.
    - **Development and Testing (May 29 - June 9)**: Focus on core functionality upgrades.
    - **Daily Stand-ups**: Held every morning at 9 AM via Teams.
    - **Sprint Review and Retrospective (June 10)**: Review completed work, gather feedback, and plan for the next sprint.

    **Sprint 2 (June 11 - June 24)**
    - **Sprint Planning (June 11)**: Define sprint backlog, assign tasks in Jira.
    - **Development and Testing (June 12 - June 23)**: Focus on integration with existing client systems.
    - **Daily Stand-ups**: Held every morning at 9 AM via Teams.
    - **Sprint Review and Retrospective (June 24)**: Review completed work, gather feedback, and plan for the next sprint.

    **Sprint 3 (June 25 - July 8)**
    - **Sprint Planning (June 25)**: Define sprint backlog, assign tasks in Jira.
    - **Development and Testing (June 26 - July 7)**: Focus on finalizing features and fixing bugs.
    - **Daily Stand-ups**: Held every morning at 9 AM via Teams.
    - **Sprint Review and Retrospective (July 8)**: Review completed work, gather feedback, and prepare for release.

    **Continuous Client and User Involvement (May 28 - July 8)**
    - **Co-creation Workshops**: First workshop on June 1, second on July 1.
    - **Beta Testing**: Beta phase starts June 15, ends July 1.
    - **Feedback Mechanisms**: In-app feedback tool set up by June 1, ongoing surveys via Teams.
    """)

elif page == "Phase 3: Evaluation and Adjustment":
    st.title('Phase 3: Evaluation and Adjustment (July 9 - July 15)')
    st.altair_chart(create_gantt_chart(df, "Phase 3: Evaluation and Adjustment"), use_container_width=True)
    st.write("""
    **Post-Implementation Review (July 9 - July 10)**
    - **Comprehensive Review**:
      - **Success Metrics**:
        - **On-time Delivery**: 95% of sprints completed on schedule.
        - **Budget Adherence**: Project completed within 10% of budget.
        - **Client Satisfaction**: 85% positive feedback from clients using **Teams**.
    - **Lessons Learned**:
      - **What Worked**: Effective client involvement, robust feedback loops documented in **Confluence**.
      - **Areas for Improvement**: Need for better initial scope definition.

    **Adjustments Based on Feedback and Performance Metrics (July 11 - July 15)**
    - **Continuous Improvement**:
      - **Client Feedback**: Implemented 15 major client-requested features post-launch tracked in **Jira**.
      - **User Feedback**: Addressed 30 usability issues identified by end-users through **Hotjar**.
    - **Refinement**:
      - **Process Adjustments**: Streamlined the sprint planning process using **Jira**.
      - **Tool Enhancements**: Upgraded project management tools for better tracking, such as **Asana** for project management.
    """)

elif page == "Complete Implementation Plan":
    st.title("Complete Implementation Plan")
    st.write("""
    This view shows the complete implementation plan, combining all phases into a comprehensive Gantt chart.
    """)
    complete_color_scale = alt.Scale(domain=list(phase_color_mapping.keys()), range=list(phase_color_mapping.values()))
    complete_chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Start:T', title='Date'),
        x2='End:T',
        y=alt.Y('Task:N', title='Tasks', sort=alt.EncodingSortField(field='Start', order='ascending')),
        color=alt.Color('Phase:N', scale=complete_color_scale, title='Phase')
    ).properties(
        title='Complete Implementation Plan',
        width=900,  # Adjust width for better label visibility
        height=600  # Adjust height for better label visibility
    ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
    ).configure_legend(
        labelFontSize=14,
        titleFontSize=16,
        labelLimit=500  # Increase the label limit to avoid truncation
    )
    st.altair_chart(complete_chart, use_container_width=True)
