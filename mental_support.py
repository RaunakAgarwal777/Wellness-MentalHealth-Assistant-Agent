import streamlit as st
from openai import OpenAI

# ✅ Replace with your real OpenAI key
client = OpenAI(api_key="sk-PUBLIC-DEMO-ONLY-DONT-USE-FOR-HACKATHON")

st.set_page_config(page_title="Mental Health Agent", page_icon="🧠")
st.title("🧠 Mental Health Check-In Agent")
st.caption("Your friendly AI companion for emotional support.")

# Store chat in session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a compassionate mental health assistant who listens and encourages."}
    ]

# Show conversation
for msg in st.session_state.chat_history[1:]:
    role = "You" if msg["role"] == "user" else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

# Get input
user_input = st.text_input("How are you feeling today?")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.chat_history
            )
            reply = response.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            st.markdown(f"**AI:** {reply}")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")


