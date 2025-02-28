import streamlit as st
import random
import pandas as pd
from datetime import datetime


st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #eef2f3, #8e9eab);
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #4b6cb7, #182848);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
    }
    h1, h2, h3 {
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .sidebar h2 {
        color: #ffffff;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .sidebar input, .sidebar textarea, .sidebar select {
        width: 100%;
        padding: 8px;
        border-radius: 8px;
        border: none;
        margin-bottom: 10px;
    }
    .sidebar .stTextInput, .sidebar .stSelectbox, .sidebar .stTextArea {
        color: black;
    }
    .stButton button {
        background: linear-gradient(135deg, #ff7eb3, #ff758c);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #ff758c, #ff7eb3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if "users" not in st.session_state:
    st.session_state.users = {}


st.markdown("<h1 style='color: #2c3e50;'>🚀 Mindset Mastery</h1>", unsafe_allow_html=True)


st.sidebar.markdown("<h2>👤 Your Profile</h2>", unsafe_allow_html=True)
name = st.sidebar.text_input("Enter your name")
goal = st.sidebar.text_input("Your biggest learning goal")
learning_style = st.sidebar.selectbox("Your preferred learning style", ["Visual", "Reading/Writing", "Hands-on", "Listening"])
bio = st.sidebar.text_area("Short bio about yourself")
interests = st.sidebar.text_input("Your interests (e.g., coding, art, science)")

if name:
    if name not in st.session_state.users:
        st.session_state.users[name] = {
            "effort": 8,
            "learning": 7,
            "streak": 0,
            "mood": "😊",
            "habits": {},
            "weekly_reflection": ""
        }

    st.markdown(f"<h2>Welcome, {name}! 🌟</h2>", unsafe_allow_html=True)
    st.markdown(f"**Your Goal:** {goal}")
    st.markdown(f"**Learning Style:** {learning_style}")
    st.markdown(f"**Bio:** {bio}")
    st.markdown(f"**Interests:** {interests}")


    quotes = [
        "Every small step you take brings you closer to your goal.",
        "Challenges are opportunities in disguise.",
        "Your potential is limitless—keep pushing forward.",
        "Success is a journey, not a destination."
    ]
    if st.button("🔄 Get a new motivation quote"):
        st.session_state.quote = random.choice(quotes)
    st.markdown(f"**💡 Daily Motivation:** {st.session_state.get('quote', random.choice(quotes))}")

    st.session_state.users[name]["effort"] = st.slider("Effort Level (1-10)", 1, 10, st.session_state.users[name]["effort"])
    st.session_state.users[name]["learning"] = st.slider("Learning Level (1-10)", 1, 10, st.session_state.users[name]["learning"])
    
  
    mood = st.radio("How are you feeling today?", ["😊 Happy", "😄 Excited", "😐 Neutral", "😔 Sad", "😡 Angry"], horizontal=True)
    st.session_state.users[name]["mood"] = mood
    
   
    st.session_state.users[name]["streak"] += 1
    st.markdown(f"🔥 Learning Streak: {st.session_state.users[name]['streak']} days!")

   
    st.markdown("### 📌 Habit Tracker")
    habits = ["Read 10 pages", "Watch a tutorial", "Practice coding", "Meditate", "Write a summary"]
    completed_habits = []
    for habit in habits:
        if st.checkbox(f"✅ {habit}"):
            completed_habits.append(habit)
    st.session_state.users[name]["habits"] = completed_habits

   
    st.session_state.users[name]["weekly_reflection"] = st.text_area("📝 Weekly Reflection", value=st.session_state.users[name]["weekly_reflection"])
    if st.button("Submit Reflection"):
        st.success("Reflection saved! Keep going! 🌟")

 
    st.markdown("### 🏆 Leaderboard")
    leaderboard_data = [
        {
            "Name": user,
            "Effort": data["effort"],
            "Learning": data["learning"],
            "Streak": data["streak"]
        }
        for user, data in st.session_state.users.items()
    ]
    df = pd.DataFrame(leaderboard_data).sort_values(by=["Streak", "Effort", "Learning"], ascending=False)
    st.table(df)

  
    st.markdown("### 📊 Learning Progress")
    st.line_chart(df.set_index("Name")["Streak"], use_container_width=True)
