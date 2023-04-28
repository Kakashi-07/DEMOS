import streamlit as st

st.set_page_config(page_title="CHIRP CHAT",
                  page_icon="🐥",
                  layout="wide",
                  initial_sidebar_state="expanded")

#st.title(':orange[CHIRP CHAT]')
st.markdown("<h1 style='text-align: center;'>:orange[CHIRP CHAT]</h1>", unsafe_allow_html=True,)

# tabs
tab1, tab2 = st.tabs(["CHAT HERE 💬", " Uploaded Documents 📄"])

tab1.markdown(
    "<h1 style='text-align: center;'>Talk With CHIRP CHAT</h1>",
    unsafe_allow_html=True,
)

user_input = st.text_area(label=":green[Welcome to CHIRP CHAT! Type in your bird-brained questions]")

