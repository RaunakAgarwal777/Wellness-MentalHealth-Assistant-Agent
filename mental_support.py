import streamlit as st
import openai
from openai import AzureOpenAI

# Azure OpenAI API Configuration
client = AzureOpenAI(
    api_key="8WxLaoodYxa7XSK2rCiWuP3nqwWUShSUVd5FrjEYSqqROfIwc0qzJQQJ99BFAC77bzfXJ3w3AAABACOGweq",
    api_version="2024-12-01-preview",
    azure_endpoint="https://mindcraft-kapidhwaj-openai-api-key.openai.azure.com/"
)

DEPLOYMENT_NAME = "mindcraft-gpt4o"

# Title
st.title("Mental Health Check-Up Assistant")

# Initialize conversation history
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []

# Display conversation
for msg in st.session_state['conversation_history']:
    role = "You" if msg['role'] == "user" else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

# User input
user_input = st.text_input("How are you feeling today?")

def generate_response(user_msg):
    st.session_state['conversation_history'].append({"role": "user", "content": user_msg})
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=st.session_state['conversation_history']
    )
    reply = response.choices[0].message.content
    st.session_state['conversation_history'].append({"role": "assistant", "content": reply})
    return reply

if user_input:
    with st.spinner("Checking in with you..."):
        reply = generate_response(user_input)
        st.markdown(f"**AI:** {reply}")
