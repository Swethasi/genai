import google.generativeai as genai
import streamlit as st
import uuid

def get_user_id():
    if 'user_id' not in st.session_state:
        st.session_state['user_id'] = str(uuid.uuid4())
    return st.session_state['user_id']

user_id = get_user_id()

st.title("user")
genai.configure(api_key="AIzaSyA_WFeiz49dqcZ-2MDunqP9sZxHmpZkBwY")

model = genai.GenerativeModel('gemini-1.5-flash')
input_one =st.chat_input()
response = model.generate_content(input_one)
st.write(f"Your unique user ID is: {user_id}")

print(response.text)