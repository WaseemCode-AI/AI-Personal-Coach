import streamlit as st
from chatbot.py import chat_with_ai
from database import add_user, update_progress
from goal_tracker import track_progress

st.title("🤖 AI Personal Coach")
st.subheader("Self-Improvement | Fitness | Motivation")

name = st.text_input("Aapka naam kya hai?")
goal = st.text_input("Aapka goal kya hai?")
progress = st.slider("Aapka progress kitna hai?", 0, 100, 0)

if st.button("Save Progress"):
    add_user(name, goal)
    update_progress(name, progress)
    st.success("Progress saved!")

user_input = st.text_input("AI se baat karo:")
if st.button("Ask AI"):
    response = chat_with_ai(user_input)
    st.write("💡 AI Response:", response)

if st.button("Motivation"):
    motivation = track_progress(goal, progress)
    st.write("🔥", motivation)
