import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="College Club Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Custom Design
st.markdown("""
<style>
.stApp {
    background-color: #F3F6FC;
}
h1 {
    color: #17365D;
}
h2, h3 {
    color: #24527A;
}
[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #DCE5F0;
}
</style>
""", unsafe_allow_html=True)

# Heading
st.title("🎓 College Club Membership Dashboard")
st.markdown("### Welcome to College Club Analysis")
st.write("Explore student membership and club participation.")

# Load Dataset
df = pd.read_csv("club_membership.csv")

# Statistics
total_students = len(df)
total_clubs = df["Club"].nunique()
club_counts = df["Club"].value_counts()

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("👨‍🎓 Total Students", total_students)
col2.metric("🏆 Total Clubs", total_clubs)
col3.metric("⭐ Most Popular Club", club_counts.idxmax())

st.divider()

# Bar Chart and Pie Chart
st.subheader("📊 Club Membership Overview")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.barplot(
        x=club_counts.index,
        y=club_counts.values,
        ax=ax
    )
    ax.set_title("Students in Each Club")
    ax.set_xlabel("Clubs")
    ax.set_ylabel("Students")
    ax.tick_params(axis="x", rotation=25)
    st.pyplot(fig)
    plt.close(fig)

with col2:
    fig2, ax2 = plt.subplots(figsize=(7, 5))
    ax2.pie(
        club_counts.values,
        labels=club_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax2.set_title("Membership Distribution")
    st.pyplot(fig2)
    plt.close(fig2)

st.divider()

# Seaborn Count Plot
st.subheader("📈 Club-wise Student Count")

fig3, ax3 = plt.subplots(figsize=(9, 5))
sns.countplot(data=df, x="Club", ax=ax3)
ax3.set_title("Number of Students in Each Club")
ax3.set_xlabel("Club")
ax3.set_ylabel("Number of Students")
ax3.tick_params(axis="x", rotation=25)
st.pyplot(fig3)
plt.close(fig3)

st.divider()

# Heatmap
st.subheader("🔥 Club Membership by Academic Year")

club_year = pd.crosstab(df["Club"], df["Year"])

fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.heatmap(
    club_year,
    annot=True,
    cmap="Blues",
    fmt="d",
    ax=ax4
)
ax4.set_title("Club and Year Distribution")
st.pyplot(fig4)
plt.close(fig4)

st.divider()

# Student Records
st.subheader("📋 Student Membership Records")

selected_club = st.selectbox(
    "Select a Club",
    ["All Clubs"] + sorted(df["Club"].unique().tolist())
)

if selected_club == "All Clubs":
    filtered_df = df
else:
    filtered_df = df[df["Club"] == selected_club]

st.dataframe(filtered_df, use_container_width=True)

st.caption("College Club Membership Analysis | Python Project")
