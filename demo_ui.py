import streamlit as st

st.set_page_config(page_title="CHIRP CHAT",
                  page_icon="🐥",
                  layout="wide",
                  initial_sidebar_state="expanded")

st.title('orange[CHIRP CHAT]')
user_input = st.text_area(label=":green[Welcome to CHIRP CHAT! Type in your bird-brained questions]")
