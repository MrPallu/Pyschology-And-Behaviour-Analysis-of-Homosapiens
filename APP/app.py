import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Load Data
# -------------------------------


df = pd.read_csv("data/cleaned_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

sns.set_style("whitegrid")

colors = ["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974"]
# Style settings (GLOBAL PREMIUM LOOK)
sns.set_style("whitegrid")
plt.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 14,
    "axes.labelsize": 11
})

# -------------------------------
# Title + Info
# -------------------------------
st.title("🧠 Human Behaviour Analysis")

st.markdown("## 👨‍💻 Palash Malviya")
st.write("B.Tech Student")
st.write("Project: Psychology and Behaviour Analysis of Homo sapiens using Data Science")

st.markdown("---")

# -------------------------------
# Dataset Preview
# -------------------------------
st.header("📊 Dataset Preview")
st.write(df.head())
st.write("Dataset Shape:", df.shape)

st.markdown("---")

# -------------------------------
# Detect Columns Automatically
# -------------------------------
columns = df.columns.tolist()

screen_col = next((col for col in columns if "screen" in col), columns[0])
gender_col = next((col for col in columns if "gender" in col), columns[1])
stress_col = next((col for col in columns if "stress" in col), columns[2])

# -------------------------------
# Clean Labels (IMPORTANT)
# -------------------------------
df[screen_col] = df[screen_col].replace({
    "Less than 2 hours": "<2h",
    "2-4 hours": "2-4h",
    "4-6 hours": "4-6h",
    "6-8 hours": "6-8h",
    "More than 8 hours": ">8h"
})

# Optional stress label cleanup (edit if needed)
df[stress_col] = df[stress_col].replace({
    "I try to stay calm and think logically": "Logical",
    "I feel anxious and overwhelmed": "Anxious",
    "I ignore the situation": "Avoid"
})

# -------------------------------
# GRAPH 1: Screen Time
# -------------------------------
st.subheader("📊 Daily Screen Time Usage")

fig, ax = plt.subplots()
sns.countplot(x=screen_col, data=df, ax=ax, palette="Blues")

ax.set_title("Distribution of Daily Screen Time")
ax.set_xlabel("Screen Time Range")
ax.set_ylabel("Number of Individuals")

st.pyplot(fig)

st.markdown("---")

# -------------------------------
# GRAPH 2: Gender
# -------------------------------
st.subheader("👥 Gender Distribution")

fig, ax = plt.subplots()
sns.countplot(x=gender_col, data=df, ax=ax, palette="Greens")

ax.set_title("Gender-wise Participation")
ax.set_xlabel("Gender")
ax.set_ylabel("Count")

st.pyplot(fig)

st.markdown("---")

# -------------------------------
# GRAPH 3: Stress Response
# -------------------------------
st.subheader("😵 Stress Response Patterns")

fig, ax = plt.subplots()
sns.countplot(x=stress_col, data=df, ax=ax, palette="coolwarm")

plt.xticks(rotation=20)
ax.set_title("Common Stress Responses")
ax.set_xlabel("Response Type")
ax.set_ylabel("Frequency")

st.pyplot(fig)

st.markdown("---")

# -------------------------------
# GRAPH 4: Screen Time vs Stress
# -------------------------------
st.subheader("📉 Screen Time vs Stress Behaviour")

fig, ax = plt.subplots()
sns.boxplot(x=stress_col, y=screen_col, data=df, ax=ax, palette="Set2")

plt.xticks(rotation=20)
ax.set_title("Impact of Screen Time on Stress")
ax.set_xlabel("Stress Response")
ax.set_ylabel("Screen Time Category")

st.pyplot(fig)

st.markdown("---")

# -------------------------------
# Cool Feature
# -------------------------------
st.subheader("🔥 Most Common Behaviour")

top_behavior = df[stress_col].value_counts().idxmax()
st.write(f"Most common stress response: **{top_behavior}**")

st.markdown("---")

# -------------------------------
# Insights
# -------------------------------
st.header("🧠 Insights")

st.write("• Screen time usage varies across individuals.")
st.write("• Stress responses show clear behavioural patterns.")
st.write("• Some coping mechanisms are more common than others.")
st.write("• Behaviour is influenced by psychological and social factors.")

st.markdown("---")

# -------------------------------
# Conclusion
# -------------------------------
st.subheader("📌 Conclusion")

st.write("This project analyzes human behaviour using data visualization.")
st.write("It highlights how screen usage and stress influence decision-making.")
st.write("The findings help understand patterns in modern human behaviour.")

st.markdown("---")

# -------------------------------
# Footer
# -------------------------------
st.write("© 2026 Palash Malviya | Psychology and Behaviour Analysis Project")